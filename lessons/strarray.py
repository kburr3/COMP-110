"""An example of vectorized operations via operator overloading"""

from __future__ import annotations
from typing import Union   


class StrArray:
    items: list[str]

    def __init__(self, items: items[str]):
        self.items = items

    def __repr__(self) -> str:
        return f"StrArray({self.items})"

    def __add__(self, rhs: Union[str, StrArray]) -> StrArray:
        result: StrArray = StrArray([])
        # TODO
        if isinstance(rhs, str):
        # 1. Loop through each item in self's item list
            for item in self.items:
        #   2. Concatenate rhs to the item value
                item += rhs
        #   3. Append the resulting string to result's item's list
                result.items.append(item)
        else:
            assert len(self.items) == len(rhs.items)
            # 1. Loop through each index of self items list
            for i in range(len(self.items)):
            # 2. Concatenate the item at this index of self with the corresponding item
            #   at the same index of rhs's items list
                self.items[i] += rhs.items[i]
            # 3. Append the concatenated string to result's item list
                result.items.append(self.items[i])
        return result


a: StrArray = StrArray(["Armando", "Pete", "Leaky"])
b: StrArray = StrArray(["Bacot", "Nance", "Black"])
print(a)
print(a + "!")
print(a)
print(a + b)
print(b + ", " + a + "!!!")
