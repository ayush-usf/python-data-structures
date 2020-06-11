a = set('aardvark')         # {'d', 'v', 'a', 'r', 'k'} 
b = {'aardvark'}            # {'aardvark'}
# To create an empty set you have to use set(), not {}; 
# the latter creates an empty dictionary

# descending because key index hashed
currencies3 = {1, 40} or set([1, 40])     # currencies = {40, 1}
currencies3 = {1, 2} or set([1, 2])       # currencies = {1, 2}

print("===================================================")

empty_set:set = set()
empty_set2 = {}
filled_set = set()
filled_set2 = {1,2,3,4}
print('type(empty_set): ', type(empty_set))
print('type(empty_set2): ', type(empty_set2))
print('type(filled_set): ', type(filled_set))
print('type(filled_set2): ', type(filled_set2))

# Set can have any data types
filled_set.add("ayush")
filled_set.add("ayush")
print('filled_set: ', filled_set)


my_set = {1, 2, 3, 1, 2}
print('my_set (before): ', my_set)

# add multiple elements at once
my_set.update([2, 3, 4, 5, 6])
print('my_set (after adding multiple): ', my_set)

# removing elements
my_set.discard(4)
my_set.discard((5,6))
print('my_set (after discarding 4): ', my_set)

# removing multiple elements / Set Difference
print("Set Difference : ",filled_set2 - {1,2})
print("Set Difference2 : ",filled_set2.difference({3,4}))
print("Set Difference3  : ",filled_set2.difference(set([4])))

s = {1, 2, 3, 4, 5}
s.difference_update({1, 2, 3})
print('difference_update', s)

# Set Union
set3 = set(["I","was","a","list"])
union_set = (filled_set | filled_set2 | set3)
print('union_set: Base Combination -', union_set)
union_set = (filled_set | filled_set2, set3)
print('union_set: Combination 2 -', union_set)

union_set2 = filled_set2.union(filled_set).union(set3)
print('python is functional | allows mutuple unions -', union_set2)

# Set Intersection
print("Interseciton set : ",filled_set2 & {1,2})
print("Interseciton set 2 : ",filled_set2.intersection(set([3,4])))

# Symmetric Difference
A = {1, 2, 3,}
B = {3, 4, 5}

# use ^ operator
# Output: {1, 2, 3, 6, 7, 8}
print("Symmetric Difference",A ^ B)

# clear my_set
# Output: set()
my_set.clear()
print('my_set (after clearing): ', my_set)

# remove an element
# not present in my_set
# you will get an error.
# Output: KeyError

# my_set.remove(1)
# print('my_set (after removing 1 from empty set): ', my_set)



