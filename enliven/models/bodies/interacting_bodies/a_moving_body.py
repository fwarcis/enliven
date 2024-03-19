from attrs import define

from enliven.models.bodies.interacting_bodies.a_interacting_body import AInteractingBody
from enliven.models.quantities.vector import Vector


@define
class AMovingBody(AInteractingBody):
    _speed: Vector = Vector()

    @property
    def speed(self) -> Vector:
        return self._speed

    @speed.setter
    def speed(self, new: Vector):
        self._speed = new

    def move(self) -> None:
        self._pos += self._speed

    def accelerate(self, dt: float, force: Vector) -> None:
        self._speed += force * dt / self._inter_data.mass