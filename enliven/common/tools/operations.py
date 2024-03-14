from typing import Any, Callable, Iterable

type OperatorT = Callable[[Any, Any], Any]  # type: ignore


def calc_pairs(op: OperatorT, pairs: Iterable[tuple[Any, Any]]) -> list[Any]:
    res: list[Any] = []

    for left, right in pairs:
        res.append(op(left, right))

    return res
