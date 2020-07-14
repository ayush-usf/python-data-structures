# Depth-first search is an algorithm for traversing or searching tree or graph data structures

# Graphs may contain cycles. So, a node may be visited twice. 
# To avoid processing a node more than once, we use a boolean visited array.
# visited_arr = [False] * (V)

# We use defaultdict() as adjacency list to store the Graph data

# Time complexity: O(V + E) ; V is the number of vertices visited and E is the edge count
# Space Complexity: O(V)

# Approach:
# 1. Create a recursive function that takes the index of node and a visited array.
# 2. mark the node 
# 3. move to the adjacent unmarked node and move to the adjacent unmarked node
# 4. backtrack and check for other unmarked nodes

# N = V = 4 | E = 6



from collections import defaultdict # if key not found, map[key] = 0, no error

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)  # default_factory() of type list
    
    def addEdge(self, u, v):
        print("Add edge here")

    # A function used by DFS 
    def DFSUtil(self, v, visited):
        print("DFSUtil")

    # The function to do DFS traversal. It uses 
    # recursive DFSUtil() 
    def DFS(self, v):
        print("DFS")

 g = Graph()
    # g.addEdge(0,1)
    # g.addEdge(0,4)
    # g.addEdge(0,2)
    # g.addEdge(1,3)
    # g.addEdge(1,4)
    # g.addEdge(3,4)
    # g.addEdge(2,5)
    # g.addEdge(2,6)
    # g.addEdge(5,6)

    print("Following is the graph traversal from node {}".format(2))
    g.DFS(2);