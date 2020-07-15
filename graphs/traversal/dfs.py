# ------------------ Extra Imports ------------------
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
from visualization import Visualizer
# ------------------------------------------------------

# Depth-first search is an algorithm for traversing or searching tree or graph data structures

# Graphs may contain cycles. So, a node may be visited twice. 
# To avoid processing a node more than once, we use a boolean visited array.
# visited_arr = [False] * (V)

# We use defaultdict() as adjacency list to store the Graph data

# Time complexity: O(V + E) ; V is the number of vertices visited and E is the edge count
# Space Complexity: O(V)

# Approach:
# 1. Create a recursive function that takes the 
#           - index of node
#           - visited array
# 2. mark the node 
# 3. move to the adjacent unmarked node and move to the adjacent unmarked node
# 4. backtrack and check for other unmarked nodes

# N = V = 4 | E = 6

from collections import defaultdict   # if key not found, defaultdict[key] = []

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)  # default_factory() of type list
        self.v = Visualizer()
        self.result = ''

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.v.add_edge(u,v)
    
    def visualize(self):
        self.v.visualize()   
    
    def print(self, starting_node):
        print("DFS from vertex {} = {}".format(starting_node, self.result))

    # The function to do DFS traversal. It uses 
    # recursive DFSUtil() 
    def DFS(self, v):
        
        '''
        6 starting vertices from 0 to 5
        => bool array with 6 elements
        '''
        visited_arr = [False] * (max(self.graph) + 1)
        
        '''
        recursive function that takes 
        the index of node and 
        visited array
        '''
        self.DFSUtil(v , visited_arr)

    # Recursive function for DFS with Backtracking
    def DFSUtil(self, v, visited):
        
        visited[v] = True
        # Adding V to result
        self.result += str(v) + " "

        # Traversing vertices adjacent to this vertex 
        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)
    


g = Graph()

g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 

starting_node = 2

print("======== Graph traversal from node {} ========".format(starting_node))
g.DFS(starting_node)
g.print(starting_node)
g.visualize()
