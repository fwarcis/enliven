from abc import ABC

from attrs import define

from enliven.models.bodies.a_body import ABody
from enliven.models.quantities.vector import Vector


@define
class AMovingBody(ABody, ABC):
    _speed: Vector = Vector()

    @property
    def speed(self) -> Vector:
        return self._speed

    def move(self) -> None:
        self._pos += self._speed
