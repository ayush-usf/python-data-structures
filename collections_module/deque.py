# Deque is preferred over list in the cases where 
# we need quicker append and pop operations from both 
# the ends of container, as deque provides
# an O(1) time complexity for append and pop operations

# Methods/Functions
# append(), appendleft()
# pop(), popleft()

import collections

de = collections.deque([3,4])
print(de)

# append()
de.append(5)
print(de)

de.appendleft(6)
print(de)

# extend(iterable)
# It appends multiple iterable elements
de.extend([11,12])
print('de: (extend) ', de)

# Order is reversed as a result of left appends.
de.extendleft([1,2])
print('de: (extendleft) ', de)
# insertionn will be like 2,1 and not 1,2
reverse_list = [1,2]
reverse_list.reverse()
de.extendleft(reverse_list)
print('de: (extendleft.reverse()) ', de)


# pop()
print(de.pop())
print(de.popleft())

# index(ele, beg, end) :- 
# This function returns the first index of the value mentioned
# in arguments, starting searching from beg till end index.
list = [1,2,3]
deq = collections.deque(list)

idx = deq.index(2, 0, len(list))
print('idx: ', idx)

# insert(i, a) :- 
# This function inserts the value mentioned in 
# arguments(a) at index(i) specified in arguments.
deq.insert(2,10)
deq.insert(4,10)
print('deq: (after insert)', deq)

# remove() :- 
# This function removes the first occurrence
# of value mentioned in arguments.
deq.remove(10)
print('deq: (after remove) ', deq)

# Will get error as 10 doesn't exist in deque
# de.remove(10)


print("================= Deque (Rotate) =======================")

import copy

print('deq: ', deq)
deq1 = copy.deepcopy(deq)

# Clockwise
deq1.rotate()

print('deq: (after Clockwise rotate) ', deq1)

# Couterclockwise
deq.rotate(-1)
print('deq: (after Couterclockwise rotate) ', deq)

deq.clear()
print('deq: (after clear) ', deq)
