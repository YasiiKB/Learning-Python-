import pygame
import random

"""
10 x 20 square grid
shapes: S, Z, I, O, J, L, T
represented in order by 0 - 6
"""

pygame.font.init()
pygame.mixer.init()

# GLOBALS VARS
s_width = 800
s_height = 700
play_width = 300  # meaning 300 // 10 = 30 width per block
play_height = 600  # meaning 600 // 20 = 20 height per blo ck
block_size = 30

top_left_x = (s_width - play_width) // 2 # in the center
top_left_y = s_height - play_height


# SOUND EFFECTS
#file_location = ('E:\Computer stuff - BUp\Python Projects\pyprojects\Tetris').replace('\\','/')
file_location = ('G:\Tetris').replace('\\','/')
start = pygame.mixer.Sound(file_location + '/start.wav')
convertsound = pygame.mixer.Sound(file_location + '/convert.wav')
clearrow= pygame.mixer.Sound(file_location +'/clearrow.wav')
gameover = pygame.mixer.Sound(file_location +'/gameover.wav')
movepiece = pygame.mixer.Sound(file_location +'/move.wav')


# SHAPE FORMATS

S = [['.....',
      '.....',
      '..00.',
      '.00..',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]

Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]

I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]

O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]

J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]

L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]

T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]

shapes = [S, Z, I, O, J, L, T]
shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]
# index 0 - 6 represent shape


class Piece(object):
    rows = 20  # y
    columns = 10  # x

    def __init__(self, column, row, shape):
        self.x = column
        self.y = row
        self.shape = shape
        self.color = shape_colors[shapes.index(shape)]  #.index returns the position of the first occurrence of (shape)
        self.rotation = 0  # number from 0-3


def create_grid(locked_positions={}): #  locked positions is a dictionary like this: {(1,1):(255,0,0)}
    # Blank 10x20 Grid 
    grid = [[(0,0,0) for x in range(10)] for x in range(20)] # every column (10) in every row (20)

    # For locked positions
    for i in range(len(grid)): # column
        for j in range(len(grid[i])): # row
            if (j,i) in locked_positions: #y,x (colums, rows)
                c = locked_positions[(j,i)]
                grid[i][j] = c
    return grid


def convert_shape_format(shape):
    positions = []
    # get the current shape
    format = shape.shape[shape.rotation % len(shape.shape)] # a list of 0 and 1s because shape.rotation is 0 to 3 & len(shape.shape) is max 4.

    for i, line in enumerate(format): # enumerate adds a counter to an iterable and returns it in a form of enumerating object
        row = list(line)  # This enumerated object can then be converted into a list of tuples using the list() method.
        for j, column in enumerate(row):
            if column == '0': # if the shape exists, add it
                positions.append((shape.x + j, shape.y + i))

    for i, pos in enumerate(positions):
        positions[i] = (pos[0] - 2, pos[1] - 4) # deleting the .. dots in x direction and 4 dots in y direction

    return positions


def valid_space(shape, grid):
    # only add positions if the grig there is empty (if grid[i][j] == (0,0,0))
    accepted_positions = [[(j, i) for j in range(10) if grid[i][j] == (0,0,0)] for i in range(20)]
    # flatten the list (in only one dimention) for easier iteration : [(1,2)], [(3,4)] --> [(1,2), (3,4)]
    accepted_positions = [j for sub in accepted_positions for j in sub] # sub() function searches for the pattern in the string and replaces the matched strings with the replacement (repl)
    formatted = convert_shape_format(shape)
    
    # check if the position is accepeted
    for pos in formatted:
        if pos not in accepted_positions:
            if pos[1] > -1: # making sure the piece is on the screen first --> won't go off screen
                return False

    # if the position is acceptable
    return True


def check_lost(positions):
    for pos in positions:
        x, y = pos
        if y < 1: # there is no space left on y, we've hit the top 
            return True
    return False


def get_shape():
    global shapes, shape_colors
    # Piece (column, row, shape), top center --> column = 5, row = 0
    return Piece(5, 0, random.choice(shapes))


def draw_text_middle(text, size, color, surface):
    font = pygame.font.SysFont('comicsans', size, bold=True)
    label = font.render(text, 1, color)
    # put the text in the middle of the screen
    surface.blit(label, (top_left_x + play_width/2 - (label.get_width() / 2), top_left_y + play_height/2 - label.get_height()/2))


def draw_grid(surface, row, col):
    # shortening the variables for easier typing
    sx = top_left_x
    sy = top_left_y
    for i in range(row):
        # horizontal lines (grey: (128,128,128))
        pygame.draw.line(surface, (128,128,128), (sx, sy+ i*30), (sx + play_width, sy + i*30))  
        for j in range(col):
             # vertical lines
            pygame.draw.line(surface, (128,128,128), (sx + j*30, sy), (sx + j*30, sy + play_height)) 


def clear_rows(grid, locked):
    # delete the bottom row with no empty spots:
    inc = 0
    for i in range(len(grid)-1,-1,-1):
        row = grid[i] # loop through backwards, from the top (i), not 0
        if (0, 0, 0) not in row: # there are no white objects, it's all filled
            inc += 1
            # add positions to remove from locked
            ind = i
            for j in range(len(row)):
                try:
                    del locked[(j, i)]
                except:
                    continue
    # shift down the rows above the one we deleted & add an empty row to the top so the size of the grid won't change
    if inc > 0: # if we have deleted at least one row
        for key in sorted(list(locked), key=lambda x: x[1])[::-1]: # sort the list based on y value (from bottom up): [(0,1),(0,0)] --> [(0,0),(0,1)] 
            x, y = key # key is a tuple
            if y < ind: # if y is smaller than the row we deleted (we sorted it backwards, so rows above have a smaller row number), because we only need to shift the rows above
                newKey = (x, y + inc) # inc equals to the number rows we've deleted
                locked[newKey] = locked.pop(key)

                clearrow.play()

    return inc # inc equals to the number rows we've deleted (to calcualte the score later)

def draw_next_shape(shape, surface):
    font = pygame.font.SysFont('comicsans', 30)
    label = font.render('Next Shape', 1, (255,255,255)) # white

    sx = top_left_x + play_width + 50
    sy = top_left_y + play_height/2 - 100
    format = shape.shape[shape.rotation % len(shape.shape)]

    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0': # on the top of the window
                pygame.draw.rect(surface, shape.color, (sx + j*block_size, sy + i*block_size, block_size, block_size), 0)

    surface.blit(label, (sx + 10, sy- 30)) #surface.blit draws one image onto another

def update_score (nscore):
    score= max_score()
    
    with open ('score.txt', 'w') as f:
        if int(score) > nscore:
            f.write(str(score))
        else: 
            f.write(str(nscore))

def max_score():
    with open ('score.txt', 'r') as f:  # don't forget to write something in the file, otherwise there'll be no lines [0]
        lines = f.readlines()
        score = lines [0].strip()
    return score

def draw_window(surface, score, last_score = 0):
    surface.fill((0,0,0)) #black background
    # Tetris Title
    font = pygame.font.SysFont('comicsans', 50)
    label = font.render('TETRIS', 1, (255,255,255))

    surface.blit(label, (top_left_x + play_width / 2 - (label.get_width() / 2), 30))

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(surface, grid[i][j], (top_left_x + j* 30, top_left_y + i * 30, 30, 30), 0)
    
    # Current Score Display
    font = pygame.font.SysFont('comicsans', 30)
    label = font.render('Score: ' + str(score), 1, (255,255,255)) # white
    sx = top_left_x + play_width + 50
    sy = top_left_y + play_height/2 - 100
    surface.blit(label, (sx + 20, sy + 160))

    # High Score Display
    font = pygame.font.SysFont('comicsans', 30)
    label = font.render('High Score: ' + last_score, 1, (255,255,255)) # white
    sx = top_left_x - 250
    sy = top_left_y + 200
    surface.blit(label, (sx + 20, sy + 160))
    
    # draw grid
    draw_grid(surface, 20, 10)
    # draw the red rectangle 
    pygame.draw.rect(surface, (255, 0, 0), (top_left_x, top_left_y, play_width, play_height), 5)


def main():
    last_score = max_score()
    score = 0
    global grid

    locked_positions = {}  # (x,y):(255,0,0)
    grid = create_grid(locked_positions)

    change_piece = False
    run = True
    current_piece = get_shape()
    next_piece = get_shape()
    clock = pygame.time.Clock()  # create an object to help track time
    fall_time = 0

    while run:
        fall_speed = 0.27 #seconds

        grid = create_grid(locked_positions) # updates the grid with new 'locked positions'
        fall_time += clock.get_rawtime() # actual time, independent of the computer's speed
        clock.tick() # how many milliseconds have passed since the previous call/frame

        # PIECE FALLING CODE
        if fall_time/1000 >= fall_speed:  # milliseconds/1000 = seconds
            fall_time = 0
            current_piece.y += 1
            if not (valid_space(current_piece, grid)) and current_piece.y > 0:
                current_piece.y -= 1 # let's move back 1 and pretend moving never happened
                change_piece = True # we've hit the ground or another piece

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                # move piece to left
                if event.key == pygame.K_LEFT:
                    current_piece.x -= 1
                    if not valid_space(current_piece, grid):
                        current_piece.x += 1 # won't move the piece
                    movepiece.play()

                # move piece to right
                elif event.key == pygame.K_RIGHT:
                    current_piece.x += 1
                    if not valid_space(current_piece, grid):
                        current_piece.x -= 1 # won't move the piece
                    movepiece.play()

                # rotate shape with Space
                elif event.key == pygame.K_SPACE:
                    current_piece.rotation = current_piece.rotation + 1 % len(current_piece.shape)
                    if not valid_space(current_piece, grid):
                        current_piece.rotation = current_piece.rotation - 1 % len(current_piece.shape)
                    convertsound.play()
                # or K_Up
                elif event.key == pygame.K_UP:
                    current_piece.rotation = current_piece.rotation + 1 % len(current_piece.shape)
                    if not valid_space(current_piece, grid):
                        current_piece.rotation = current_piece.rotation - 1 % len(current_piece.shape)
                    convertsound.play()

                # move shape down
                if event.key == pygame.K_DOWN:
                    current_piece.y += 1
                    if not valid_space(current_piece, grid):
                        current_piece.y -= 1

        shape_pos = convert_shape_format(current_piece)

        # add piece to the grid for drawing
        for i in range(len(shape_pos)):
            x, y = shape_pos[i]
            if y > -1: # not above the screen
                grid[y][x] = current_piece.color

        # IF PIECE HIT GROUND
        if change_piece:
            for pos in shape_pos:
                p = (pos[0], pos[1])
                locked_positions[p] = current_piece.color
            current_piece = next_piece
            next_piece = get_shape()
            change_piece = False
            
            # Calculating the score
            score += clear_rows(grid, locked_positions) * 10 

        draw_window(win, score, last_score)
        draw_next_shape(next_piece, win)
        pygame.display.update()

        # Check if user lost
        if check_lost(locked_positions):
            gameover.play()
            run = False
            update_score (score)

    draw_text_middle("You Lost", 40, (255,255,255), win)
    pygame.display.update()
    pygame.time.delay(2000)


def main_menu():
    run = True
    while run:
        win.fill((0,0,0))
        draw_text_middle('Press any key to begin.', 60, (255, 255, 255), win)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                start.play()
                main()

    pygame.quit()

# the game's window
win = pygame.display.set_mode((s_width, s_height))
pygame.display.set_caption('Tetris')

main_menu()  # start game