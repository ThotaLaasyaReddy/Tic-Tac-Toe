import time
# Tic-Tac-Toe Game in Python (Console Version)

def print_board(board):
    print(f"\n {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} \n")

def check_winner(board, player):
    # Check rows, columns and diagonals for a win
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def check_draw(board):
    return all([space != ' ' for space in board])

def play_game():
    board = [' '] * 9  # Empty board
    current_player = 'X'  # Player 'X' starts
    game_over = False
    print("\nWelcome to Tic-Tac-Toe Game\n")
    name = input("Enter your name: ")
    print("Hello " + name + "! Best of Luck!")
    print("The game is about to start!\nLet's play")
    time.sleep(2)
    print("Welcome to Tic-Tac-Toe!\n")
    print_board(board)

    while not game_over:
        try:
            move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1
            if board[move] != ' ':
                print("That space is already taken. Try again!")
                continue
        except (ValueError, IndexError):
            print("Invalid move. Please enter a number between 1 and 9.")
            continue

        board[move] = current_player
        print_board(board)

        # Check for winner
        if check_winner(board, current_player):
            print(f"Player {current_player} wins!")
            game_over = True
        elif check_draw(board):
            print("It's a draw!")
            game_over = True
        else:
            # Switch players
            current_player = 'O' if current_player == 'X' else 'X'

    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again == 'y':
        play_game()
    else:
        print("Thanks for playing!")

if __name__ == "__main__":
    play_game()
