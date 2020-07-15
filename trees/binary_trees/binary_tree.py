# A binary tree is a non linear data structure 
# where each node can have at most 2 child nodes.

# there is no ordering in terms of how the nodes are organised in the binary tree.

class BinaryTree(Node):
    
    def insert(self, data):
    
        if self.data:  # If no data empty tree, use base case
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            else:
            # elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
    
    def print_tree(self):
        if self.left:
            self.left.print_tree()
    
        # base case - root node
        print(self.data)         # printed the left most mode
                                 # now backtracking to previous node
                                 # when left nodes of current subtree are finished
                                 # print(root)
                                 # same for right subtree now
        if self.right:
            self.right.print_tree()