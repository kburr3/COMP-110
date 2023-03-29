"""EX04 - Lists(utils)."""
__author__: str = "730470131"


def all(input: list[int], one_number: int) -> bool: 
    """Checks if one_number is the same as input."""
    i: int = 0
    if len(input) == 0:        
        return False
    while i < len(input):
        if one_number == input[i]:
            i += 1
        else:
            return False
    return True


def max(input: list[int]) -> int: 
    """Finds the max number."""
    i: int = 0
    highest_number: int = input[0]
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    while i < len(input):
        if highest_number >= input[i]:
            i += 1
        elif highest_number < input[i]:
            highest_number: int = input[i]
            i += 1
    return highest_number


def is_equal(input_one: list[int], input_two: list[int]) -> bool: 
    """Checks if list_one is equal to list_two."""
    i: int = 0
    while len(input_one) != len(input_two):
        return False
    while i < len(input_one):
        if input_one[i] == input_two[i]:
            i += 1
        else: 
            return False
    return True