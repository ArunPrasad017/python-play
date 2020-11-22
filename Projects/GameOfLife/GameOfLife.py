import copy
import random
class GameOfLife:

    def __init__(self,r,c,total_generations):
        self.total_generations = total_generations
        self.rows = r
        self.cols = c

    def make_grid(self):
        # self.grid = [[0] * self.dimension for i in range(self.dimension)]
        # for i in range(self.rows):
        #     for j in range(self.cols):
        #         self.grid[i][j]=random.randint(0,1)
        self.grid = [[0,1,0], [0,0,1], [1,1,1], [0,0,0]]

    def show_grid(self):
        print(self.grid)
    
    def create_temp_grid(self):
        return [[0] * self.dimension for i in range(self.dimension)]
    
    def count_neighbors(self,temp_board,x,y):
        total_cnt = 0
        for i in (-1,2):
            for j in (-1,2):
                if(x+i!=self.rows and y+j!=self.cols):
                    total_cnt+=temp_board[x+i][y+j]
                elif(x==self.rows and y!=self.cols):
                    total_cnt+=temp_board[0][y+j]
                elif(x!=self.rows and y==self.cols):
                    total_cnt+=temp_board[x+i][0]
                else:
                    total_cnt+=temp_board[0][0]
        total_cnt-=temp_board[x][y]
        return total_cnt

    def update_grid(self):
        temp_board = copy.deepcopy(self.grid)
        for i in range(self.rows):
            for j in range(self.cols):
                curr_state = temp_board[i][j]
                neighbors = self.count_neighbors(temp_board,i,j)
                if curr_state==0 and neighbors==3:
                    self.grid[i][j]=1
                elif curr_state == 1 and neighbors in [2, 3]:
                    self.grid[i][j]=1
                # death from stravation or overcrowding for any cell considered as living
                elif curr_state==1 and (neighbors>3 or neighbors<2):
                    self.grid[i][j]=0

    # def play(self):
    #     generations = 0
    #     # while generations<self.total_generations:
    #     #     for i in range()
    #     update_grid

def main():
    X = GameOfLife(4,3,10)
    X.make_grid()
    X.show_grid()
    X.update_grid()
    X.show_grid()

if __name__ == "__main__":
    main()