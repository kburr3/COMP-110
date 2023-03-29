"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730470131"

five_character_word: str = input("Enter a 5-character word: ")
if len(five_character_word) < 5:
    print("Error: Word must contain 5 characters")
    exit()
if len(five_character_word) > 5:
    print("Error: Word must contain 5 characters")
    exit()
single_character_word: str = input("Enter a single character: ")
if len(single_character_word) > 1:
    print("Error: Character must be a single character.")
    exit()
if len(single_character_word) < 1:
    print("Error: Character must be a single character.")
    exit()
print("Searching for " + single_character_word + " in " + five_character_word)

number_of_times: int = 0

if single_character_word == five_character_word[0]:
    print(single_character_word + " found at index 0")
    number_of_times = number_of_times + 1
if single_character_word == five_character_word[1]:
    print(single_character_word + " found at index 1")
    number_of_times = number_of_times + 1
if single_character_word == five_character_word[2]:
    print(single_character_word + " found at index 2")
    number_of_times = number_of_times + 1
if single_character_word == five_character_word[3]:
    print(single_character_word + " found at index 3")
    number_of_times = number_of_times + 1
if single_character_word == five_character_word[4]:
    print(single_character_word + " found at index 4")
    number_of_times = number_of_times + 1

if int(number_of_times) > 1:
    print(str(number_of_times) + " instances of " + single_character_word + " found in " + five_character_word)
if int(number_of_times) == 1:
    print(str(number_of_times) + " instance of " + single_character_word + " found in " + five_character_word)
if int(number_of_times) == 0:
    print("No instances of " + single_character_word + " found in " + five_character_word)
