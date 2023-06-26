import random

def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('-' * 9)

def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]

    return None

def is_board_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True

def get_player_move(board):
    while True:
        row = int(input("Enter the row (0-2): "))
        col = int(input("Enter the column (0-2): "))

        if board[row][col] == ' ':
            return row, col
        else:
            print("Invalid move. Try again.")

def get_computer_move(board):
    # Check for possible winning moves
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                board[row][col] = 'O'
                if check_winner(board) == 'O':
                    return row, col
                else:
                    board[row][col] = ' '

    # Check for possible blocking moves
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                board[row][col] = 'X'
                if check_winner(board) == 'X':
                    return row, col
                else:
                    board[row][col] = ' '

    # Choose a random move
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == ' ':
            return row, col

def play_game():
    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    current_player = 'X'

    while True:
        print_board(board)

        if current_player == 'X':
            row, col = get_player_move(board)
            board[row][col] = current_player
        else:
            print("Computer's turn...")
            row, col = get_computer_move(board)
            board[row][col] = current_player

        winner = check_winner(board)
        if winner:
            print_board(board)
            if winner == 'X':
                print("Congratulations! You win!")
            else:
                print("Sorry, the computer wins.")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

play_game()
