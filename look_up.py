from typing import Any, Protocol, Mapping, overload, Iterable, Sequence


class Comparable(Protocol):
    """
    This protocol defines what methods are required for a class to be considered comparable.
    """

    def __eq__(self, other: Any) -> bool:
        ...

    def __ne__(self, other: Any) -> bool:
        ...

    def __lt__(self, other: Any) -> bool:
        ...

    def __le__(self, other: Any) -> bool:
        ...

    def __gt__(self, other: Any) -> bool:
        ...

    def __ge__(self, other: Any) -> bool:
        ...


BaseMapping = Mapping[Comparable, Any]


class LookUp:
    """Our custom dictionary-like class that stores key-value pairs in sorted order."""

    @overload
    def __init__(self, source: Iterable[tuple[Comparable, Any]]) -> None:
        ...

    @overload
    def __init__(self, source: BaseMapping) -> None:
        ...

    def __init__(self, source: Iterable[tuple[Comparable, Any]] | BaseMapping | None = None) -> None:

        sorted_pairs: Sequence[tuple[Comparable, Any]]

        if isinstance(source, Mapping):
            sorted_pairs = sorted(source.items())
        elif isinstance(source, Sequence):
            sorted_pairs = sorted(source)
        else:
            sorted_pairs = []

        self.keys = [pair[0] for pair in sorted_pairs]
        self.values = [pair[1] for pair in sorted_pairs]
