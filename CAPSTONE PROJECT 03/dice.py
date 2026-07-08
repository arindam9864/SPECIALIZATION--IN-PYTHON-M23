import random


def roll_dice():
    return random.randint(1, 6)

print("******** DICE ROLLING GAME ********")

while True:
    choice = input("\nPress 'r' to roll the dice or 'q' to quit: ").lower()

    if choice == "r":
        result = roll_dice()
        print("Dice shows:", result)

        if result == 1:
            print("You rolled the smallest number. Try again!")
        elif result == 2:
            print("A decent start. Keep rolling!")
        elif result == 3:
            print("Nice! You got three.")
        elif result == 4:
            print("Great! Four is a lucky number today.")
        elif result == 5:
            print("Awesome! You rolled a five.")
        else:
            print("Fantastic! You hit a SIX! Congratulations!")

    elif choice == "q":
        print("Game Over. Thanks for using the Dice Rolling Simulator!")
        break

    else:
        print("Invalid choice! Please enter 'r' to roll or 'q' to quit.")
