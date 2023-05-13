# You might need to install colorama module by running pip install colorama
from colorama import Fore, Style
import winsound

def print_board(board):
    print("-------------")
    for i in range(3):
        print("|", end=" ")
        for j in range(3):
            color = Fore.GREEN if board[i][j] == "X" else Fore.RED if board[i][j] == "O" else Fore.RESET
            print(color + board[i][j] + Style.RESET_ALL, "|", end=" ")
        print()
        print("-------------")

def play_sound(sound_file):
    winsound.PlaySound(sound_file, winsound.SND_ASYNC)

def check_win(board, player):
    for i in range(3):
        if board[i][0] == player and board[i][1] == player and board[i][2] == player:
            return True
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

def tic_tac_toe():
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    players = ["X", "O"]
    current_player = players[0]
    print_board(board)
    while True:
        print(Fore.YELLOW + "Player", current_player, "turn" + Style.RESET_ALL)
        row = int(input("Enter row number (0, 1, 2): "))
        col = int(input("Enter column number (0, 1, 2): "))
        if board[row][col] != " ":
            print(Fore.CYAN + "Invalid move, try again" + Style.RESET_ALL)
            continue
        board[row][col] = current_player
        play_sound("move_sound.wav")
        print_board(board)
        if check_win(board, current_player):
            play_sound("win_sound.wav")
            print(Fore.GREEN + "Player", current_player, "wins!" + Style.RESET_ALL)
            break
        if " " not in [item for sublist in board for item in sublist]:
            print(Fore.BLUE + "It's a tie!" + Style.RESET_ALL)
            break
        current_player = players[(players.index(current_player) + 1) % 2]

tic_tac_toe()
