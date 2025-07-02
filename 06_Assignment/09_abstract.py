# yahan sab se pehle abc module ko import kraen getattr
# abc stands for abstract based class

from abc import abstractmethod , ABC
# now we create a class

class Shape:
# and inherit here abc
# abc does not run directly

#  ab aik decorator create kren ge

    @abstractmethod
# kisi bhi shape (circle,triangle,square,rectangle ect)
#  k liye area ka ka veriable lena zururi he warna wo kaam nhi kre ga

    def area (self):
        pass

class Rectangle(Shape):
    def __init__(self, width , height):
        self.width = width
        self.height = height

    def area (self):
        return self.width * self.height

rect = Rectangle(5,10)
print (f"The area of Rectangel = {rect.area()}")
      
