"""EX02 - Wordle."""
__author__: str = "730470131"

secret_word: str = "python"
#The answer to the wordle is set above
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

guess: str = input(f"What is your {len(secret_word)}-letter guess? ")
while len(guess) != len(secret_word):
    guess: str = input(f"That was not {len(secret_word)} letters! Try again: ")

index_of_guess: int = 0
emoji_string: str = ""
while index_of_guess < len(secret_word):
    if guess[index_of_guess] == secret_word[index_of_guess]:
        emoji_string += GREEN_BOX
        index_of_guess += 1
    elif guess[index_of_guess] != secret_word[index_of_guess]:
        anywhere_else: bool = False
        alternative_index: int = 0
        while anywhere_else is not True and alternative_index < len(secret_word):
            if secret_word[alternative_index] == guess[index_of_guess]:
                anywhere_else: bool = True
                alternative_index += 1 
            else:
                alternative_index += 1 
        if anywhere_else is True:
            emoji_string += YELLOW_BOX
            index_of_guess += 1
        else:
            emoji_string += WHITE_BOX
            index_of_guess += 1

if guess == secret_word:
    print(emoji_string)
    print("Woo! You got it!")
else:
    print(emoji_string)
    print("Not quite. Play again soon!")