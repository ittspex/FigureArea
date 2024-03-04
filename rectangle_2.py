from rectangle import Rectangle, Square, Circle

rect_1 = Rectangle(3,4)
rect_2 = Rectangle(12,5)

print(rect_1.get_area())
print(rect_2.get_area())

square_1 = Square(5)
square_2 = Square(10)

print(square_1.get_square_area(),
    square_2.get_square_area())

circle_1 = Circle(4)
circle_2 = Circle(7)
print(circle_1.get_circle_area())
print(circle_2.get_circle_area())
