#importing the random library for the computer to use to play against the player
import random
#generating random seed
random.seed(2357864)
#MOAR RANDOM (which in hindsight does'nt actually make it MOAR RANDOM but im leaving in anyways
for times in range(0,random.randint(0,50)):
    random.seed(random.randint(0,500))

def __find(self, value): #moved over to class
    #defines base location
    index = [0]
    #checks if for value through normal index
    try:
        index[0] = self.index(value)
        return(index)
        print("test")
    except:
        #checks for value through nested index
        for row in range(0,len(self)):
            index[0] = row
            if type(self[row]) == list:
                try:
                    index.append(self[row].index(value))
                    index = index[::-1]
                    return(index)
                except:
                    None
        return('False')
# wanted to add method to list obj, but py does not support adding methods
# to py objs list.find = find

def create_board_of_size(size): #moved over to class
    board = []
    #create rows
    for rows in range(0,size):
        board.append([(rows*size) + 1])
        #create cols
        for cols in range(1,(size)):
            board[rows].append(cols + (rows*size) + 1)
    #sends back finished board
    return(board)

def print_board(board): #moved over to class
    #itterate through rows
    for row in range(0,len(board)):
        #itterate through col
        for col in range(0,len(board[row])):
            #print board with padding 
            print(f'{board[row][col]:<2}', end = "")
            #print borders
            if col != (len(board[row]) - 1):
                print("|", end = "")
        print()

def win_condition_values(size): #moved over to class
    #to check in if a player wins, every time a player places their symbol in a row/col/diagonal
    #it will add(plaer1) or remove(player2) from the value or that row/col/diangonal
    #if the absolute value of a row/col/diagonal exceeds the length of the board,
    #we will know someone has a line goign acrossed the board
    #then we will check if the value of the r/c/d is negative(player 2 wins) or positive
    #(player 1 wins)
    #this func will make the skeleton of the values or each row/col/diagonal
    board_rows = []
    board_cols = []
    board_diagonals = [0,0]
    for rows in range(0,size):
        board_rows.append(0)
    for cols in range(0,size):
        board_cols.append(0)
    #compressing win condition skeleton so i can return it
    
    win_skeleton = [board_rows,board_cols,board_diagonals]
    return(win_skeleton)

def DEBUG_FUNC_show_win_cond(win_skeleton,size): #moved over to class
    # shows the values of each row/col/diagonal
    # dia 1 row 1-size
    # col 1-9(\n) dia 2
    board_rows = win_skeleton[1]
    board_cols = win_skeleton[0]
    #flip for looks and debugging
    board_rows = board_rows#[::-1]
    board_cols = board_cols#[::-1]
    board_diagonals = win_skeleton[2]
    print(board_diagonals[0], end = " ")
    for rows in range(0,size):
        print(board_rows[rows], end = " ")
    print()
    for cols in range(0,size):
        if  cols != size-1:
            print(board_cols[cols])
        else:
            print(board_cols[cols], end = "")
    print(f'{board_diagonals[1]:>{size * 2}}')

def __edit_win_cond(location, player,win_cond, size): #moved over to class
    #setting the score to add depending on whos turn it is
    if player == 1:
        score = 1
    elif player != 1:
        score = -1
    #uncompressing win condition skeleton
    vb_rows = win_cond[0]
    vb_cols = win_cond[1]
    vb_diagonals = win_cond[2]

    #adding to the rows/col/diagonal values
    vb_cols[location[0]] += score
    vb_rows[location[1]] += score
    if location[0] == location[1] and (location[0] + location[1]) == size - 1:
        vb_diagonals[0] += score
        vb_diagonals[1] += score
    elif location[0] == location[1]:
        vb_diagonals[0] += score
    elif (location[0] + location[1]) == size - 1:
        vb_diagonals[1] += score

    #recompressing and setting new win cond values
    win_cond = [vb_rows,vb_cols,vb_diagonals]
    return(win_cond)

def get_int(arg,arg2): #moved over to class
    getting_int = True
    while getting_int:
        try:
            get = int(input(arg))
            return(get)
        except:
            print(arg2)

def __get_cp_pos(size,win_cond,board): #moved over to class

    #sends back a random position if the player is not close to winning
    if __find(win_cond,size-1) == 'False' and __find(win_cond,1-size) == 'False':
        max_size = size ** 2
        return(random.randint(0,max_size))
    else:
        #if it detects the player is about to win in a row/col first we break down the win condition skeleton
        brows = win_cond[0]
        bcols = win_cond[1]
        bdiags = win_cond[2]
        #then we look for this winning row/col/diagonal and assign it

        #if computer is about to wi nwe assign for it to look for the win
        if __find(win_cond,1-size) != 'False':
            brows = __find(brows,1-size)
            bcols = __find(bcols,1-size)
            bdiags = __find(bdiags,1-size)
        #if player1 is about to win we assign it to blocck them
        else:
            brows = __find(brows,size-1)
            bcols = __find(bcols,size-1)
            bdiags = __find(bdiags,size-1)
        #test and run through each of the rows/cols/diags for a valid move in a winning row/col/diag
        #checking rows
        if brows != 'False':
            win_row = brows[0]
            for col in range(0,size):
                if board[win_row][col] != 'x' and board[win_row][col] != 'o':
                    return(board[win_row][col])
            
        #checking cols
        elif bcols != 'False':
            win_col = bcols[0]
            for row in range(0,size):
                if board[row][win_col] != 'x' and board[row][win_col] != 'o':
                    return(board[row][win_col])
        #checking diagonals        
        elif bdiags != 'False':
            bdiags = bdiags[0]
            print(bdiags)
            #checkign downwards diagonal
            if bdiags == 0:
                for diag in range(0,size):
                    if board[diag][diag] != 'x' and board[diag][diag] != 'o':
                        return(board[diag][diag])
            #checking upwards diagonal
            else:
                for diag1 in range(0,size):
                    diag2 = (size-1) - diag1
                    if board[diag1][diag2] != 'x' and board[diag1][diag2] != 'o':
                        return(board[diag1][diag2])

        #sends back a random position if it doesnt find a smart move to play
        max_size = size ** 2
        return(random.randint(0,max_size))
        #board[row][col]


def edit_board(board, player, size, win_cond): # moved over to class
    edditing_board = True
    while edditing_board:

        #here we are going to get the location by asking the player if its player1's turn and asking the comptuer if its player2's turns
        if player == 1:
            position = get_int('Where would you like to go ? ','Please choose a valid location.')
        elif player != 1:
            position = __get_cp_pos(size,win_cond,board)
        #first we need to get the position we will be edditing
        location = __find(board,position)
        if location != 'False':
            #board[location[1]][location[0]]
            
            #then we check to see that this spot is not already taken
            if (board[location[1]][location[0]] != 'x') and (board[location[1]][location[0]] != 'o'):
                #set that we found a suitible spot
                edditing_board = False
                #then we will update the win_condition using that location
                win_cond = __edit_win_cond(location, player, win_cond, size)
                #then we will edit the board
                if player == 1:
                    board[location[1]][location[0]] = 'x'
                elif player != 1:
                    board[location[1]][location[0]] = 'o'
                    print(f'Where would you like to go computer ? {position}')
        else:
            if player == 1:
                print('Please choose a valid location.')
            
def check_win(win_cond, size): #moved to class
    #see if any symbol goes from one side of the board to the other, and if so returns true
    if __find(win_cond,size) != 'False':
        return(True)
    elif __find(win_cond,(0 -size)) != 'False':
        return(True)
    else:
        return(False)

def check_tie(board,size): #moved to class
    #runs through every playable move, and returns false if it finds a valid move, else returns there is a tie if there are no playable moves
    for cell in range(0,(size * size)):
        if __find(board,cell) != 'False':
            return(False)
    return(True)
        
def run_game(size,board,win_cond,show_win_cond):
    #get board size       
    size = get_int('How large would you like the board? ','Please enter a valid number.')
    #genereate board
    board = create_board_of_size(size)
    #generate win condition skeleton
    win_cond = win_condition_values(size)
    #set that the game is running
    running = True
    #sets base turn
    turn = 0
    while running:
        #increment turn every condition
        turn += 1
        #check witch player
        if turn % 2 == 1:
            player = 1
        else:
            player = 2
        #print board
        print_board(board)
        #uncomment this if you want to see how the inner magnations of my mind are an inigma \/
        if show_win_cond == True:
            DEBUG_FUNC_show_win_cond(win_cond,size)
        #runs the players turn
        edit_board(board,player,size,win_cond)
        #checks for win
        if check_win(win_cond,size):
            print_board(board)
            print(f'Player {player} Wins!!!')
            #stops game when someone wins
            running = False
        #if nobody has won, checks if there is a playable move, if there is not calls a tie
        elif check_tie(board,size):
            print_board(board)
            print("It's a tie!!")
            print_board(board)
            running = False






show_win_cond = False
playing = True
while playing:
    #defines these 3 in the global scope, so all functions can edit them
    size = 0
    board = []
    win_cond = []
    #asks if the player would like to see how the win codition skeleton is working
    if input('Show win condition skeleton? y/n? ') == 'y':
        show_win_cond = True
    run_game(size,board,win_cond,show_win_cond)
    #asks if the player wants to play again
    exit_game = input('Play again? y/n ')
    if exit_game != 'y':
        playing = False

