"""Choose Your Own Adventure Experience."""
__author__: str = "730470131"


from random import randint
NAMED_CONSTANT: str = "\U00002764"

points: int = 0
player: str = ""

def main() -> None:
    """The main function."""
    global points
    i = 1
    greet()
    while i > 0:
        experience_type: str = input("\nWhich opportunity do you choose: ")
        if int(experience_type) == 3:
            i = 0
        elif int(experience_type) == 1:
            points += smaller_points(points)
            print(f"Your score is now = {points}")
        elif int(experience_type) == 2:
            bigger_points()
            print(f"Your score is now = {points}")
        else:
            print("Not a valid number")
            print(f"Your score is still = {points}")
            i += 1
    print(f"Game Over! Your total adventure points was {points}! Play again soon! {NAMED_CONSTANT}")
    return


def smaller_points(points_one: int) -> int:
    """The function to earn up to 3 points."""
    points_one = 0
    print(f"{player}, in this option, you will have the ability to earn 3 adventure point by guessing a number between 1-3")
    print("You will still earn 1 adventure point for a wrong guess")
    correct_answer: int = randint(1, 3)
    guess: str = input("Enter a guess between 1-3: ")
    if correct_answer == int(guess):
        print("That is correct!")
        return (points_one + 3)
    else:
        print("That is incorrect!")
        return (points_one + 1)


def bigger_points() -> None:
    """The function to earn up to 5 points."""
    global points 
    print(f"{player}, in this option, you will have the ability to earn 5 adventure point by guessing a number between 1-5")
    print("You will still earn 1 adventure point for a wrong guess")
    correct_answer: int = randint(1, 5)
    guess: str = input("Enter a guess between 1-5: ")
    if correct_answer == int(guess):
        points += 5
        print("That is correct!")
    else:
        points += 1 
        print("That is incorrect!")


def greet() -> None:
    """Introduction to game!"""
    global player
    player = input("Hello there! Please Enter your name: ")
    print("Welcome to the guessing game!")
    print("In this game you will guess numbers to earn points!")
    print("The larger the guessing interval, the more points you earn!")
    print("Let's get started!")
    print("Type 1 to have an opportunity to earn 3 points")
    print("Type 2 to have an opportunity to earn 5 points")
    print("Type 3 to end the game!")


if __name__ == "__main__":
    main()