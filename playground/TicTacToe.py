import os
os.system('clear')

class Board:
    def __init__(self):
        self.cells=[
        [" "," "," "]
        ,[" "," "," "]
        ,[" "," "," "]
    ]
        n=len(self.cells)
        self.row_container=[0]*n
        self.col_container=[0]*n
        self.diag_container=[0]*n
        self.antiDiag_container=[0]*n

    def display(self):
        for i,cell in enumerate(self.cells):
            print(*cell, sep='|')
            if i<len(self.cells)-1:
                print('-----')

    def update_cell(self,cell_num,player):
        if cell_num >= 10:
            raise Exception("Number not valid")
        r = (cell_num-1)//3
        c = (cell_num-1)%3
        if self.cells[r][c]==" ":
            self.cells[r][c] = player
            if self.is_winner(r,c):
                return True
            else:
                return None
        else:
            print("pick_another")

    def is_winner(self,r,c):
        size = len(self.cells[0])
        self.row_container[r]+=1
        self.col_container[c]+=1
        if r==c:
            self.diag_container[r]+=1
        if r+c==size:
            self.antiDiag_container[r]+=1
        return (
            self.row_container[r]== size or self.col_container[c] == size or sum(self.diag_container) == size or sum(self.antiDiag_container) == size
            )

def print_header():
    print("TicTacToeGame")

def screen_refresh(board):
    os.system("clear")
    print_header()
    board.display()

def main():
    board = Board()
    board.display()
    val1,val2 = False,False
    while True:
        screen_refresh(board)
        x_choice = int(input("\n X - Pls choose between 1-9: "))
        # update board
        val1 = board.update_cell(x_choice,'X')
        if val1:
            print('X is the winner')
            break
        # refresh screen
        screen_refresh(board)
        o_choice = int(input("\n O - Pls choose between 1-9: "))
        # update board
        val2 = board.update_cell(o_choice,'O')
        if val2:
            print('O is the winner')
            break

if __name__ == '__main__':
    main()
    