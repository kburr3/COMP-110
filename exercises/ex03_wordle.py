"""EX03 - Wordle part three."""
__author__: str = "730470131"


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(given_word: str, single_characer: str) -> bool:
    """Searching for character in word."""
    assert len(single_characer) == 1
    i = 0 
    while i < len(given_word):
        if single_characer == given_word[i]:
            return True
        else:
            i += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Coding the Colors."""
    assert len(guess) == len(secret)
    emoji_string: str = ""
    i: int = 0
    while i < len(secret):
        if guess[i] == secret[i]:
            emoji_string += GREEN_BOX
            i += 1
        elif contains_char(secret, guess[i]) is True:
            emoji_string += YELLOW_BOX
            i += 1
        elif contains_char(secret, guess[i]) is False:
            emoji_string += WHITE_BOX
            i += 1
    return emoji_string


def input_guess(expected_length: int) -> str:
    """Expected length of guess."""
    user_guess: str = input(f"Enter a {expected_length} character word: ") 
    while len(user_guess) != expected_length:
        user_guess: str = input(f"That wasn't {expected_length} chars! Try again: ")
    return user_guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    current_turn: int = 1
    correct_word: str = "codes"
    while current_turn < 7:
        print(f"=== Turn {current_turn}/6 ===")
        main_guess: str = input_guess(len(correct_word))
        print(emojified(main_guess, correct_word))
        if main_guess == correct_word:
            print(f"You won in {current_turn}/6 turns!")
            return
        else:
            current_turn += 1
    print("X/6 - Sorry, try again tomorrow!")
    return


if __name__ == "__main__":
    main()
"""Need this to be able to run as module."""