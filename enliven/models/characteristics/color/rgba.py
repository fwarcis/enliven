from attr import define, field

from enliven.common.validators.by_range.by_range import ByRangeValidator
from enliven.common.validators.by_range.comparison_operators import GTE, LTE
from enliven.models.characteristics.color.a_color import AColor

validate_color_range = ByRangeValidator(GTE(0), LTE(255))
validate_alpha_range = ByRangeValidator(GTE(0), LTE(1))


@define
class RGBA(AColor):
    r: int = field(validator=[validate_color_range])
    g: int = field(validator=[validate_color_range])
    b: int = field(validator=[validate_color_range])
    a: float = field(validator=[validate_alpha_range])
