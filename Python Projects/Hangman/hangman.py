import random
import json
import string
from hangman_visual import lives_visual_dict

# Make a python list of the words in the json file:
words = list()
f = open('words.json')
data = json.load(f)
for i in data['data']:
    words.append(i)

f.close()

# Pick a random word:
def get_valid_word(words):
    word = random.choice(words)
    #if there is a - or a space, keep choosing
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

#print(get_valid_word(words)) --> Randomly chooses and prints the word in uppercase.

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) #letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #a set of the letters the user has guessed

    lives = 7

    # Getting input and showing the results:
    while len(word_letters) > 0 and lives > 0: #for as long as there are letters in the word and user has lives left, user needs to guess.
        print('You have', lives, 'left and you\'ve used these letters:', ' '.join(used_letters))

        # Current word is W-RD
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print('Current word: ', ' '.join(word_list))

        #Getting users input:
        user_letter = input('Guess a Letter: ').upper()
        if user_letter in alphabet - used_letters:  #if the letter is in the alphabet, but not in the used_letters
            used_letters.add(user_letter)           #add the letter to used_letters
            if user_letter in word_letters:         # if the letter is in the word
                word_letters.remove(user_letter)    #remove that letter from the word
            else:                                   #if the letter is not in word (Wrong Guess!)
                lives -= 1                          #take away a life!
                print('Your letter,', user_letter, 'isn\'t in the word!')

        elif user_letter in used_letters:
            print('You\'ve already used that letter! Guess another letter!')

        else: # if the input is not in the aplphabet, it's not a letter!
            print('That\'s not a valid letter! Try again!')

    #Exit this while loop when len(word_letters) = 0 or lives = 0
    if lives == 0:
        print(lives_visual_dict[lives])
        print ('\nYou died, sorry! The word was', word)
    else:
        print ('Yay! You guessed the word', word, '!')

hangman()
