#importing the random library for the computer to use to play against the player
import random
#generating random seed
random.seed(2357864)

class connect_x_board():


    def __init__(self,size,show_win_cond = False):
        self.size = size
        self.show_win_cond = show_win_cond

    
