## PYTHON MINI PROJECT 2 - M00810859

# Class Created - Shapes.py

This method contains two classes
1. Rectangle class
2. Square class (Sub-class)

The Module allows you to instantiate a rectangle with its width and height passed as arguments and a square with length of each side passed as an argument.

Each class contains different methods
1. setWidth() - This is the function used for changing the width of the rectangle after instantiated
2. setHeight() - This is the function used for changing the height of the rectangle after instantiated
3. setSide() - This is the function for changing the length of each side of the square after being instantiated
4.  getArea() - This is the function for calculating the area of the rectangle or square
5. getPerimeter() - This is the function for calculating the perimeter of the rectangle or square
6. getDiagonal() - This is the function for finding the length of the diagonal of the rectangle or square
7. getPicture() - Function for drawing the picture of the shape to the terminal
8. getAmountInside() - This function gets a square or rectangle as an argument and returns the amount of times the shape will fit in the parent shape

## Python's Compiler Import functionality

When we want to use codes from a module or library, we need to import that library or module into the required program. To do this we use the import keyword. 

Import can be done in three different ways
1. Full import: This gets all the classes used in that module into our program and ready to be used by the programmer
`import xyz`
2. Partial import: This is used to get specific classes from a module/library, to prevent the burdening the interpreter with information that won't be used. 
`from xyz import abc`
3. Renaming modules: We can import a module with a different name just in case the module/library name is too long for us to use. 
`import xyz as abc`

To import a library/module into a python program we need to keep the module in the same directory as the required program or install it into the python virtual machine.  