"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730470131"


class Simpy:
    """Simpy Class."""
    values: list[float]

    def __init__(self, values: list[float]):
        """Itself."""
        self.values = values

    def __repr__(self) -> str:
        """Returns a string of simpy."""
        return f"Simpy({self.values})"

    def fill(self, float_value: float, int_value: int) -> None:
        """Fill a simpy's values with a specific number of repeating values."""
        self.values = [float_value] * int_value
    
    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fill in the values attribute with range of values."""
        assert step != 0.0
        self.values = []
        current_value: float = start
        if step > 0:
            while current_value < stop:
                self.values.append(current_value)
                current_value += step
        else:
            while current_value > stop:
                self.values.append(current_value)
                current_value += step

    def sum(self) -> float:
        """Finds sum of values."""
        total: float = sum(self.values)
        return total

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Adds both sides."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            for item in self.values:
                result.values.append(item + rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.values.append(self.values[i] + rhs.values[i])
        return result

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Conducts the power value."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            for item in self.values:
                result.values.append(item ** rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.values.append(self.values[i] ** rhs.values[i])
        return result

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Checks if is equal too."""
        result: list[bool] = []
        if isinstance(rhs, float):
            for item in self.values:
                if item == rhs:
                    result.append(True)
                else:
                    result.append(False)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                if self.values[i] == rhs.values[i]:
                    result.append(True)
                else:
                    result.append(False)
        return result

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Checks if item is greater than."""
        result: list[bool] = []
        if isinstance(rhs, float):
            for item in self.values:
                if item > rhs:
                    result.append(True)
                else:
                    result.append(False)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                if self.values[i] > rhs.values[i]:
                    result.append(True)
                else:
                    result.append(False)
        return result

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Returns values in simpy."""
        if isinstance(rhs, int):
            return self.values[rhs]
        else:
            result: Simpy = Simpy([])
            i: int = 0
            while i < len(rhs):
                if rhs[i]:
                    result.values.append(self.values[i])
                i += 1
            return result