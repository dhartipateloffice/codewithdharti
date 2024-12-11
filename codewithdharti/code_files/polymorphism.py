# methods/functions with the same name that can be executed on many

class Shape:
    def calculateArea(self):
        raise NotImplementedError("Subclasses must implement this method")
    
class Square(Shape):

    def __init__(self, side):
        self.side = side

    def calculateArea(self):
        return self.side ** 2
    
class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def calculateArea(self):
        return 3.14 * (self.radius ** 2)
    
class Rectangle(Shape):

    def __init__(self, length,width):
        self.length = length
        self.width = width

    def calculateArea(self):
        return self.length * self.width

squareobj = Square(5)
circleobj = Circle(3)
rectangleobj = Rectangle(4, 6)

sqare_result = squareobj.calculateArea()
print(sqare_result)
circle_result = circleobj.calculateArea()
print(circle_result)
rectangle_result = rectangleobj.calculateArea()
print(rectangle_result)

# print()
# shapes = [square, circle, rectangle]
# for shape in shapes:
#     print(shape.calculateArea())