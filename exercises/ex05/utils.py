"""First program for ex05."""
__author__: str = "730470131"


def only_evens(input: list[int]) -> list:
    """Determine the evens in a list."""
    i: int = 0
    even_list: list[int] = []
    while i < len(input):
        if input[i] % 2 == 0:
            even_list.append(input[i])
            i += 1
        else:
            i += 1
    return even_list


def concat(input_one: list[int], input_two: list[int]) -> list:
    """Combine two lists of ints."""
    total_list: list[int] = input_one + input_two
    return total_list


def sub(input: list[int], start_index: int, end_index: int) -> list:
    """Find the list between two indexs, minus one."""
    new_list: list[int] = []
    while start_index < end_index:
        if start_index < 0:
            start_index = 0
        elif end_index > len(input):
            end_index = len(input)
        elif start_index > len(input):
            return new_list
        else:  
            new_list.append(input[start_index])
            start_index += 1        
    return new_list