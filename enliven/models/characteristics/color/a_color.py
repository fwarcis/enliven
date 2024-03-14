from abc import ABC
from typing import Any

from attrs import define


@define
class AColor(ABC):
    r: Any
    g: Any
    b: Any
    a: Any
