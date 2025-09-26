import random

def play_game():
    number = random.randint(1, 100)
    attempts = 0

    print("Guess a number between 1 and 100!")

    while True:
        guess = input("Your guess: ")

        if not guess.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(guess)
        attempts += 1

        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed it in {attempts} attempts.")
            break

play_game()

