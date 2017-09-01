from random import randint
class Minesweeper:
    
    def __init__(self, row, col, mine_count):
        self.row = row
        self.col = col
        self.mine_count = mine_count
        self.spaces_left = row * col - mine_count
        
        #creates board that is displayed to user
        self.board = [["?" for x in range(col)] for y in range(row)] 
        
        #creates behind the scenes grid: 0=unchecked coordinates, 1=checked coordinates, X=mines
        self.bts = [["0" for x in range(col)] for y in range(row)]
        
        #adding mines to bts
        for x in range(0, mine_count):
            self.mine_row = randint(0, row - 1)
            self.mine_col = randint(0, col - 1)
            self.bts[self.mine_row][self.mine_col] = "X"
    
        
    #prints board: entering True as the parameter reveals mines
    def print_board(self, reveal = False):
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if(self.bts[row][col]=='X' and reveal == True):
                    print(" ".join('X'), end=' ')
                else:
                    print(" ".join(self.board[row][col]), end=' ')
            print()
    
    #prints bts
    def print_bts(self):
        for row in range(len(self.bts)):
            for col in range(len(self.bts[row])):
                print(" ".join(self.bts[row][col]), end=' ')
            print()

    
    def is_mine(self, r, c):
        if self.bts[r][c]=="X":
            return True
        else:
            self.bts[r][c]="1"
            return False
    
    def within(self, r, c):
        if r < 0 or r > self.row - 1:
            return False
        if c < 0 or c > self.col - 1:
            return False
        return True
    
    def search(self, r, c):
        if not self.within(r, c): #if out of bounds
            #print(r, c, " is out of bounds")
            return
        
        if not self.board[r][c]=="?": #if already checked
            #print(r, c, " is not ?")
            return
        
        if self.is_mine(r, c): #if a mine
            #print(r, c, " is a mine")
            return
        
        self.spaces_left-=1
        if self.perim(r, c) > 0: #it is adjacent to at least one mine
            self.board[r][c] = str(self.perim(r, c))
            #print(r, c, " has an adjacent mine")
            return
        else:
            self.board[r][c] = "_"
            
            for (dr, dc) in [(r+1, c), (r-1, c), (r, c+1), (r, c-1), (r+1, c+1), (r-1, c+1), (r+1, c-1), (r-1, c-1)]:
                self.search(dr, dc)
            
    def perim(self, r, c):
        self.count = 0
        for (dr, dc) in [(r, c+1), (r, c-1), (r+1, c), (r-1, c), (r+1, c+1), (r+1, c-1), (r-1, c+1), (r-1, c-1)]:
            if self.within(dr, dc) and self.is_mine(dr, dc):
                self.count += 1
        return self.count
    