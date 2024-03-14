from functools import partial
from random import uniform
from typing import NamedTuple, Sequence

from attrs import astuple, define
from pygame import QUIT, Surface, init, quit
from pygame.display import flip, set_mode
from pygame.draw import circle
from pygame.event import get
from pygame.time import Clock

from enliven.models.bodies.interacting_bodies.a_interacting_body import (
    AInteractingBody,
)
from enliven.models.bodies.interacting_bodies.a_interacting_moving_body import (
    AInteractingMovingBody,
)
from enliven.models.bodies.interacting_bodies.atom import Atom
from enliven.models.complex_behaviours.interaction.a_interaction import AInteraction
from enliven.models.complex_behaviours.interaction.electromagnetism import (
    Electromagnetism,
)
from enliven.models.complex_behaviours.interaction.gravity import Gravity
from enliven.models.quantities.position import Position


class SizeT(NamedTuple):
    width: int
    height: int


@define
class GameConfig:
    size: SizeT
    fps: float
    bodies_count: int
    interactions: Sequence[AInteraction]


def init_game(size: SizeT) -> tuple[Surface, Clock]:
    init()

    return set_mode(size), Clock()


def gen_bodies(
    count: int,
    ins: type[AInteractingMovingBody] | partial[AInteractingMovingBody],
    poses: Sequence[Position],
) -> list[AInteractingMovingBody]:
    return [ins(pos=poses[i]) for i in range(count)]


def rand_pos(count: int, surface_size: SizeT) -> list[Position]:
    return [
        Position(uniform(0, surface_size.width), uniform(0, surface_size.height))
        for _ in range(count)
    ]


def handle_events() -> None:
    for event in get():
        if event.type == QUIT:
            quit()


def update_screen(surface: Surface, bodies: Sequence[AInteractingBody]) -> None:
    surface.fill("white")

    for body in bodies:
        if isinstance(body, Atom):
            pos_pair = body.pos.x, body.pos.y
            circle(surface, astuple(body.color), pos_pair, body.radius)

    flip()


def move_interacting_bodies(
    interactions: Sequence[AInteraction],
    bodies: Sequence[AInteractingMovingBody],
    dt: float,
) -> None:
    for interaction in interactions:
        forces = interaction.work(bodies)

        for force, body in zip(forces, bodies):
            body.accelerate(dt, force)
            body.move()


def main() -> None:
    cfg = GameConfig(
        SizeT(1280, 720),
        fps=60.0,
        bodies_count=30,
        interactions=[Gravity(), Electromagnetism()],
    )
    bodies: list[AInteractingMovingBody] = gen_bodies(
        cfg.bodies_count, partial(Atom), rand_pos(cfg.bodies_count, cfg.size)
    )

    surface, clock = init_game(cfg.size)

    while True:
        handle_events()
        move_interacting_bodies(cfg.interactions, bodies, dt=0.1)

        update_screen(surface, bodies)
        clock.tick(cfg.fps)


if __name__ == "__main__":
    main()
