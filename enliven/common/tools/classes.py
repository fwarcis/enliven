from typing import Any, Iterable


def get_attrs(obj: Any, names: Iterable[str]) -> list[Any]:
    return [getattr(obj, attr) for attr in names]
