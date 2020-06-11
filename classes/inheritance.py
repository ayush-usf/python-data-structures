from classes.variable_types import CSStudent

class MLCSStudent(CSStudent):
    def __init__(self, name, roll):
        self.name= "Circle"
        self.roll = roll

    def getName(self):
        return self.__class__.__name__

# c = Circle("ayush",1)

## Driver code in same Python Module

student1 = MLCSStudent("Ayush",1)
student2 = MLCSStudent("Akaash",2)

print(CSStudent.static_var_stream) # CSE

print(student1.getName(), student1.name,"|", student1.roll,"|",student1.static_var_stream)
#                            ('Ayush', '|', 1, '|', 'CSE')

print(student2.getName(),student2.name,"|", student2.roll,"|",student2.static_var_stream)
#                            ('Akaash', '|', 2, '|', 'CSE')