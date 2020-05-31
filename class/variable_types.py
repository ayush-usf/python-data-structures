class CSStudent:
    static_var_stream = "CSE"

    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

## Driver code in same Python Module

student1 = CSStudent("Ayush",1)
student2 = CSStudent("Akaash",2)

print(CSStudent.static_var_stream) # CSE

print(student1.name,"|", student1.roll,"|",student1.static_var_stream)
#                            ('Ayush', '|', 1, '|', 'CSE')

print(student2.name,"|", student2.roll,"|",student2.static_var_stream)
#                            ('Akaash', '|', 2, '|', 'CSE')