from __future__ import annotations
from types import NotImplementedType
from typing import Final

class DistanceUnit:
    name: Final[str]

    factor: Final[float]
    """Multiplying factor compared to m.

    For example, for km, this is 1,000.
    """

    def __init__(self, name: str, factor: float) -> None:
        self.name = name
        self.factor = factor

    def __repr__(self) -> str:
        return self.name

M = DistanceUnit("m", 1.0)
KM = DistanceUnit("km", 1000.0)
MM = DistanceUnit("mm", 0.001)

class Distance:
    value: Final[float]
    unit: Final[DistanceUnit]

    def __init__(self, value: float, unit: DistanceUnit) -> None:
        self.value = value
        self.unit = unit

    def __repr__(self) -> str:
        return f"Distance({repr(self.value)}, {repr(self.unit)})"

    def __str__(self) -> str:
        return f"{self.value} {self.unit}"

    def value_as(self, unit: DistanceUnit) -> float:
        return self.value * self.unit.factor / unit.factor

    @property
    def value_m(self) -> float:
        return self.value * self.unit.factor

    def __eq__(self, other: object) -> bool | NotImplementedType:
        match other:
            case Distance():
                return self.value_m == other.value_m
            case _:
                return NotImplemented

    def __lt__(self, other: Distance) -> bool:
        return self.value_m < other.value_m

    def __le__(self, other: Distance) -> bool:
        return self.value_m <= other.value_m

    def __gt__(self, other: Distance) -> bool:
        return self.value_m > other.value_m

    def __ge__(self, other: Distance) -> bool:
        return self.value_m >= other.value_m

    def __add__(self, other: Distance) -> Distance:
        # we standardize to our unit
        return Distance(self.value + other.value_as(self.unit), self.unit)

    def __sub__(self, other: Distance) -> Distance:
        return self + (-other)

    def __neg__(self) -> Distance:
        return Distance(-self.value, self.unit)

    def __pos__(self) -> Distance:
        return self

    def __mul__(self, other: float) -> Distance:
        return Distance(self.value * other, self.unit)

    def __rmul__(self, other: float) -> Distance:
        return Distance(other * self.value, self.unit)

    def __truediv__(self, other: float) -> Distance:
        return Distance(self.value / other, self.unit)
