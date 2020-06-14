# Queue can be implemented using:
#     1. list : lists are quite slow for enqueue(), dequeue(), append() and pop()
#     2. collections.deque : Instead of enqueue and deque, append() and popleft() functions are used.
#     3. queue.Queue(maxsize): If maxsize = 0, infinite queue

from queue import Queue

q = Queue(maxsize=3)

print("========================== empty() ==========================")
# Return True if the queue is empty
print("Empty: ", q.empty()) 

print("========================== qsize() ==========================")

# Return the number of items in the queue. 
# If no free slot is immediately available, raise QueueFull.
print('q.qsize(): ', q.qsize())

print("========================== put(item) ==========================")
# If the queue is full, wait until a free slot is available before adding the item.
print('q.put(1): ', q.put(1))
print('q.put(2): ', q.put(2))

print("====================== Print Elements =======================")

for q_item in q.queue:
    print('q_item: ', q_item)

print('q: ', q.queue)

print("========================== full() ==========================")
# If the queue was initialized with maxsize=0 (the default), then full() never returns True.
print("Is Full (wtih 2 elements): ", q.full()) 
print('q.put(3): ', q.put(3))
print("Is Full (wtih 3 elements): ", q.full()) 

print("=============== Removing elements : get() ===================")
# Remove and return an item from the queue. 
# If queue is empty, wait until an item is available.

print('q.qsize(): ', q.qsize())
print('q.get(): ', q.get())
print('q.get(): ', q.get())
print('q.get(): ', q.get())
# print('q.get(): ', q.get()) # Queue will wait for next item to be added
print('q.qsize(): ', q.qsize())

print("============ Removing elements : get_nowait() ===============")
# raise QueueEmpty if empty queue
print('q.get_nowait(): ', q.get_nowait())