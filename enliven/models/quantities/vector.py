from attrs import define, field

from enliven.models.quantities.a_quantity import AQuantity


@define
class Vector(AQuantity):
    __dimensions__: tuple[str, ...] = field(default=("a", "b"), init=False)

    a: float = 0.0
    b: float = 0.0
