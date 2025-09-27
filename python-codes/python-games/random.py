import random

number = random.randint(1, 100)
attempts = 0

while True:
    guess = input("Guess a number between 1 and 100: ")
    if not guess.isdigit():
        print("Enter a valid number.")
        continue
    guess = int(guess)
    attempts += 1
    if guess < number:
        print("Too low.")
    elif guess > number:
        print("Too high.")
    else:
        print(f"Correct! You guessed it in {attempts} tries.")
        break

