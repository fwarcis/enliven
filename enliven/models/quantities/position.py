from attrs import define, field

from enliven.common.validators.by_range.by_range import validate_positivity
from enliven.models.quantities.a_quantity import AQuantity


@define
class Position(AQuantity):
    __dimensions__: tuple[str, ...] = field(default=("x", "y"), init=False)

    x: float = field(default=0.0, validator=[validate_positivity])
    y: float = field(default=0.0, validator=[validate_positivity])
