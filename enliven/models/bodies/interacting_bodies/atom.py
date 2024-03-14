from attrs import define

from enliven.models.bodies.interacting_bodies.a_interacting_moving_body import (
    AInteractingMovingBody,
)


@define
class Atom(AInteractingMovingBody):
    _radius: float = 5.0

    @property
    def radius(self) -> float:
        return self._radius
