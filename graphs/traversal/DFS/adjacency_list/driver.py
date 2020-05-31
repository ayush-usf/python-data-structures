from graph import Graph

class Driver:
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