# left -> root -> right

from trees.binary_trees.binary_search_tree.traversal.Node import Node

class InOrderTraversal(Node):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def in_order_traversal(self, root):
        traversed_arr = []
        # base case
        if(root):
            traversed_arr = self.in_order_traversal(root.left)
            traversed_arr.append(root.data)
            traversed_arr += self.in_order_traversal(root.right)
        return traversed_arr


root = InOrderTraversal(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
root.print_tree()
print(root.in_order_traversal(root))