# Python’s Itertool 
# It is a module that provides various functions 
# that work on iterators to produce complex iterators
# It is fast, memory-efficient tool that is used either
# by themselves or in combination to form iterator algebra.

# itertools.groupby()
# Syntax: itertools.groupby(iterable, key_func)

import itertools as iter

input_list = [("a",1), ("a",2),("a",3), ("b",1), ("b",6), ("a",2)]
key_func = lambda x : x[0]

input_list.sort(key=key_func)

for key, group in iter.groupby(input_list, key_func):
    # print(key, list(group))
    # The below will not work if above uncommented
    # The type of group will become list type
    print(key, sum(row[1] for row in group))
    