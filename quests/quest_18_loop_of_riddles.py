#!/usr/bin/python3

secret_number = 42
guess = None

while guess != secret_number:
    guess = int(input("Guess the secret number: "))
    
    if guess == secret_number:
        print("You got it right!")
    elif guess < secret_number:
        print("Too low, try again.")
    else:
        print("Too high, try again.")