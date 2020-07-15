# ------------------ Extra Imports ------------------
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
from visualization import Visualizer
# ------------------------------------------------------

# Queue is used to keep track of children nodes in sequential order

# Algorithm:
# 1. Create an iterative function that children of current visited node and enqueue in queue
# 2. Pop the current node and mark as visited
# 3. Push child nodes of current node to queue and repeat

from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph = defaultdict(list) # default_factory() of type list
        self.v = Visualizer()
        self.result = ""

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)     # Undirected graph is bidrectional
        self.v.add_edge(u,v)
    
    # No BFS util required, no recusion required
    # Will be solved with just iteration
    # Passing children of nodes iteratively and visit them
    def BFS(self, starting_node):
        
        visited_arr = [False] * (len(self.graph))
        queue = list()

        # enqueue it 
        queue.append(starting_node)
        visited_arr[starting_node] = True

        while queue:
            node = queue.pop(0)
            self.result += str(node) + " "

            for i in self.graph[node]:
                if visited_arr[i] == False:
                    queue.append(i)
                    visited_arr[i] = True
    
    def print(self, starting_node):
        print("BFS from vertex {} = {}".format(starting_node, self.result))
    
    def visualize(self):
        self.v.visualize()   
    
g = Graph()

g.add_edge(0, 2) 
g.add_edge(1, 0)
g.add_edge(1, 2) 
g.add_edge(2, 0) 
g.add_edge(2, 3) 
g.add_edge(3, 3) 

starting_node = 3

print("======== Graph traversal from node {} ========".format(starting_node))
g.BFS(starting_node)
g.print(starting_node)
g.visualize()
