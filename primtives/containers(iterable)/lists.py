print("===================================================")

# list is a type of object

basic_list = [1,2,3,4,5]

# Prints the values to a stream, or to sys.stdout by default.
print(basic_list)

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
print('class_list: ', class_list)

for obj in class_list:
    print(obj,"|", obj.name,"|", obj.roll)

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
l1 = ["eat","sleep","repeat"] 

# index starts from 0
for idx,element in enumerate(l1): 
    print(idx,element)

# index starts from 100
for idx,element in enumerate(l1,100): 
    print(idx,element)