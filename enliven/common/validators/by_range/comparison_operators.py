from abc import ABC, abstractmethod
from typing import TypeGuard

from attr import define


@define
class AComparisonOperator(ABC):
    right: float

    @abstractmethod
    def compare(self, left: float) -> TypeGuard[float]:
        pass


class LT(AComparisonOperator):
    def compare(self, left: float) -> TypeGuard[float]:
        return left < self.right


class LTE(AComparisonOperator):
    def compare(self, left: float) -> TypeGuard[float]:
        return left <= self.right


class GT(AComparisonOperator):
    def compare(self, left: float) -> TypeGuard[float]:
        return left > self.right


class GTE(AComparisonOperator):
    def compare(self, left: float) -> TypeGuard[float]:
        return left >= self.right
