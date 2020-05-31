# list is a type of object

basic_list = [1,2,3,4,5]
print(basic_list)

################################################

# Class List

class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

class_list = []

class_list.append(Student("Ayush",1))
class_list.append(Student("Adarsh",2))
class_list.append(Student("Ameya",3))

# This will print list of objects
print('class_list: ', class_list)

for obj in class_list:
    print(obj,"|", obj.name,"|", obj.roll)
