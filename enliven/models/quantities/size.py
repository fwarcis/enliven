from attrs import define, field

from enliven.common.validators.by_range.by_range import validate_positivity
from enliven.models.quantities.a_quantity import AQuantity


@define
class Size(AQuantity):
    __dimensions__: tuple[str, ...] = field(default=("width", "height"), init=False)

    width: float = field(validator=[validate_positivity])
    height: float = field(validator=[validate_positivity])
