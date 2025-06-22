import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

# Test the classes (optional)
# if __name__ == "__main__":
#     rectangle = Rectangle(10, 5)
#     circle = Circle(7)
#     print(f"The area of the Rectangle is: {rectangle.area()}")
#     print(f"The area of the Circle is: {circle.area()}")
