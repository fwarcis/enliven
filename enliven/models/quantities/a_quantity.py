from abc import ABC
from operator import add, iadd, imul, isub, itruediv, mul, sub, truediv
from typing import Any, Protocol, Self, runtime_checkable

from attrs import define, field

from enliven.common.tools.classes import get_attrs
from enliven.common.tools.operations import OperatorT, calc_pairs


@runtime_checkable
class Dimensions(Protocol):
    __dimensions__: tuple[str, ...]


@define
class AQuantity(Dimensions, ABC):
    __nondimensionals__: tuple[str, ...] = field(init=False)
    __dimensions__: tuple[str, ...] = field(init=False)

    def __attrs_post_init__(self) -> None:
        self.__nondimensionals__ = tuple(set(self.__slots__) - set(self.__dimensions__))  # type: ignore

    def __add__(self, right: Dimensions) -> Self:
        return type(self)(**self._get_all_kwargs(add, right))

    def __sub__(self, right: Dimensions) -> Self:
        return type(self)(**self._get_all_kwargs(sub, right))

    def __mul__(self, right: Dimensions | float) -> Self:
        return type(self)(**self._get_all_kwargs(mul, right))

    def __truediv__(self, right: Dimensions | float) -> Self:
        return type(self)(**self._get_all_kwargs(truediv, right))

    def __iadd__(self, right: Dimensions) -> Self:
        return type(self)(**self._get_all_kwargs(iadd, right))

    def __isub__(self, right: Dimensions) -> Self:
        return type(self)(**self._get_all_kwargs(isub, right))

    def __imul__(self, right: Dimensions | float) -> Self:
        return type(self)(**self._get_all_kwargs(imul, right))

    def __itruediv__(self, right: Dimensions | float) -> Self:
        return type(self)(**self._get_all_kwargs(itruediv, right))

    def _get_all_kwargs(
        self, op: OperatorT, right: Dimensions | float
    ) -> dict[str, float | Any]:
        dimensions_vars: dict[str, float] = dict(
            zip(self.__dimensions__, self._calc_dimensions_vals(op=op, right=right))
        )
        nondimensional_vars: dict[str, Any] = dict(
            zip(
                self.__nondimensionals__,
                get_attrs(self, self.__nondimensionals__),
            )
        )

        return dict(**dimensions_vars, **nondimensional_vars)

    def _calc_dimensions_vals(
        self, op: OperatorT, right: Dimensions | float
    ) -> list[float]:
        left_vals: list[float] = get_attrs(self, self.__dimensions__)

        if isinstance(right, Dimensions):
            right_vals: list[float] = get_attrs(right, right.__dimensions__)
            right_vals_with_pass_filling: list[float] = right_vals + list(
                0.0 for _ in range(len(left_vals) - len(right_vals))
            )

            return calc_pairs(op, zip(left_vals, right_vals_with_pass_filling))

        return (mul_by_num := [op(left_val, right) for left_val in left_vals])  # type: ignore  # noqa: F841
