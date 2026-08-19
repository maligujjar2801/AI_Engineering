class Rectangle :
    def __init__(self,length,width):
        self.length = length
        self.width = width 
    def area(self):
        return self.length * self.width
    def __str__(self):
        return f"length={self.length}, width={self.width}"
    def __eq__(self , other):
        return self.area() == other.area()
    def __add__(self , other):
        return self.area() + other.area()


rect1 = Rectangle(10,20)
rect2 = Rectangle(20,10)
print(rect1 == rect2)  # True because both rectangles have the same area
print(rect1 + rect2)   # 400 (area of rect1 + area of rect2)    
print(rect1)           # length=10, width=20
print(rect2)           # length=20, width=10    