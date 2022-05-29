# import pandas as pd
from matplotlib.style import available
import numpy as np
import seaborn as sns; sns.set_theme()
import matplotlib.pyplot as plt
# rng = np.random.default_rng()

diag_matrix_lr = np.identity(4)
diag_matrix_rl = np.fliplr(np.identity(4))

def create_empty_grid() -> np.array:
    return np.zeros(shape=(6,7))


black_number = 1
red_number = 2

import sys

print(sys.path)

def get_black_grid(grid):
    return grid == black_number

def get_red_grid(grid:np.array):
    return grid == red_number

def get_color_grid(grid,color:str):
    if color == 'Black':
        return grid == black_number
    elif color == 'Red':
        return grid == red_number
    else:
        raise('Dumbass, that is not a valid color')



def is_horizontal_victory(color_grid):
    # Top to bottom, left to right search
    for row in range(6):
        for col in range(4):
            if sum(color_grid[row,col:(col+4)]) == 4:
                return True
    return False


def is_vertical_victory(color_grid):
    for row in range(3):
        for col in range(7):
            if sum(color_grid[row:(row+4),col]) == 4:
                return True
    return False


def is_diagonal_victory(color_grid:np.array):
    for row in range(3):
        for col in range(4):
            if  np.multiply(diag_matrix_lr,color_grid[row:(row+4),col:(col+4)]).sum() == 4 or np.multiply(diag_matrix_rl,color_grid[row:(row+4),col:(col+4)]).sum() == 4 :
                return True
    return False


def is_connect_four(color_grid:np.array):
    """Returns a grid that should only indicate one color"""

    if is_horizontal_victory(color_grid) or is_vertical_victory(color_grid) or is_diagonal_victory(color_grid):
        return True
    else:
        return False


def get_available_row_index(grid:np.array,column:int) -> int:
    for row in range(5,-1,-1):
        if grid[row,column] == 0:
            return row
    return None

def get_available_cols(grid):
    available_cols = []
    for col in range(7):
        if grid[0,col] == 0:
            available_cols.append(col)    
    return available_cols


class Player:

    def __init__(self) -> None:
        self.decision_maker = None
    
    def make_decision(self,grid:np.matrix) -> int:
        """Returns the column to play in."""
        col = np.random.choice(7)
        available_cols =  get_available_cols(grid)
        while col not in available_cols:
            col = np.random.choice(7)

        return col


class Game:

    def __init__(self,black_player=None,red_player=None):
        self.grid = None
        self.player_turn = 'Black'
        self.actions_dict = {'Black':[],'Red':[]}
        self.game_on = None
        self.black_player = black_player
        self.red_player = red_player


    def update_grid(self,row,col:int):
        """Place the appropriate row"""
        if self.player_turn == 'Black':
            checker_number = black_number
        else:
            checker_number = red_number

        
        self.grid[row,col] = checker_number


    def start_game(self):

        self.game_on = True
        self.grid = create_empty_grid()


    def play_turn(self,col:int):

        if col not in range(7):
            raise Exception('Not a valid column index')

        row = get_available_row_index(self.grid,col)

        if row is None:
            raise Exception('Dumbass. Bad Column input')

        self.update_grid(row,col)

        if self.player_turn == 'Black':
            self.actions_dict['Black'].append(col)
        elif self.player_turn == 'Red':
            self.actions_dict['Red'].append(col)

        reward = 0

        if is_connect_four(get_color_grid(self.grid,self.player_turn)):
            print(f'Hot damn. {self.player_turn} won.')
            self.game_on = False
            reward = 1 if self.player_turn == 'Black' else -1

        self.player_turn = "Red" if self.player_turn == 'Black' else "Black"

        return reward


    # def play_game(self):
    #     print("Begin!!\n")

    #     while True:
    #         print(f"It's {self.player_turn}'s turn:")
    #         print(self.grid)

    #         while True:
    #             col_choice = input('Select column choice as an integer from 1-7.')
    #             col_choice = int(col_choice)

    #             row_index = self.get_available_row_index(column=col_choice-1) 
    #             if row_index is None:
    #                 print(f'Sorry, column "{col_choice}" is not a valid column. Please choose again.')
    #             else:
    #                 self.update_grid(row_index,col_choice-1)
    #                 break

    #         if is_connect_four(get_color_grid(self.grid,self.player_turn)):
    #             print(f'Hot damn. {self.player_turn} won.')
    #             break


    #         self.player_turn = "Red" if self.player_turn == 'Black' else "Black"



    
if __name__ == '__main__':


    black = Player()
    red = Player()
    game = Game(black_player=black, red_player=red)
    game.start_game()
    print(game.grid)
    game_counts = 3

    rewards = []
    actions = []

    for i in range(game_counts):

        while game.game_on == True:
            

            if game.player_turn == "Black":
                col = black.make_decision(game.grid)
            else:
                col = red.make_decision(game.grid)
            
            reward =  game.play_turn(col)
            # plt.clf()
            # sns.heatmap(game.grid)
            # plt.show()
            print(game.grid)
            actions = game.actions_dict.copy()

        rewards.append(reward)





# game.play_game()



print('done')