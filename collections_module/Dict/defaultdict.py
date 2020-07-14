# defaultdict is a sub-class of the dict class
# It provides a default value, with extra code from user, 
# for the key that does not exists.

# defualtdict never raises a KeyError

# Inner Working
# In addition to the standard dictionary operations, Defaultdict adds 
#       - one writable instance variable :  default_factory
#       - one method  :                     __missing__()


print("=================== __missing__() ===================")

from collections import defaultdict
import json

def undef_val(): 
    return "Not Present"
      
# Defining the dict 
d = defaultdict(undef_val) 
d2 = defaultdict(lambda: "Not Present") 


d["a"] = 1
d["b"] = 2
print('d: ', json.dumps(d, indent=4))

print('d["a"]: ', d["a"])
print('d["b"]: ', d["b"])
print('d["c"]: ', d["c"])

# Provides the default value for the key even if key already exists
print("d.__missing__('a'): ", d.__missing__('a'))       # Not Present
print("d.__missing__('d'): ", d.__missing__('d'), "\n") # Not Present

d2["a"] = 1
d2["b"] = 2

print('d2["a"]: ', d2["a"])
print('d2["b"]: ', d2["b"])
print('d2["c"]: ', d2["c"])

print("============= default_factory() of type list =============")

d = defaultdict(list)  # passing type list

for i in range(2): 
    d[i].append(i+10) 
      
print(d)
print('d: ', json.dumps(d, indent=4))

print("============= default_factory() of type int =============")

d = defaultdict(int) 
   
L = [1, 2, 3, 4, 2, 4, 1, 2]
for i in L: 
    d[i] += 1
print('d: (Number of occurences)', json.dumps(d, indent=4))
