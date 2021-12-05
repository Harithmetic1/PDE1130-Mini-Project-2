from shapes import *
"""
Author: Harith Oluwatosin Onigemo
MISIS: M00810859
Tutor: Miss Engie Bashir
Title: Second Mini Project

"""


rect = Rectangle(5, 10)
rect.getArea()
rect.setWidth(3)
print(rect.getPerimeter())


sq = Square(4)

sq.getArea()
sq.setSide(6)
print(sq.getDiagonal())

print(rect.getAmountInside("square"))
sq.getPicture()

print(sq)
print(rect)