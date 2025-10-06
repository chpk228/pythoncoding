import random

def guess_the_number():
    """
    A simple number guessing game.
    The player has to guess a randomly generated number.
    """
    secret_number = random.randint(1, 100)
    attempts = 0
    
    print("Guess a number between 1 and 100.")
    
    while True:
        try:
            player_guess = int(input("Enter your guess: "))
            attempts += 1
            
            if player_guess < secret_number:
                print("Too low! Try again.")
            elif player_guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    guess_the_number()
```

