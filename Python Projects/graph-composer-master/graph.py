
"""
Empty Graph Template by Kylie Ying 
"""
# This is our Markov Chain representaion

import random

# Define the graph in term of vertices 

class Vertex(object):
    def __init__(self, value): # value will be the word
        self.value = value
        self.adjacent = {} # a dictionary of Nodes that this vertex point to: (vertex, weight)
        # lists we'll use in random selection of next word based on Weight
        self.neighbors = []
        self.neighbors_weights = []
    
    def add_edge_to(self, vertex, weight=0):
        # adding edge to the vertex we input with weight
        self.adjacent[vertex] = weight

    def increment_edge(self, vertex):
        # adding to the weight of the edge
        self.adjacent[vertex] = self.adjacent.get(vertex, 0) + 1

    def get_adjacent_nodes(self):
        return self.adjacent.keys()

    # initializes probability map
    def get_probability_map(self):
        for (vertex, weight) in self.adjacent.items():
            self.neighbors.append(vertex)
            self.neighbors_weights.append(weight)

    def next_word(self):
        # randomly select the next word but ** Based on Weights!!!
        return random.choices(self.neighbors, weights=self.neighbors_weights)[0]  # it's a list of size 1 but we still need to get the first one: [0]

# Putting the vertex representation together in a graph

class Graph(object):
    def __init__(self):
        self.vertices = {} # an empty dict to get the words (String to Vertex mapping)

    def get_vertex_values(self):
        # What are the values of all the vertices? 
        # in other words, return all possible words
        return set(self.vertices.keys())

    def add_vertex(self, value):
        # whenever we encounter a new word, we add a vertex 
        self.vertices[value] = Vertex(value) # value represents the word

    def get_vertex(self, value):
        # if the value isn't in the graph, add it.
        if value not in self.vertices:
            self.add_vertex(value)
        return self.vertices[value]  # get the vertex object

    def get_next_word(self, current_vertex):
        # maps the vertex object to its current value 
        return self.vertices[current_vertex.value].next_word()

    def generate_probability_mappings(self):
        # maps every vertex to its probability 
        for vertex in self.vertices.values():
            vertex.get_probability_map()
