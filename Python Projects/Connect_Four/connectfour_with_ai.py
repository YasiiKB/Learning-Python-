from pickle import TRUE
import numpy as np
import pygame
from pygame import mixer
import sys
import math
import random

# Global variables (that won't change!)
BLUE = (0,0,255) #R,G,B
BLACK = (0,0,0)
RED = (250,0,0)
YELLOW = (250,250,0)

ROW_COUNT = 6
COLUMN_COUNT = 7

PLAYER = 0
AI = 1

PLAYER_PIECE = 1
AI_PIECE = 2

WINDOW_LENGTH = 4
EMPTY = 0

# Functions 

def create_board():
    board = np.zeros((ROW_COUNT,COLUMN_COUNT))
    return board

# in numpy (0,0) is on the top left corner, but we want (0,0) on the bottom left corner so the pieces will fill up from the bottom, so we need to flip the board!
def print_borad(board):
    print(np.flip(board, 0))

def drop_piece(board, row, col, piece):
    board[row][col] = piece 

def is_valid_location(board, col):
    # if the last row is not filled (==0), the location is valid
    return board[ROW_COUNT - 1][col] == 0

def get_next_open_row(board, col):
    for r in range (ROW_COUNT):
        # if the r in the column is 0, it is open!
        if board [r][col] == 0:
            return r

def winning_move(board, piece):
    # Check horizontaly for win
    for c in range(COLUMN_COUNT - 3): # last 3 columns can't work b/c it's connect FOUR.
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    # Check Vertically for win
    for r in range(ROW_COUNT - 3): # last 3 rows can't work b/c it's connect FOUR.
        for c in range(COLUMN_COUNT):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    # Check positively sloped diagonals for win
    for r in range(ROW_COUNT - 3):
        for c in range(COLUMN_COUNT - 3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    # Check negatively sloped diagonals for win for win
    for c in range(COLUMN_COUNT - 3): 
        for r in range(3, ROW_COUNT): # from row 3 to down
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True

def evaluate_window(window, piece):
    score = 0
    opp_piece = PLAYER_PIECE
    if piece == PLAYER_PIECE:
        opp_piece = AI_PIECE

    if window.count(piece) == 4:
        score += 100
    elif window.count(piece) == 3 and window.count(EMPTY) == 1: #if there are three pieces and there is an empty spot, it's good too.
        score += 5
    elif window.count(piece) == 2 and window.count(EMPTY) == 2:
        score += 2
    if window.count(opp_piece) == 3 and window.count(EMPTY) == 1:
        score -= 4
    
    return score

def score_position(board, piece):
    score = 0
    
    # Score Center column (for more winning opportunities)
    center_array = [int(i) for i in list(board[:,COLUMN_COUNT//2])] # taking all the rows, slicing columns from COLUMN_COUNT//2  
    center_count = center_array.count(piece)
    score += center_count * 3

    # Score Horizontal
    for r in range (ROW_COUNT):
        row_array = [int(i) for i in list(board[r,:])] # sliced the row from r, taking all the columns 
        for c in range (COLUMN_COUNT - 3):
            window = row_array[c:c+WINDOW_LENGTH]
            score += evaluate_window(window, piece)

    # Score Vertical 
    for c in range (COLUMN_COUNT):
        col_array = [int(i) for i in list(board[:,c])] #all the rows 
        for r in range (ROW_COUNT - 3):
            window = col_array[r:r+WINDOW_LENGTH]
            score += evaluate_window(window, piece)

    # Score positive sloped diagonal (Left to Right)
    for r in range(ROW_COUNT - 3): 
        for c in range (COLUMN_COUNT - 3):
            window = [board[r+i][c+i] for i in range (WINDOW_LENGTH)]
            score += evaluate_window(window, piece)

    # Score negative sloped diagonal (Right to Left)
    for r in range(ROW_COUNT - 3):
        for c in range (COLUMN_COUNT - 3):
            window = [board[r+3-i][c+i] for i in range (WINDOW_LENGTH)]
            score += evaluate_window(window, piece)

    return score
# Terminal_node for the Minimax function
def is_terminal_node(board):
    # ternimal_node is when one player wins or there are no empty spots left
    return winning_move(board, PLAYER_PIECE) or winning_move(board, AI_PIECE) or len(get_valid_locations(board)) == 0

# Based on the Pseudocode on Wikipedia 
# (Minimax) https://en.wikipedia.org/wiki/Minimax
# (Alpha–beta pruning) https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning
def minimax(board, depth, alpha, beta, maximizingPlayer):    # depth is how far into the future moves it will look
    valid_locations = get_valid_locations(board)
    is_ternimal = is_terminal_node(board)
    if depth == 0 or is_ternimal:
        if is_ternimal:
            if winning_move(board, AI_PIECE):
                return (None, 1000000000000) # None means no column value will be returned
            elif winning_move(board, PLAYER_PIECE):
                return (None, -1000000000000)
            else: # Game is over, no more valid moves 
                return (None, 0)
        else: # Depth is Zero
            return(None, score_position(board, AI_PIECE))

    if maximizingPlayer:
        value = -math.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = get_next_open_row(board, col)
            # make a copy of the board in a *differnet* memory location
            b_copy = board.copy()
            drop_piece(b_copy,row, col,AI_PIECE)
            new_score = minimax(b_copy, depth-1, alpha, beta, False)[1]#False because we're the maxizing player
            if new_score > value:
                value = new_score
                column = col
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return column, value

    else: #MinimizingPlayer 
        value = math.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = get_next_open_row(board, col)
            b_copy = board.copy()
            drop_piece(b_copy,row, col,PLAYER_PIECE)
            new_score = minimax(b_copy, depth-1, alpha, beta,TRUE)[1] #TRUE because we're minimizing player
            if new_score < value:
                value = new_score
                column = col 
            beta = min(beta, value)
            if alpha >= beta:
                break
        return column, value

# Getting a list of valid locations
def get_valid_locations(board):
    valid_locations =[]
    for col in range(COLUMN_COUNT):
        if is_valid_location(board, col):
            valid_locations.append(col)

    return valid_locations

def pick_best_move(board, piece):
    valid_locations = get_valid_locations(board)

    best_score = -1000
    best_col = random.choice(valid_locations)

    for col in valid_locations:
        row = get_next_open_row(board, col)
        temp_board = board.copy()
        drop_piece(temp_board, row, col, piece) 
        score = score_position(temp_board, piece)
        if score > best_score:
            best_score = score
            best_col = col
            
    return best_col

def draw_board(board):
    # background
    for c in range (COLUMN_COUNT):
        for r in range (ROW_COUNT): 
            # pygame.draw.rect(surface, color, rec (position, position, dimension, dimension, width(optional for border))
            pygame.draw.rect(screen, BLUE, (c*SQUARESIZE , r*SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)   
            
    # pieces
    for c in range (COLUMN_COUNT):
        for r in range (ROW_COUNT):
            if board[r][c] == PLAYER_PIECE: # PLAYER dropped a ball
                pygame.draw.circle(screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2), height - int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
            if board[r][c] == AI_PIECE: # AI dropped a ball
                pygame.draw.circle(screen, YELLOW, (int(c*SQUARESIZE+SQUARESIZE/2), height - int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
    
    pygame.display.update()


# Initialize the board and other stuff
board = create_board()
print_borad(board)
game_over = False
turn = random.randint(PLAYER, AI) # so it won't always be PLAYER's turn first.

# Graphics for the game, using pygame
pygame.init()

SQUARESIZE = 100
width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT + 1) * SQUARESIZE
size = (width, height)

RADIUS = int(SQUARESIZE/2 - 5)

screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()

myfont = pygame.font.SysFont('Monospace', 75)

# Sound
mixer.init()
balldrop= mixer.Sound("E:/Computer stuff - BUp/Python Projects/pyprojects/connectfour/balldrop.wav")
win= mixer.Sound("E:/Computer stuff - BUp/Python Projects/pyprojects/connectfour/win.wav")

while not game_over:
    
    # event is any input by the user, clicking, typying , etc.
    for event in pygame.event.get():
        
        # if something in typed, nothing happens (⚠ do it in all games)
        if event.type == pygame.QUIT:
            sys.exit()

        # creating the bar on the top that shows the piece before dropping it
        if event.type == pygame.MOUSEMOTION:
            # to clear out everything before moving the mouse each time
            pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
            posx = event.pos[0]
            if turn == PLAYER:
                pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE/2)), RADIUS)    
            
        pygame.display.update()
        
        # dropping the pieces
        if event.type == pygame.MOUSEBUTTONDOWN:
            # to clear out everything before clicking the mouse each time
            pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
            
            #print(event.pos) # gives a tuple of (x, y) positions in pixels
        
            # Ask for the Player's input
            if turn == PLAYER:
                posx = event.pos[0]
                col = int(math.floor((posx/ SQUARESIZE))) # converting pixels to squares 
                
                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, PLAYER_PIECE)
                    balldrop.play()

                    if winning_move(board, PLAYER_PIECE):
                        label = myfont.render('Player 1 Wins!', 1, RED)
                        screen.blit(label, (40, 10)) # updates the (40, 10) piosition of the screen
                        win.play()
                        game_over = True
                    
                    turn += 1
                    turn = turn % 2 # alternate between 0 and 1 

                    print_borad(board)
                    draw_board(board)

    # Ask for the AI's input, which is not dependent on MOUSEBOTTONDOWN so it should be out of that loop 
    if turn == AI and not game_over:
        
        # col  = pick_best_move(board, AI_PIECE)
        # need to initialize alpha = -infinity, beta = +infinity
        col, minimax_score = minimax(board, 5, -math.inf, math.inf, True) # the bigger the depth, the smater the moves will be but *it will also be slower* b/c it'll be checking a lot of branches of possible moves

        if is_valid_location(board, col):
            pygame.time.wait(500) # so the AI won't play too fast
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, AI_PIECE)
            balldrop.play()

            if winning_move(board, AI_PIECE):
                label = myfont.render('Player 2 Wins!', 1, YELLOW)
                screen.blit(label, (40, 10)) # updates the (40, 10) piosition of the screen
                win.play()
                game_over = True
            
            
            turn += 1
            turn = turn % 2 # alternate between 0 and 1 

            print_borad(board)
            draw_board(board)


    if game_over:
        pygame.time.wait(3000) # so it won't jump out of the game immediately