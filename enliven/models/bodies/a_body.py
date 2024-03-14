from abc import ABC

from attrs import define

from enliven.models.characteristics.color.rgba import RGBA
from enliven.models.quantities.position import Position


@define
class ABody(ABC):
    _color: RGBA = RGBA(0, 0, 0, 1)
    _pos: Position = Position()

    @property
    def color(self) -> RGBA:
        return self._color

    @property
    def pos(self) -> Position:
        return self._pos
