from attrs import define, field

from enliven.common.validators.a_validator import AValidator
from enliven.common.validators.by_range.comparison_operators import (
    GT,
    GTE,
    LT,
    LTE,
)


@define
class ByRangeValidator(AValidator[float]):  # type: ignore
    _gt: GT | GTE
    _lt: LT | LTE
    _val: float = field(init=False)

    def _validate(self, val: float) -> None:  # type: ignore
        self._val: float = val

        self._validate_gt()
        self._validate_lt()

    def _validate_lt(self) -> None:
        if not self._lt.compare(left=self._val):
            raise ValueError(f"{self._val} is not less then {self._lt.right}")

    def _validate_gt(self) -> None:
        if not self._gt.compare(left=self._val):
            raise ValueError(f"{self._val} is not greater then {self._gt.right}")


validate_positivity = ByRangeValidator(GTE(0), LT(float("+inf")))
