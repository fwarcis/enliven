from abc import ABC

from attrs import define

from enliven.models.bodies.a_body import ABody


@define
class InteractionData:
    _mass: float = 1.0
    _charge: float = 1.0

    @property
    def mass(self) -> float:
        return self._mass

    @property
    def charge(self) -> float:
        return self._charge


@define
class AInteractingBody(ABody, ABC):
    _inter_data: InteractionData = InteractionData()

    @property
    def inter_data(self) -> InteractionData:
        return self._inter_data
