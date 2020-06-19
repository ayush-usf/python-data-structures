# Pro: Faster and uses less space for Sparse Graph
# Con: Slower for Sparse Graph, complex for weighted edges

from graphs.representation.adjacency_list.AdjNode import AdjNode

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [None] * self.V
    
    def add_edge(self, src, dest):
        node = AdjNode(dest)
        node.next = self.graph[src]
        self.graph[src] = node