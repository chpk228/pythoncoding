import random
def play_game():
    word_list = ["python", "program", "game", "string", "computer"]
    word = random.choice(word_list)
    guessed_letters = []
    lives = 6
    while lives > 0:
        display_word = "".join([letter if letter in guessed_letters else "_" for letter in word])
        if "_" not in display_word:
            print("You won!")
            break
        print(f"Word: {display_word}")
        print(f"Lives: {lives}")
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        guessed_letters.append(guess)
        if guess not in word:
            lives -= 1
            print("Incorrect guess!")
    else:
        print("You lost!")
        print(f"The word was: {word}")
play_game()

