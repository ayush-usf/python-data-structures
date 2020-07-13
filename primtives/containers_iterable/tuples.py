# commas which tell Python something is a tuple
# brackets are added for readability
currencies = (1, 75)
currencies = 1, 75

# Adding brackets around a single number doesn't turn it into a tuple.
a = (20)
print(type(a))    # <class 'int'>

print("=============== Enumerate Tuples ===============")
print("list(enumerate(('kia', 'audi', 'bmw'))): ", list(enumerate(('kia', 'audi', 'bmw'))), \n)

L = [('Matt', 20), ('Karim', 30), ('Maya', 40)]

for idx, (name, age) in enumerate(L):
    print("index is %d, name is %s, and age is %d" \
        % (idx, name, age))

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

