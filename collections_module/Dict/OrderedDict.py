from collections import OrderedDict

print("Ordered Dict can be used as a stack with the help of popitem function")

od = OrderedDict()

od['a']=1
od['b']=2
od['c']=3

for or_key,or_val in od.items():
    print('or_key,or_val: ', or_key,or_val)

print("============== Deleting and re-inserting the same key ================")
# Deleting and re-inserting the same key will push it to 
# the back as OrderedDict however maintains the order of insertion.

od.pop('b')
od['b'] = 2


for or_key,or_val in od.items():
    print('or_key,or_val (after pop/insert): ', or_key,or_val)