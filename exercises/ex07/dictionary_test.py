"""Second program (test program) for ex07."""
__author__: str = "730470131"


from dictionary import invert
from dictionary import favorite_color
from dictionary import count


def test_invert_works() -> None:
    """Check for invert."""
    input: dict[str, str] = {"Keegan": "Burr", "Michael": "Jordan", "Lebron": "James"}
    assert invert(input) == {"Burr": "Keegan", "Jordan": "Michael", "James": "Lebron"}


def test_invert_empty() -> None:
    """Check for an empty list."""
    input: dict[str, str] = {}
    assert invert(input) == {}


def test_invert_runs() -> None:
    """Check for invert."""
    input: dict[str, str] = {"Ciaran": "Burr", "Michael": "Jackson", "Will": "James"}
    assert invert(input) == {"Burr": "Ciaran", "Jackson": "Michael", "James": "Will"}


def test_favorite_color() -> None:
    """Check the favorite color."""
    input: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(input) == "blue"


def test_favorite_color_empty() -> None:
    """Check for empty list."""
    input: dict[str, str] = {}
    assert favorite_color(input) == ""


def test_favorite_color_more_colors() -> None:
    """Check favorite color still looks for more colors."""
    input: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue", "Keegan": "yellow", "Marcus": "green", "Victor": "green"}
    assert favorite_color(input) == "yellow"


def test_count_empty() -> None:
    """Check for empty list."""
    input: list[str] = list()
    assert count(input) == {}


def test_count_works() -> None:
    """Check if this works."""
    input: list[str] = ["Keegan", "Jordan", "Burr", "Michael", "Ciaran", "Burr", "Aidan", "Burr"]
    assert count(input) == {"Keegan": 1, "Jordan": 1, "Burr": 3, "Michael": 1, "Ciaran": 1, "Aidan": 1}


def test_count_single_variables() -> None:
    """Check if this works."""
    input: list[str] = ["Keegan", "Jordan", "Burr", "Michael"]
    assert count(input) == {"Keegan": 1, "Jordan": 1, "Burr": 1, "Michael": 1}