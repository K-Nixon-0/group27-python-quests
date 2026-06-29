#!/usr/bin/python3

secret_code = "42"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    guess = input("Guess the secret code: ")
    attempts += 1
    
    if guess == secret_code:
        print("Correct! You won!")
        break
    else:
        remaining = max_attempts - attempts
        print(f"Wrong! You have {remaining} attempts left.")
else:
    print("Game Over! The code was 42.")