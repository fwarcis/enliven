from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

from attr import define
from attrs import Attribute


@define
class AValidator[Value: Any](ABC):  # type: ignore
    def __call__(self, obj: Any, attr: Attribute[Value], val: Value) -> None:  # type: ignore
        self._validate(val)

    @abstractmethod
    def _validate(self, val: Value) -> None:  # type: ignore
        pass
