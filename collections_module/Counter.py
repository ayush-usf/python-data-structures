print("===================================================")

from collections import Counter

# Counts the number of occurences, returns a list

# Syntax :
# class collections.Counter([iterable-or-mapping])

# The constructor of counter can be called in any one 
# of the following ways :
#      - With sequence of items
#      - With dictionary containing keys and counts
#      - With keyword arguments mapping string names to counts

data = [1,1,2,3,6,7,9,5,2,1]

# Declaration and Initialization
counter_obj = Counter(data)

# Empty Counter object
counter = Counter()
counter.update(data)
print('counter: ', counter)
print('counter.items(): ', counter.items())

print('counter_obj: ', counter_obj)
print('counter_obj.most_common(): ', counter_obj.most_common())
print('counter_obj.most_common(1): ', counter_obj.most_common(1))

print(Counter({'A':3, 'B':5, 'C':2}))
print(Counter(A=3, B=5, C=2))