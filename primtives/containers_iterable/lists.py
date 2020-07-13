print("===================================================")

# list is a type of object

basic_list = [1,2,3,4,5]

# Prints the values to a stream, or to sys.stdout by default.
print(basic_list)

################################################

# Iterator / Iterable

iterable_value = "Ayush"
iterable_obj = iter(iterable_value)

while True: # Nothing like hasNext()
    try:
        item = next(iterable_obj)
        print(item, "| ", end = '') # end = '' means no new line
    except StopIteration:
        print()
        break

# Enumerate() - get index from iterable
# In Python, the enumerate function returns a Python object of type enumerate

print("list(enumerate(['a', 'b', 'c'])): ", list(enumerate(['a', 'b', 'c'])), "\n")

l1 = ["eat","sleep","repeat"] 

# index starts from 0
for idx,element in enumerate(l1): 
    print(idx,element)

# index starts from 100
for idx,element in enumerate(l1,100): 
    print(idx,element)

print("\n======= Enumerate with a Different Starting Index ==========")
L = ['apples', 'bananas', 'oranges']
for idx, s in enumerate(L, start = 1):
    print("index is %d and value is %s" % (idx, s))

################################################

# List of Objects

class Student:
    def __init__(self, name, roll):
        self.name = name    # Instance variables -
        self.roll = roll    # no extra declaration

class_list = []

class_list.append(Student("Ayush",1))
class_list.append(Student("Adarsh",2))
class_list.append(Student("Ameya",3))

# This will print list of objects
print(\n'class_list: ', class_list)

for obj in class_list:
    print(obj,"|", obj.name,"|", obj.roll)

print("=============== sorting - sorted() ===============")
# sorted()
# sorted() method sorts the given sequence either in ascending order 
# or in descending order and always return the a sorted list. 
# This method does not effect the original sequence.

# Syntax: 
# sorted(iterable, key, reverse=False)
#       iterable: sequence (list, tuple, string) or 
#                  collection (dictionary, set, frozenset) or 
#                   any other iterator that needs to be sorted.
#       Key(function): 
#               A function that would serve as a key or a basis of sort comparison.


logs  = ["let3 art can","let1 own kit dig","let2 art zero"]

print("\nlist:", logs) 
print("\nSorted list (new iterable):", sorted(logs)) 
print("Reverse sorted list (new iterable):", sorted(logs, reverse = True))
print("Original list after sorting:", logs,"\n") 


print("========== sorting - sort() [Uses Timsort]===============")
# Timsort
#       hybrid stable sorting algorithm, derived from merge sort and insertion sort

# Timsort Complexity
#       Worst case performance       O(nlogn)
#       Best case performance        O(n)       // linear time
#       Average case performance     O(nlogn)
#       Worst case space complexity - O(n)
#          Timsort can require a temp array containing as many as N//2 pointers
