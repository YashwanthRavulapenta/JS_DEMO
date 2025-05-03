import os

# Terminal Colors
RED = '\033[91m'      # X color
BLUE = '\033[94m'     # O color
GRAY = '\033[90m'
WHITEBG = '\033[47m'  # White background
RESET = '\033[0m'
BOLD = '\033[1m'

# 3x3 Board
board = [' ' for _ in range(9)]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def format_cell(value, idx):
    if value == 'X':
        return WHITEBG + RED + BOLD + f' {value} ' + RESET
    elif value == 'O':
        return WHITEBG + BLUE + BOLD + f' {value} ' + RESET
    else:
        return GRAY + f' {idx} ' + RESET

def print_board():
    print()
    for i in range(3):
        print('|'.join(format_cell(board[3*i+j], 3*i+j) for j in range(3)))
        if i < 2:
            print(GRAY + "---+---+---" + RESET)
    print()

def check_winner(player):
    win_combinations = [
        [0,1,2], [3,4,5], [6,7,8], # Rows
        [0,3,6], [1,4,7], [2,5,8], # Columns
        [0,4,8], [2,4,6]           # Diagonals
    ]
    for line in win_combinations:
        if all(board[pos] == player for pos in line):
            return True
    return False

def is_draw():
    return ' ' not in board

def player_move(player_symbol):
    while True:
        try:
            move = int(input(f"{player_symbol}'s turn. Enter position (0-8): "))
            if 0 <= move <= 8 and board[move] == ' ':
                board[move] = player_symbol
                break
            else:
                print(RED + "Invalid move! Try again." + RESET)
        except ValueError:
            print(RED + "Please enter a number between 0 and 8." + RESET)

# MAIN GAME
clear_screen()
print(RED + BOLD + "Welcome to 3x3 Tic Tac Toe (Player vs Player)!" + RESET)
print_board()

current_player = 'X'

while True:
    player_move(current_player)
    clear_screen()
    print_board()

    if check_winner(current_player):
        print(BOLD + f"\nPlayer {current_player} wins! 🎉" + RESET)
        break
    if is_draw():
        print(BOLD + "\nIt's a draw! 🤝" + RESET)
        break

    # Switch player
    current_player = 'O' if current_player == 'X' else 'X'
