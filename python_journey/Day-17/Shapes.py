from abc import ABC , abstractmethod 

class Shapes(ABC) :

    @abstractmethod

    def area(self):
        pass

class Circle(Shapes) :
    def area(self,radius):
        return 3.14*radius**2

class Rectangle(Shapes) :
    def area(self,length,width):
        return length*width

class Square(Shapes) :
    def area(self,length):
        return length**2
    
circle = Circle()
rect = Rectangle()
square = Square()

print(circle.area(2))
print(rect.area(2,3))
print(square.area(3))