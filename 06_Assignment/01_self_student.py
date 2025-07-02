class Student:
        def __init__ (self, name , marks):
            self.name = name
            self.marks = marks

        
        def display(self):
            print(f"Hi! my name is {self.name} and I got {self.marks} in my last semester")

s1 = Student("Faiza" , 58)
s1.display()