# importing networkx  
import networkx as nx 
# importing matplotlib.pyplot 
import matplotlib.pyplot as plt 
  
class Visualizer:
    def __init__(self):
        self.g = nx.Graph()
    
    def add_edge(self, u, v):
        self.g.add_edge(u, v)
    
    def add_edge_all(self, vertices_list):
        for u,v in vertices_list:
            self.g.add_edge(u, v)
    
    def visualize(self):
        nx.draw(self.g, with_labels = True) 
        plt.savefig("graph_vizualization.png") 
        plt.show()

v = Visualizer()

# Add One edge at a time
# v.add_edge(1, 2)
# v.add_edge(2, 3) 
# v.add_edge(3, 4) 
# v.add_edge(1, 4)
# v.add_edge(1, 5)

# Add all edges at a time
v.add_edge_all([(1, 2), (2, 3), (3, 4), (1, 4), (1, 5)])

v.visualize()