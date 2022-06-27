import math
import time
from player import HumanPlayer, RandomComputerPlayer, SmartComputerPlayer

class TicTacToe():
    def __init__(self):
        self.board = [' ' for _ in range(9)] # A simple list to rep a 3x3 board
        self.current_winner = None # Keep track of the winner

    def print_board(self):
        #Getting the rows
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print ('| ' + ' | ' .join(row) + ' |')

    @staticmethod
    def print_board_nums():
        #What number corresponds to what box:  0| 1 | 2 etc
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print ('| ' + ' | ' .join(row) + ' |')


    def make_move(self, square, letter): # we need info about which square the player wants and what leter
        # if valid move, then make the move (assign square to letter)
        # then return true. if Invalid, return false
        if self.board[square] == ' ': #if the square is empty.
            self.board[square] = letter
            #after making a move, we need to check if someone won or not!
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # Winner if 3 in a row anywhere so we have to check rows, colums and diagonals
        #Checking the rows
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind + 1)*3]
        if all([spot == letter for spot in row]):
            return True

        #Checking the columns
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        #Check the diagonals
        # The only possible moves to win a diagonal are even squares 0, 2, 4 ,6
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]] #diagonal top left to bottom right
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]  #diagonal top right to bottom left
            if all([spot == letter for spot in diagonal2]):
                return True
        # if all these checks fail, we don't have a Winner
        return False

    def empty_squares(self):
        return ' ' in self.board  #a Boolean‌: each square is either empty or not.

    def num_empty_squares(self):
        #return len(self.available_moves())
        return self.board.count(' ')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot ==' ']
        #Works the same as the code below:
        # moves = [] #list of moves
        # for (i , spot) in enumerate(self.board):
        #     # ['x', 'x', 'o'] ---> [(0, 'x'), (1 , 'x'), (2, 'o')]
        #     if spot == ' ':
        #         moves.append[i]
        # return moves

def play(game, x_player, o_player, print_game=True):
    # returns the letter of the winner of the game! or None for a tie!
    if print_game: #if start the game, show the board
        game.print_board_nums()
    letter = 'X' #starating letter
    #iterate while the game still has empty squares
    while game.empty_squares():
        if letter =='O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

    #A function to make the move:
        if game.make_move(square, letter):
            if print_game:
                print('\n'+ letter + f' makes a move to square {square}')
                game.print_board() #we want to see the new board, after the move
                print('') #print an empty line
            #check if there is winner. If there is, we can end the game.
            if game.current_winner:
                if print_game:
                    print(letter +' wins!')
                return letter #return the winning letter, exit the loop and end the game

            #after the move, we need to alternate the letters
            letter = 'O' if letter =='X' else 'X' #switching player

        #tiny break, so the computer won't print out the next move immediately
        time.sleep(.8)

    if print_game:
        print('It\'s a tie!')

if __name__ == '__main__':
    x_player = SmartComputerPlayer('X')
    o_player = HumanPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)
