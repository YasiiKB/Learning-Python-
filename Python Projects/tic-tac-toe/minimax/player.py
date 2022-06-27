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
        square = random.choice(game.available_moves())
        return square


class SmartComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9: # if all squares are empty
            square = random.choice(game.available_moves()) # randonly choose one
        else:
            #get a square based on the minimax algorithm
            square = self.minimax(game, self.letter)['position']
        return square

    def minimax(self, state, player): #state is like a screenshot of the game that we pass in. It can be named anything.
        max_player = self.letter #yourself!
        other_player = 'O' if player == 'X' else 'X'

        #Checking if the previous move was a win
        #Base Case:
        if state.current_winner == other_player:
            # return position and the score in a dict because we need to keep track of those things for the algorithm to work
            return {'position': None, 'score': 1* (state.num_empty_squares() + 1) if other_player == max_player else -1* (state.num_empty_squares() + 1)}

        #no empty squres, it's a tie.
        #Position is None b/c we made no new moves.
        elif not state.empty_squares():
            return {'position': None, 'score': 0}

        # initialize a dictionary to record the best moves
        if player == max_player:
            best = {'position': None, 'score': -math.inf} #anything will be larger than -infinity
        else:
            best = {'position': None, 'score': math.inf}  # #anything will be smaller than +infinity

        for possible_move in state.available_moves():
            # step 1: make a move, try that spot
            state.make_move(possible_move, player)
            # step 2: use minimax to simulate the game after making that move
            sim_score = self.minimax(state, other_player)
            # step 3: undo the move
            state.board[possible_move] = ' '
            state.current_winner =  None
            sim_score['position'] = possible_move #return it to the previous position
            # step 4: update the best dictionaries
            if player == max_player:  #X is max player
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        return best
