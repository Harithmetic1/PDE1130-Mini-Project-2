# This solves SOB35
class Rectangle():
    shape = "rectangle"
    def __init__(self, width, height): # Function to instantiate the object with width and height passed as arguments
        self.width = width
        self.height = height

    def setWidth(self, newWidth): # Function to change the width of the rectangle entered
        self.width = newWidth
    
    def setHeight(self, newHeight): # Function to chnage the height of the rectangle entered
        self.height = newHeight

    def getArea(self): # Function for calculating the area of the rectangle
        area = self.width * self.height
        print("Area of rectangle: ", area)
        return (area)

    def getPerimeter(self): # Function for calculating perimeter of the rectangle
        perimeter = 2 * (self.width + self.height)
        return f'Perimeter of rectangle: {perimeter}m'

    
    def getDiagonal(self): # Function for finding the length of the diagonal for the shape 
        diagonal = (self.width ** 2 + self.height ** 2) ** 0.5
        return f'The diagonal lenght of this {self.shape} is: {diagonal}'

    def getPicture(self): # Function for drawing the picture of the shape to the terminal
        if self.width < 50 and self.height < 50:
            for i in range(self.height):
                print("*" * self.width)
        else:
            print("Shape is too big")

    # This solves SOB32
    def getAmountInside(self, shape): # This function gets a square or rectangle as an argument and returns the amount of times the shape will fit in the parent shape
        if shape.lower() == "rectangle":
            recHeight = int(input("Enter height of rectangle: "))
            recWidth = int(input("Enter width of rectangle: "))
            area = recWidth * recHeight
        elif shape.lower() == "square":
            length = int(input("Enter length of the square: "))
            area = length ** 2
        else:
            return "Enter either square or rectangle"
        areaOfShape = self.getArea() # Gets area of parent shape
        amountInside = areaOfShape/ area # Calculation to check the amount of times the shape fills the parent shape
        if amountInside < 1:
            return "Entered shape is too big"
        else:
            return f"The {shape} will fill the {self.shape} {round(amountInside)} times" 
        
    def __str__(self) -> str:
        return f"Hi, i am a {self.shape} with height {self.height}m and width {self.width}, Area of {self.shape}: {self.getArea()} and {self.getPerimeter()}"

class Square(Rectangle): # A square class that inherits from the rectangle class 
    shape = "square"
    def __init__(self, width): # Function for instantiating the square class
        super().__init__(width, height = width)

    def setSide(self, side): # Function for changing the side length of the square 
        self.width = side

    def getArea(self): # Function for calculating the area of the square
        area = self.width ** 2
        print("Area of square: ", area)
        return (area)

    def getPerimeter(self): # Function for calculating perimeter of the rectangle
        perimeter = 4 * (self.width)
        return f'Perimeter of square: {perimeter}m'

    def __str__(self) -> str:
        return super().__str__() + f". Being a square is awesome"

