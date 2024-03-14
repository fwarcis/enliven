from abc import ABC, abstractmethod
from typing import Any, Sequence


class IBehaviour(ABC):
    @abstractmethod
    def work(self, entities: Sequence[Any]) -> Any:
        pass
