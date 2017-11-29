from minesweeper import Minesweeper


row = int(input("# of rows: "))
col = int(input("# of columns: "))
mine_count = int(input("# of mines: "))

m = Minesweeper(row, col, mine_count)

turn = 1
keepGoing = True

while keepGoing:
    print("\nTurn " + str(turn) + "--------------------------------------")
    m.print_board()
    # restrict guesses to be within board
    guess_row = int(input("\nGuess Row: "))
    while guess_row < 0 or guess_row > row - 1:
        guess_row = int(input("That's not even on the board! Guess Row: "))
    
    guess_col = int(input("Guess Col: "))
    while guess_col < 0 or guess_col > col - 1:
        guess_col = int(input("That's not even on the board! Guess Col: "))
    
    # if you guess directly on a mine's position
    if m.bts[guess_row][guess_col] == "X":
        print("\nGAME OVER\n")
        m.print_board(True)
        keepGoing = False
    else:
        m.search(guess_row, guess_col)
        if m.spaces_left == 0:
            print("\nCONGRATULATIONS! You win!\n")
            m.print_board(True)
            keepGoing = False

    turn += 1 
print("------------------GAME END------------------")
