from random import randint

board = []
row = 6
col = 7
mineCount = 5
""" Use when done testing
row = int(input("# of rows: "))
col = int(input("# of columns: "))
mineCount = int(input("# of mines: "))
"""
answers = []

for x in range(0, row):
    board.append(["?"] * col)

def print_board(board):
    for row in board:
        print(" ".join(row))

print_board(board)

def rand_row(board):
    return randint(0, len(board) - 1)

def rand_col(board):
    return randint(0, len(board[0]) - 1)

for x in range(0,mineCount):
    mine_row = rand_row(board)
    mine_col = rand_col(board)
    answers.append({mine_col,mine_row})

def printAnswers():
    for answer in answers:
        print(answer)
printAnswers()

guess_row = int(input("Guess Row:"))
guess_col = int(input("Guess Col:"))

