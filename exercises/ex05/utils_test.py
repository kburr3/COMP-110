"""Second program (test program) for ex05."""
__author__: str = "730470131"


from utils import only_evens
from utils import sub
from utils import concat


def test_only_evens_empty() -> None:
    """Check for an empty list."""
    input: list[int] = []
    assert only_evens(input) == []


def test_only_evens_not_empty() -> None:
    """Check for an empty list."""
    input: list[int] = [1, 2]
    assert len(only_evens(input)) > 0


def test_only_evens_evens() -> None:
    """Check if evens work."""
    input: list[int] = [2, 4, 6]
    assert only_evens(input)


def test_only_evens_odds() -> None:
    """Check if odds work."""
    input: list[int] = [1, 2, 3, 5]
    assert only_evens(input)


def test_concat_list_empty() -> None:
    """Check for empty list."""
    input_one: list[int] = []
    input_two: list[int] = []
    assert concat(input_one, input_two) == []


def test_concat_append_correct() -> None:
    """Check if list appended right."""
    input_one: list[int] = [1, 2]
    input_two: list[int] = [3, 4]
    assert concat(input_one, input_two) == [1, 2, 3, 4]


def test_concat_append_negatives() -> None:
    """Check if list appended negatives."""
    input_one: list[int] = [-1, 2]
    input_two: list[int] = [-2, 5]
    assert concat(input_one, input_two) == [-1, 2, -2, 5]


def test_sub_list() -> None:
    """Creating a new list of numbers."""
    input: list[int] = [1, 2, 3, 4]
    start_index: int = 0
    end_index: int = 3
    assert sub(input, start_index, end_index) == [1, 2, 3]


def test_sub_long() -> None:
    """Testing longer list."""
    input: list[int] = [1, 2, 3, 4, 5, 6, 7, 8]
    start_index: int = 3
    end_index: int = 5
    assert sub(input, start_index, end_index) == [4, 5]


def test_sub_one_index() -> None:
    """Checking to see if one index works."""
    input: list[int] = [1, 2, 3, 4, 5, 6]
    start_index: int = 4
    end_index: int = 5
    assert sub(input, start_index, end_index) == [5]


def test_sub_same_index() -> None:
    """Checking to see if same index works."""
    input: list[int] = [1, 2, 3, 4]
    start_index: int = 2
    end_index: int = 2
    assert sub(input, start_index, end_index) == []


def test_sub_negative_start() -> None:
    """Checking negative start index."""
    input: list[int] = [1, 2, 3, 4]
    start_index: int = -2
    end_index: int = 2
    assert sub(input, start_index, end_index) == [1, 2]


def test_sub_greater_index() -> None:
    """Checking when end index is greater than length."""
    input: list[int] = [1, 2, 3, 4]
    start_index: int = 1
    end_index: int = 7
    assert sub(input, start_index, end_index) == [2, 3, 4]


def test_sub_length_none() -> None:
    """Checking if length of list is 0."""
    input: list[int] = []
    start_index: int = 1
    end_index: int = 3
    assert sub(input, start_index, end_index) == []