from operator import add, sub, mul, floordiv
from attrs import define, field
from types import FunctionType
from enum import Enum
from pygame import Color

@define
class IntVec:
    x: int = field()
    y: int = field()

    @staticmethod
    def from_tuple(tpl: tuple[int, int] | list[int]) -> "IntVec":
        return IntVec(tpl[0], tpl[1])

    def to_tuple(self) -> tuple[int, int]:
        return self.x, self.y

    def is_inbounds(self, pos: "IntVec", size: "IntVec") -> bool:
        return (self.x > pos.x) and (self.x < pos.x + size.x) and (self.y > pos.y) and (self.x < pos.y + size.y)

    def __str__(self):
        return f"I<{self.x}; {self.y}>"

    # Sometimes I fear myself
    @staticmethod
    def _wrap_operator(func: FunctionType) -> FunctionType:
        def _apply_func(self, other):
            match other:
                case IntVec():
                    return IntVec(func(self.x, other.x), func(self.y, other.y))
                case int():
                    return IntVec(func(self.x, other), func(self.y, other))
                case _:
                    raise NotImplementedError
        return _apply_func

    __add__ = _wrap_operator(add)
    __mul__ = _wrap_operator(mul)
    __sub__ = _wrap_operator(sub)
    # __truediv__ = NotImplemented
    __floordiv__ = _wrap_operator(floordiv)



class InteractionState(Enum):
    NOT_INTERACTING = 0
    HOVERING = 1
    INTERACTING = 2


@define
class ColorScheme:
    text_color: Color
    primary: Color
    background: Color
    border: Color
    disabled: Color

    font_name: str
    font_al: bool # Stands for anitaliasing

@define
class Padding:
    @staticmethod
    def round(size: int):
        # TODO: Make adaptive
        return Padding(*[size for _ in range(4)])

    top: int
    left: int
    bottom: int
    right: int
