"""Check if code works."""

def reverse_string(a: str) -> str:
    result: str = ""
    i: int = len(a) - 1
    while i >= 0:
        result += a[i]
        i -= 1
    return result

reverse_string("happy")