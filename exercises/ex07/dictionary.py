"""First program for ex07."""
__author__: str = "730470131"


def invert(input: dict[str, str]) -> dict[str, str]:
    """Invert a dictionary."""
    new_dict: dict[str, str] = dict()
    for i in input:
        new_dict[input[i]] = i
    return new_dict


def favorite_color(input: dict[str, str]) -> str:
    """Find the favorite color."""
    initial: dict[str, int] = dict()
    result: str = ""
    for colors in input:
        if result == "":
            result = input[colors]
        if not input[colors] in initial:
            initial[input[colors]] = 1
        else:
            initial[input[colors]] += 1
    for colors in initial:
        if initial[colors] > initial[result]:
            result = colors
    return result


def count(input: list[str]) -> dict[str, int]:
    """Count the number of times."""
    result: dict[str, int] = dict()
    i = 0
    for i in input:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    return result