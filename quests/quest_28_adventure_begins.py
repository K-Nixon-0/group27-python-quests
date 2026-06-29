#!/usr/bin/python3
def forest():
    print("You are in a dark forest.They lead north and south.")
    choice = input("Which way do you chose to  go? (N/S): ")
    if choice == "N":
        cave()
    else:
        village()


def cave():
    print("You found a hidden cave with treasure!")
    print("You win!.")
    print("The END!")


def village():
    print("You landed into a village.")
    print("The villagers welcome you. If you decide to stay.")
    print("The END.")


forest()
