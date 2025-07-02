class Dog:
    def __init__(self, name, breed): # Constructor
        self.name = name
        self.breed = breed

    def bark (self):
        print(f"{self.name} is saying waoof to you, who is {self.breed}")

d = Dog("Moti", "Gali ka Kutta")
d.bark()