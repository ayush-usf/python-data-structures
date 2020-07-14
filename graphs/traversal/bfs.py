# Algorithm:
# 1. Create a recursive function that takes the index of node and a visited array.
# 2. Mark the current node as visited and print the node.
# 3. Traverse all the adjacent and unmarked nodes and call the recursive function with index of adjacent node.

# ------------------ Extra Imports ------------------
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
from visualization import Visualizer
# ------------------------------------------------------