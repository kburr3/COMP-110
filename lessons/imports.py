"""Examples of importing in Python."""


from lessons import helpers

# Alias a module / imported name as another name
from lessons import helpers as hp

# import names defined globally
from lessons.helpers import powerful


def main() -> None:
    """Entrypoint of program"""
    print(helpers.powerful(2,4))
    print(f"The answer: {hp.The_Answer}")


if __name__ == "__main__":
    main()