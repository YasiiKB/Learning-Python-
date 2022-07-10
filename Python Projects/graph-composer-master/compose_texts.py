"""
Empty Compose Template by Kylie Ying
"""

import os
import re
import string
import random

from graph import Graph, Vertex

# Step 1: Get words from text
def get_words_from_text(text_path):
    with open(text_path, 'rb') as file:
        text = file.read().decode("utf-8") 

        # remove [verse 1: artist]
        # include the following line if you are doing song lyrics
        # text = re.sub(r'\[(.+)\]', ' ', text)

        text = ' '.join(text.split())
        text = text.lower()
        text = text.translate(str.maketrans('', '', string.punctuation))

    words = text.split()

    words = words[:1000]

    return words

# Step 2: Make a graph using those words
def make_graph(words):
    g = Graph()
    prev_word = None
    # for each word
    for word in words:
        # check that word is in graph, and if not then add it
        word_vertex = g.get_vertex(word)

        # if there was a previous word, then add an edge if does not exist
        # if exists, increment weight by 1
        if prev_word:  # prev word should be a Vertex
            # check if edge exists from previous word to current word
            prev_word.increment_edge(word_vertex)

        prev_word = word_vertex
    # we need the probability mapping for choosing the next word
    g.generate_probability_mappings()
    
    return g

# Step 3: For x number of words (defined by user), get the next word
def compose(g, words, length=50):
    composition = []
    word = g.get_vertex(random.choice(words)) # pick a random word to begin with. 
    for _ in range(length):
        composition.append(word.value)
        word = g.get_next_word(word) # then get the next word and replace it in the random word chosen at first

    return composition

def main():
    # Step 1: Get words from text
    words = get_words_from_text('texts/hp_sorcerer_stone.txt')

    # Step 2: Make a graph using those words
    g = make_graph(words)

    # Step 3: For x number of words (defined by user), get the next word   
    composition = compose(g, words, 100)  # 100 overwrites the length= 50 we defined in def compose(g, words, length=50)
    
    # Step 4: Show the results!
    print(' '.join(composition)) # returns and prints a *string*, not a list, where all the words and separated by a space


if __name__ == '__main__':
    main()