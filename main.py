from rectangle import * 
from datetime import date # This solves part of SOB33, Check the README.md file for the remaining part
"""
Author: Harith Oluwatosin Onigemo
MISIS: M00810859
Tutor: Miss Engie Bashir
Title: Second Mini Project

"""

today = date.today() # Function to get the present date
print(f"Welcome to the rectangle shape maker! Today's date is {today}\nUse the rectangle class to create a rectangle and perform desired methods with it.")

# This solves SOB 34
rect = Rectangle(5, 10)
# rect.getArea()
# rect.setWidth(3)

print(rect)



sq = Square(4)
sq.getPicture()

# sq.getArea()
# sq.setSide(6)
# print(sq.getDiagonal())

# print(rect.getAmountInside("square"))

print(sq)