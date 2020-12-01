import copy
import random

class GameOfLife:
    def __init__(self,dimensions,total_generations):
        """Constructor for the GameOfLife
        This will instantiate the object required to generate the 
        Game Of Life board and corresponding items to initate the 
        playing sequence
        Args:
            dimensions (integer): NXN matrix size
            total_generations ([integer]): how long the generations happen
        """
        self.total_generations = total_generations
        self.rows = dimensions
        self.cols = dimensions
        self.grid = []

    def make_grid(self):
        """Makes the necessary grid required for us to start playing

        Returns:
            [NXN matrix]: only to be captured by py test for validation
        """
        self.grid = [[0] * self.rows for i in range(self.cols)]
        for i in range(self.rows):
            for j in range(self.cols):
                if i in ((self.rows//2)-1,self.rows//2,(self.rows//2)+1) and \
                    j in ((self.cols//2)-1,(self.cols//2)+1):
                    self.grid[i][j]=1
        return self.grid

    def show_grid(self):
        """A method thats called to periodically 
        keep printing step by step output
        """
        print(self.grid)
    
    def _count_neighbors(self,temp_board,x,y):
        """this is a helper function to determine 
        the neighboring count based on the current version
        on the board
        Args:
            temp_board (list): NXN matrix
            x (int): current row
            y (int): current column

        Returns:
            Integer: total count based on the neighbors associated
        """
        total_cnt = 0
        for i in range(-1,2):
            for j in range(-1,2):
                if (
                    (x + i < self.rows and x + i >= 0)
                    and (y + j < self.cols and y + j >= 0)
                ) and (temp_board[x + i][y + j]) == 1:
                    total_cnt+=1
        total_cnt-=temp_board[x][y]
        return total_cnt

    def update_grid(self):
        """
        Updates the grid for the iterations on the game of life based 
        on the neighboring structure.
        """
        # creating a copy of the board for reference
        temp_board = copy.deepcopy(self.grid)
        for i in range(self.rows):
            for j in range(self.cols):
                curr_state = temp_board[i][j]
                neighbors = self._count_neighbors(temp_board,i,j)
                if curr_state==0 and neighbors==3:
                    self.grid[i][j]=1
                # ideal for live cells
                elif curr_state == 1 and neighbors in [2, 3]:
                    self.grid[i][j]=1
                # death from stravation or overcrowding for any cell considered as living
                elif curr_state==1 and (neighbors>3 or neighbors<2):
                    self.grid[i][j]=0

    def play(self):
        """Orchestrator of the game of life
        """
        self.make_grid()
        print("initial grid")
        self.show_grid()
        for _ in range(self.total_generations):
            self.update_grid()
            self.show_grid()
        # final state for test
        print("final state")
        return self.grid # return here to display the last output to help test the functions

def main(dim,repeat):
    game_obj = GameOfLife(int(dim),int(repeat))
    return(game_obj.play())

if __name__ == "__main__":
    # assumption: we are considering this as an nxn problem with same rows and columns 
    # as per the question and instructions in document. 
    # We also assume that we are not considering the edges to 
    # contribute to a circular stream as it's been given as a continous input stream
    
    dim = input("Enter the NXN dimension: ") 
    repeat = input("Enter the number of times to repeat: ")
    print(main(dim,repeat))