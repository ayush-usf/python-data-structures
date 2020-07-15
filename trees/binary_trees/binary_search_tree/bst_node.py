class Node():
    def __init__(self, val):
        self.left =  None
        self.right = None
        self.val = val

    def insert(self, val):
    
        if self.val:     # If no val empty tree, use base case
            if val < self.val:
                if self.left is None:
                    self.left = Node(val)
                else:
                    self.left.insert(val)
            else:
            # elif val > self.val:
                if self.right is None:
                    self.right = Node(val)
                else:
                    self.right.insert(val)
        else:
            self.val = val
    
    def print_tree(self):
        if self.left:
            self.left.print_tree()