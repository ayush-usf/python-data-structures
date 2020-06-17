# Heaps - Used to represent PRIORITY QUEUE
# Insertion - top to bottom, left to right
# Insert at root and call heapify

# Insertion is possible only at specific places
# So, the indexes can be mapped.
# Root = 0, Left child of Root = 1, Right child of Root = 2
# Left child of node 1 = 3, Right child of node 1 = 4
# Left child of node 2 = 5, Right child of node 2 = 6  and so on....

# Parent = (idx - 2)/2  | left child = (idx * 2) + 1 |  right child = (idx * 2) + 2

print("====================== heapq ======================")

# The property of this data structure in python is that 
# each time the smallest of heap element is popped(min heap).
# The heap[0] element also returns the smallest element each time

# Whenever elements are pushed or popped, heap structure in maintained

import heapq

list = [5,7,9,1,3]
print('list: ', list)

print("======== heapify(iterable) | heap order ===========")
# This function is used to convert the iterable into a heap data structure
print('heapq.heapify(list): ', heapq.heapify(list))
print('list: ', list)

print("====== heappush(heap, ele) | heap structure =======")
# This function is used to insert the element mentioned in its arguments into heap.
# The order is adjusted, so as heap structure is maintained

print("========== heappop(heap) | heap structure =========")
# This function is used to remove and return the smallest element from heap.
# The order is adjusted, so as heap structure is maintained.