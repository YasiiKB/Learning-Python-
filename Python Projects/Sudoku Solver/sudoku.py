from pprint import pprint
############################################################
# OPTIONAL HELPER FUNCTIONS
############################################################

def find_next_empty(puzzle):
    # finds the next row, col on puzzle that's not filled yet --> we represent these with -1
    # returns a row, col tuple (or (None, None) if there is none)
    for r in range (9):
        for c in range (9): #range 0 is 0, 1, ..., 8
            if puzzle[r][c] == -1: # -1 means it's empty
                return r, c

    return None, None  # if there are no empty spaces

def is_valid(puzzle, guess, row, col):
    # figures out whether the guess at the row/col of the puzzle is a valid guess
    # returns True or False

    # for a guess to be valid, then we need to follow the sudoku rules
    # that number must not be repeated in the row, column, or 3x3 square that it appears in
    
    #checking the rows
    row_vals = puzzle[row]
    if guess in row_vals:
        return False # if we've repeated, then our guess is not valid!

    #checking the columns
        #making a list of the values in each column, b/c unlike rows, they columns aren't lists in the puzzle we made 
    # col_vals = []
    # for i in range(9):
    #     col_vals.append(puzzle[i][col])
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False 

    #cheking the 3x3 squares
        #get where the 3x3 square starts and iterate over the 3 values in the row/column
    row_start = (row // 3) * 3
    col_start = (col //3) * 3
    for r in range (row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess: 
                return False
    #if we passed all these test, and we haven't returned False yet, then the guess is correct
    return True
############################################################
# SOLVER IMPLEMENTATION
############################################################

def solve_sudoku(puzzle):
    # solve sudoku using backtracking!
    # our puzzle is a list of lists, where each inner list is a row in our sudoku puzzle
    # mutates the puzzle (lists) to be the solution (if it exists) 
    # return solution

    # step 1: choose somewhere on the puzzle to make a guess
    row, col = find_next_empty(puzzle)

    # step 1.1: if there's nowhere left, then we're done because we only allowed valid inputs
    if row is None:  # no need to check the column, b/c if None is passed to row, it is also passed to the column (in the find_next_empty function)
        return True

    # step 2: if there is a place to put a number, then make a guess between 1 and 9
    for guess in range(1, 10):
        # step 3: check if this is a valid guess
        if is_valid(puzzle, guess, row, col):
            # step 3.1: if this is a valid guess, then place it at that spot on the puzzle
            puzzle[row][col] = guess
            # step 4: then we recursively call our solver!
            if solve_sudoku(puzzle):
                return True
    # step 5: if not valid OR if our guess doesn't solve the puzzle, then we need to backtrack and try a new number
        puzzle[row][col] = -1 # reset
    # step 6: if none of the numbers that we try work, then this puzzle is UNSOLVABLE!!
    return False

if __name__ == '__main__':
    example_board = [
        [-1, -1, 7,   -1, -1, 9,   1, 8, -1],
        [9, -1, 5,   6, -1, 1,   -1, -1, -1],
        [-1, -1, -1,   4, -1, 7,   5, -1, -1],

        [-1, -1, -1,   -1, -1, 5,   -1, -1, 3],
        [5, 9, -1,   -1, -1, -1,   -1, 1, -1],
        [1, -1, -1,   -1, 3, -1,   2, -1, -1],

        [-1, 1, -1,   -1, 7, 6,   -1, -1, -1],
        [3, 7, -1,   -1, -1, -1,   -1, 2, -1],
        [-1, -1, -1,   9, -1, -1,   -1, -1, 1]
    ]
    print(solve_sudoku(example_board))
    pprint(example_board)