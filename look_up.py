from typing import Any, Protocol, Mapping


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
