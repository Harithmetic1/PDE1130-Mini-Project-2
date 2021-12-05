"""
Author: Harith Oluwatosin Onigemo
MISIS: M00810859
Tutor: Miss Engie Bashir
Title: Second Mini Project
"""
from rectangle import * 
"""
This solves part of SOB33 (Write code that makes use of a library or external module to carry out specialized tasks. Describe how the interpreter/compiler 'imports)
Check the README.md file for the explanation
"""
from datetime import date


today = date.today() # Function to get the present date
print(f"Welcome to the rectangle shape maker! Today's date is {today}\nUse the rectangle class to create a rectangle and perform desired methods with it.")

# This solves SOB 34 (Write code that utilizes classes/objects/methods in an appropriate scenario. Instantiate an object and modify its state using methods.)
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