class Node:
    def __init__(self, data, children = None):
        self.data = data
        self.children = children or []