"""
Name: Zachary Sika
Lab9.py
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def build_board():
    board = [1,2,3,4,5,6,7,8,9]
    character = ["x","o"]
    return board
def print_board(board):
    """ prints the values of board """
    RED = "\033[1;31m"
    BLUE = "\033[1;36m"
    LIGHT_GRAY = "\033[0;37m"
    reset = "\033[0m"
    new_board = []
    for v in board:
        new_board.append(v)
    for i in range(len(board)):
        if str(board[i]).find('x') >= 0:
            new_board[i] = RED + board[i] + LIGHT_GRAY
        elif str(board[i]).find('o') >= 0:
            new_board[i] = BLUE + board[i] + LIGHT_GRAY
    row_format = ' {0} | {1} | {2} '
    row_1 = row_format.format(new_board[0], new_board[1], new_board[2])
    row_2 = row_format.format(new_board[3], new_board[4], new_board[5])
    row_3 = row_format.format(new_board[6], new_board[7], new_board[8])
    row_separator = '-' * 11
    print(LIGHT_GRAY)
    print(row_1)
    print(row_separator)
    print(row_2)
    print(row_separator)
    print(row_3)
    print(reset)


def is_legal(board, position):
    if board[0:8] == "x":
        print("Position is taken, please choose another position")
    elif board[0:8] == "o":
        print("Position is taken, please choose another position")
    elif position > 9 or position < 1:
        print("Invalid position, please choose another position")
    else:
        return True
def fill_spot(board, position, character):
        if is_legal() == True:
            if position == 1:
                board.replace(0,character)
            elif position == 2:
                board.replace(1,character)
            elif position == 3:
                board.replace(2,character)
            elif position == 4:
                board.replace(3,character)
            elif position == 5:
                board.replace(4,character)
            elif position == 6:
                board.replace(5,character)
            elif position == 7:
                board.replace(6,character)
            elif position == 8:
                board.replace(8,character)
            elif position == 9:
                board.replace(8,character)


def winning_game(board):
    if board[0:2] == "x":
        return True
    elif board[3:5] == "x":
        return True
    elif board[6:8] == "x":
        return True
    elif board[0:2] == "o":
        return True
    elif board[3:5] == "o":
        return True
    elif board[6:8] == "o":
        return True
    else:
        return False

def game_over(board):
    if board[0:8] == 'x' or 'o':
        print("game is over")


def get_winner(board):
    if winning_game(board) == True:
        if board[0:2] == "x":
            return "x"
        elif board[3:5] == "x":
            return "x"
        elif board[6:8] == "x":
            return "x"
        if board[0:2] == "o":
            return "o"
        elif board[3:5] == "o":
            return "o"
        elif board[6:8] == "o":
            return "o"
        else:
            return "None"

def play(board):
    while winning_game(board) == True:
        position = input("Where would you like to place your mark?")
        
        for i in range(board):
            if winning_game(board) == True:
                print((get_winner(board),"'s win!"))
            else:
                print("Tie!")
def main():
    board = build_board()
   # position = build_board()
   # character = build_board()
   # build_board()
    print_board(board)
   # is_legal(board, position)
   # fill_spot(board, position, character)
   # winning_game(board)
   # game_over(board)
   # get_winner(board)
   # play(board)

main()


if __name__ == '__main__':
    main()
