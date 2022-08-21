import numpy as np
import pygame
from pygame import mixer
import sys
import math

# Global variables (that won't change!)
BLUE = (0,0,255) #R,G,B
BLACK = (0,0,0)
RED = (250,0,0)
YELLOW = (250,250,0)

ROW_COUNT = 6
COLUMN_COUNT = 7

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

def draw_board(board):
    for c in range (COLUMN_COUNT):
        for r in range (ROW_COUNT):
            # background 
            # pygame.draw.rect(surface, color, rec (position, position, dimension, dimension, width(optional for border))
            pygame.draw.rect(screen, BLUE, (c*SQUARESIZE , r*SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)   
            
            # pieces
    for c in range (COLUMN_COUNT):
        for r in range (ROW_COUNT):
            if board[r][c] == 1: # player 1 dropped a ball
                pygame.draw.circle(screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2), height - int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
            if board[r][c] == 2: # player 2 dropped a ball
                pygame.draw.circle(screen, YELLOW, (int(c*SQUARESIZE+SQUARESIZE/2), height - int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
    pygame.display.update()


# Initialize the board and other stuff
board = create_board()
print_borad(board)
game_over = False
turn = 0

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
            if turn == 0:
                pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE/2)), RADIUS)    
            else:
                pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE/2)), RADIUS)
        
        pygame.display.update()
        
        # dropping the pieces
        if event.type == pygame.MOUSEBUTTONDOWN:
            # to clear out everything before clicking the mouse each time
            pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
            
            #print(event.pos) # gives a tuple of (x, y) positions in pixels
        
            # Ask for Player 1 input
            if turn == 0:
                posx = event.pos[0]
                col = int(math.floor((posx/ SQUARESIZE))) # converting pixels to squares 
                
                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 1)
                    balldrop.play()

                    if winning_move(board, 1):
                        label = myfont.render('Player 1 Wins!', 1, RED)
                        screen.blit(label, (40, 10)) # updates the (40, 10) piosition of the screen
                        win.play()
                        game_over = True

            # Ask for Player 2 input
            else: # if turn is not 0
                posx = event.pos[0]
                col = int(math.floor((posx/ SQUARESIZE)))

                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 2)
                    balldrop.play()

                    if winning_move(board, 2):
                        label = myfont.render('Player 2 Wins!', 1, YELLOW)
                        screen.blit(label, (40, 10)) # updates the (40, 10) piosition of the screen
                        win.play()
                        game_over = True

            print_borad(board)
            draw_board(board)
            turn += 1
            turn = turn % 2 # alternate between 0 and 1 

            if game_over:
                pygame.time.wait(3000) # so it won't jump out of the game immediately