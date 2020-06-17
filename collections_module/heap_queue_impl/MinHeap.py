# Heaps
# Insertion - top to bottom, left to right
# Insert at root and call heapify

# Insertion is possible only at specific places
# So, the indexes can be mapped.
# Root = 0, Left child of Root = 1, Right child of Root = 2
# Left child of node 1 = 3, Right child of node 1 = 4
# Left child of node 2 = 5, Right child of node 2 = 6  and so on....

# Parent = (idx - 2)/2  | left child = (idx * 2) + 1 |  right child = (idx * 2) + 2

print("=========== Min Heap ============")
# MINIMUM : get_min()
# MAXIMUM :
# INSERT :

class MinHeap:
    def __init__(self,max_size):
        self.max_size = max_size
        self.size = 0
        self.Heap = 