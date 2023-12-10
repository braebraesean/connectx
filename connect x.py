#importing the random library for the computer to use to play against the player
import random
#generating random seed
random.seed(2357864)

#define the board class
class connect_x_board():
    
    #setting the innitial states
    def __init__(self,show_win_cond = False):
        self.show_win_cond = False
    
    #creates the game board
    def create_board(self):
        board = []
        #create rows
        for rows in range(0,self.size):
            board.append([(rows*self.size) + 1])
            #create cols
            for cols in range(1,(self.size)):
                board[rows].append(cols + (rows*self.size) + 1)
        #sends back finished board
        return(board)

    #sets the values that will determine if someone has won
    def win_condition_values(self):
        #to check in if a player wins, every time a player places their symbol in a row/col/diagonal
        #it will add(plaer1) or remove(player2) from the value or that row/col/diangonal
        #if the absolute value of a row/col/diagonal matches the length of the board,
        #we will know either player 1 or 2 has a line going acrossed the board
        #then we will check if the value of the r/c/d is negative(player 2 wins) or positive
        #(player 1 wins)
        #this func will make the the values or each row/col/diagonal and set them to a default of 0
        board_rows = []
        board_cols = []
        board_diagonals = [0,0]
        for rows in range(0,self.size):
            board_rows.append(0)
        for cols in range(0,self.size):
            board_cols.append(0)
        #compressing win condition skeleton so i can return it
    
        win_skeleton = [board_rows,board_cols,board_diagonals]
        return(win_skeleton)

    #workds like list.index() but for nested lists
    def find(self,data,value):
        #defines base location
        index = [0]
        #checks if for value through normal index
        try:
            index[0] = data.index(value)
            return(index)
            print("test")
        except:
            #checks for value through nested index
            for row in range(0,self.size):
                index[0] = row
                try:
                    index.append(data[row].index(value))
                    index = index[::-1]
                    return(index)
                except:
                    None
            return('False')

    #prints the board
    def print_board(self):
        board_str = ''
        #itterate through rows
        for row in range(0,self.size):
            #itterate through col
            for col in range(0,self.size):
                #print board with padding 
                print(f'{connectx.board[row][col]:<2}', end = "")
                #print borders

                if col != (len(connectx.board[row]) - 1):
                    print("|", end = "")
            print(board_str)

    #shows win condition if show_win_cond is set to true
    def DEBUG_FUNC_show_win_cond(self):
        if self.show_win_cond == True:
            # shows the values of each row/col/diagonal
            board_rows = self.win_cond[1]
            board_cols = self.win_cond[0]
            board_diagonals = self.win_cond[2]
            #prints the values
            print(board_diagonals[0], end = " ")
            for rows in range(0,self.size):
                print(board_rows[rows], end = " ")
            print()
            for cols in range(0,self.size):
                if  cols != self.size-1:
                    print(board_cols[cols])
                else:
                    print(board_cols[cols], end = "")
            print(f'{board_diagonals[1]:>{self.size * 2}}')

    #gets a int value
    def get_int(self,arg,arg2):
        getting_int = True
        while getting_int:
            try:
                get = int(input(arg))
                return(get)
            except:
                print(arg2)

    #edits the values of the rows/cols/diagonals
    def edit_win_cond(self,location,player):
        #setting the score to add depending on whos turn it is
        if player == 1:
            score = 1
        elif player != 1:
            score = -1
        #uncompressing win condition skeleton
        vb_rows = self.win_cond[0]
        vb_cols = self.win_cond[1]
        vb_diagonals = self.win_cond[2]

        #adding to the rows/col/diagonal values
        vb_cols[location[0]] += score
        vb_rows[location[1]] += score
        if location[0] == location[1] and (location[0] + location[1]) == self.size - 1:
            vb_diagonals[0] += score
            vb_diagonals[1] += score
        elif location[0] == location[1]:
            vb_diagonals[0] += score
        elif (location[0] + location[1]) == self.size - 1:
            vb_diagonals[1] += score

        #recompressing and setting new win cond values
        win_cond = [vb_rows,vb_cols,vb_diagonals]
        return(win_cond)

    #gets the position the computer wants to play with some ai
    def get_cp_pos(self):
        #sends back a random position if the player is not close to winning
        if self.find(self.win_cond,self.size-1) == 'False' and self.find(self.win_cond,1-self.size) == 'False':
            max_size = self.size ** 2
            return(random.randint(0,max_size))
        else:
            #if it detects the player is about to win in a row/col first we break down the win condition skeleton
            brows = self.win_cond[0]
            bcols = self.win_cond[1]
            bdiags = self.win_cond[2]
            #then we look for trys winning row/col/diagonal and assign it

            #if computer is about to win we assign for it to look for the win
            if self.find(self.win_cond,1-self.size) != 'False':
                brows = self.find(brows,1-self.size)
                bcols = self.find(bcols,1-self.size)
                bdiags = self.find(bdiags,1-self.size)
            #if player1 is about to win we assign it to blocck them
            else:
                brows = self.find(brows,self.size-1)
                bcols = self.find(bcols,self.size-1)
                bdiags = self.find(bdiags,self.size-1)
            #test and run through each of the rows/cols/diags for a valid move in a winning row/col/diag
            #checking rows
            if brows != 'False':
                win_row = brows[0]
                for col in range(0,self.size):
                    if self.board[win_row][col] != 'x' and self.board[win_row][col] != 'o':
                        return(self.board[win_row][col])
                
            #checking cols
            elif bcols != 'False':
                win_col = bcols[0]
                for row in range(0,self.size):
                    if self.board[row][win_col] != 'x' and self.board[row][win_col] != 'o':
                        return(self.board[row][win_col])
            #checking diagonals        
            elif bdiags != 'False':
                bdiags = bdiags[0]
                print(bdiags)
                #checkign downwards diagonal
                if bdiags == 0:
                    for diag in range(0,self.size):
                        if self.board[diag][diag] != 'x' and self.board[diag][diag] != 'o':
                            return(self.board[diag][diag])
                #checking upwards diagonal
                else:
                    for diag1 in range(0,self.size):
                        diag2 = (self.size-1) - diag1
                        if self.board[diag1][diag2] != 'x' and self.board[diag1][diag2] != 'o':
                            return(self.board[diag1][diag2])

            #sends back a random position if it doesnt find a smart move to play
            max_size = self.size ** 2
            return(random.randint(0,max_size))
            #board[row][col]

    #edits the board and win condition
    def edit_board(self, player):
        #making a loop to continue running this code until we succsesfully get a poition and edit the board
        edditing_board = True
        while edditing_board:

            #here we are going to get the location by asking the player if its player1's turn and asking the comptuer if its player2's turns
            if player == 1:
                position = self.get_int('Where would you like to go ? ','Please choose a valid location.')
            elif player != 1:
                position = self.get_cp_pos()
            #first we need to get the position we will be edditing
            location = self.find(self.board,position)
            if location != 'False':
                #board[location[1]][location[0]]
            
                #then we check to see that this spot is not already taken
                if (self.board[location[1]][location[0]] != 'x') and (self.board[location[1]][location[0]] != 'o'):
                    #set that we found a suitible spot
                    edditing_board = False
                    #then we will update the win_condition using that location
                    win_cond = self.edit_win_cond(location,player)
                    #then we will edit the board
                    if player == 1:
                        self.board[location[1]][location[0]] = 'x'
                    elif player != 1:
                        self.board[location[1]][location[0]] = 'o'
                        print(f'Where would you like to go computer ? {position}')
            else:
                if player == 1:
                    print('Please choose a valid location.')

    #checks if a player has won by checking the abs value of each row/col/diagonal and seeing if any match the length of the board
    def check_win(self):
        #see if any symbol goes from one side of the board to the other, and if so returns true
        if self.find(self.win_cond,self.size) != 'False':
            return(True)
        elif self.find(self.win_cond,(0 - self.size)) != 'False':
            return(True)
        else:
            return(False)

    #makes sure there is an availible move still
    def check_tie(self):
        #runs through every playable move, and returns false if it finds a valid move, else returns there is a tie if there are no playable moves
        for cell in range(0,(self.size ** 2)):
            if self.find(self.board,cell) != 'False':
                return(False)
        return(True)

    #runs the game
    def run_game(self):
        #set that the game is running
        running = True
        #sets base turn
        turn = 0
        while running:
            #increment turn
            turn += 1
            #sets which player
            if turn % 2 == 1:
                player = 1
            else:
                player = 2
            #prints board
            self.print_board()
            self.DEBUG_FUNC_show_win_cond()
            #runs the players turn
            self.edit_board(player)
            #checks for win
            if self.check_win():
                self.print_board()
                if player == 1:
                    print('Player 1 Wins!!!')
                else:
                    print('Computer WINS!!!')
                #stops game when someone wins
                running = False
            #if nobody has won, checks if there is a playable move, if there is not calls a tie
            elif self.check_tie():
                self.print_board()
                print("It's a tie!!")
                running = False

#creates the game obj
def create_game():
    game = connect_x_board()
    game.size = game.get_int('How large would you like the board? ','Please enter a valid number.')
    game.board = game.create_board()
    game.win_cond = game.win_condition_values()
    #asks if the player would like to see how the win codition skeleton is working
    if input('Show win condition skeleton? y/n? ') == 'y':
        game.show_win_cond = True
    return(game)


connectx = create_game()
connectx.run_game()
