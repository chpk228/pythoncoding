
import random

def play_game():
    fruits = ['apple', 'banana', 'orange', 'strawberry', 'grape', 'pineapple', 'mango']
    word = random.choice(fruits)
    guesses = ''
    turns = 10

    print("Guess the fruit!")

    while turns > 0:
        failed = 0
        for char in word:
            if char in guesses:
                print(char, end=" ")
            else:
                print("_", end=" ")
                failed += 1
        print()

        if failed == 0:
            print("You won!")
            break

        guess = input("Guess a character: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guesses:
            print("You already guessed that letter.")
            continue

        guesses += guess

        if guess not in word:
            turns -= 1
            print("Wrong guess.")
            print(f"You have {turns} more guesses.")

        if turns == 0:
            print("You lost!")
            print(f"The word was: {word}")

if __name__ == "__main__":
    play_game()

