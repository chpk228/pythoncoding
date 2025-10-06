import os

board = [' ' for _ in range(9)]

def print_board():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(' 1 | 2 | 3 ')
    print('-----------')
    print(' 4 | 5 | 6 ')
    print('-----------')
    print(' 7 | 8 | 9 ')
    print()
    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2] + ' ')
    print('-----------')
    print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5] + ' ')
    print('-----------')
    print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8] + ' ')
    print()

def check_win(player):
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def check_tie():
    return ' ' not in board

def player_move(player):
    while True:
        try:
            choice = int(input(f"Player {player}, enter your move (1-9): "))
            if 1 <= choice <= 9:
                if board[choice - 1] == ' ':
                    board[choice - 1] = player
                    break
                else:
                    print("That space is already taken! Try again.")
            else:
                print("Invalid input. Please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def play_game():
    current_player = 'X'
    game_over = False

    while not game_over:
        print_board()
        player_move(current_player)

        if check_win(current_player):
            print_board()
            print(f"Player {current_player} wins! Congratulations!")
            game_over = True
        elif check_tie():
            print_board()
            print("It's a draw!")
            game_over = True
        
        if not game_over:
            current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    play_game()

```

