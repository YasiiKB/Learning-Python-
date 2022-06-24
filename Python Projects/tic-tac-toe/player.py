import math
import random

class Player():
    def __init__(self, letter):
        #letter is either x or o
        self.letter = letter

    def get_move(self, game):
        pass

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        #While the HumanPlayer hasn't chosen a valid square, they can play.
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8):')
            # We're going to check that this is a correct input:
            try:
                val = int(square)
                #if the square isn't in the available moves, we'll also raise an error
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')
        return val

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        #get a random valid spot for the next move
        square = random.choice(game.available_moves())
        return square
