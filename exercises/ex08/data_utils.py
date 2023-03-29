"""Dictionary related utility functions."""


__author__ = "730470131"


from csv import DictReader


# Define your functions below


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")
    # Prepare to read the data file 
    csv_reader = DictReader(file_handle)
    # Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)
    # Close the file when we're done, to free its resources.
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table: 
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(column: dict[str, list[str]], number: int) -> dict[str, list[str]]:
    """Produce a new column-based table with only the first N rows of data for each column."""
    result: dict[str, list[str]] = {}
    for item in column:
        n_values: list[str] = []
        i: int = 0
        while i < number and i < len(column[item]):
            if number != 0:
                n_values.append(column[item][i])
                i += 1
            else:
                i += 1
        result[item] = n_values
    return result


def select(input: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}
    for i in names:
        result[i] = input[i]
    return result


def concat(first: dict[str, list[str]], second: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column-based table with two column-based tables combined."""
    result: dict[str, list[str]] = {}
    for i in first:
        result[i] = first[i]
    for i in second:
        if i in result:
            for value in second[i]:
                result[i].append(value)
        else:
            result[i] = second[i]
    return result   


def count(input: list[str]) -> dict[str, int]:
    """Count the number of times."""
    result: dict[str, list[str]] = {}
    for item in input:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result