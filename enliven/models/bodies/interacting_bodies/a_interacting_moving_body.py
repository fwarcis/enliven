from abc import ABC

from attrs import define

from enliven.models.bodies.a_moving_body import AMovingBody
from enliven.models.bodies.interacting_bodies.a_interacting_body import AInteractingBody
from enliven.models.quantities.vector import Vector


@define
class AInteractingMovingBody(AInteractingBody, AMovingBody, ABC):
    def accelerate(self, dt: float, force: Vector) -> None:
        self._speed += force * dt / self._inter_data.mass
