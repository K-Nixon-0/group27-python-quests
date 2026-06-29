secret_number = 42
while True:
    guess = int(input("Guess the secret number: "))
    if guess == secret_number:
        print("Correct! You found the secret number!")
        break
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Too low! Try again.")

