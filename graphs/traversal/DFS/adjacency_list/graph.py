# Depth First Traversal (or Search) for a graph is similar to 
# Depth First Traversal of a tree. The only catch here is, unlike trees, 
# graphs may contain cycles, a node may be visited twice. 
# 
# To avoid processing a node more than once, we use a boolean visited array.

# Input | V = 4 | E = 6

# Approach:
# 1. start from the root (arbitrary node)
# 2. mark the node 
# 3. move to the adjacent unmarked node and move to the adjacent unmarked node
# 4. backtrack and check for other unmarked nodes

from collections import defaultdict # if key not found, map[key] = 0, no error

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)
    
    def addEdge(self, u, v):
        print("Add edge here")

    # A function used by DFS 
    def DFSUtil(self, v, visited):
        print("DFSUtil")

    # The function to do DFS traversal. It uses 
    # recursive DFSUtil() 
    def DFS(self, v):
        print("DFS")