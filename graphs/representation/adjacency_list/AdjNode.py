# An array of lists is used.
#   - Size of the array is equal to the number of vertices
#   - An entry array[i] represents the list of vertices adjacent to the ith vertex
#   - If weighted graph, the weights of edges can be represented as lists of pairs

# A class to represent node of an adjacency list
class AdjNode:
    def __init__(self,data):
        self.vertex = data
        self.next = None
