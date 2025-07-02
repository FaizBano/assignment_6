class Person:
    def __init__(self, name):
        self.name = name

#  ab aik aur class banaen ge our is me Person ko inherit kraen ge
class Teacher (Person):
    def __init__(self, name , subject):
        # super method ham class ke variable ko inherit krne k liye use krte hen
        super().__init__(name)
        self.subject = subject
tea = Teacher("Faiz", "python")
print(tea.name , tea.subject)
print(tea.name)
print (tea.subject)