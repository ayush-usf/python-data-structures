import collections

dict1 = {"a":1,"b":2}
dict2 = {"a":4,"c":3}

print("=============== Chainmap ================")
#  It encapsulates many dictionaries into one unit

print('dict1: ', dict1)
print('dict2: ', dict2)

combined_dict1 = collections.ChainMap(dict1, dict2)

print("ChainMap(dict1, dict2)")
for key,val in combined_dict1.items():
    print('key,val: ', key,val)

print("ChainMap(dict2, dict1) // Keys with smaller value taken")
combined_dict2 = collections.ChainMap(dict2, dict1)
for key,val in combined_dict1.items():
    print('key,val: ', key,val)