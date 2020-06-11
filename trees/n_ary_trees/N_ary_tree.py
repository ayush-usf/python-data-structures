# https://github.com/joaohelis/n_ary_tree_with_python/blob/master/n_ary_tree.py

from trees.n_ary_trees.Node import Node

class NAryTree(Node):
    
    def __init__(self):
        self.root = None
        self.size = 0
    
    def insert(self, key, parent_key):
        pass