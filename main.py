#Nava Levene-Harvell
#Polygon Class

import math

#this is the superclass/baseclass
class Polygon:
    def __init__(self, num_of_sides):
        self.n = num_of_sides
        self.sides = []
        self.perimeter = 0.0

    #will find and print the perimeter
    def findPerimeter(self):
        for i in range(self.n):
            self.sides.append(float(input("Enter the length of a side: ")))


        for item in self.sides:
            self.perimeter += item

        print("The perimeter is %.2f" % self.perimeter)
        print()
 

    def dispSide(self):
        #displays the length for each side
        print("This polygon has %d sides" % len(self.sides))
        print("This polygon has sides with lengths", self.sides)
        print()

    #this will print all info about the polygon
    def __str__(self):
        self.dispSide()
        return("The perimeter is %.2f" % self.perimeter)

#below are three subclasses with different areas! Square, RightTriangle and Regualr Pentagon

class RightTriangle(Polygon):
    def __init__(self, num_of_sides = 3):
        Polygon.__init__(self, num_of_sides)
        self.area = 0.0

    def findPerimeter(self):
        Polygon.findPerimeter(self)

    def dispSide(self):
        print("This right triangle has %d sides" % len(self.sides))
        print("This right triangle has sides with lengths", self.sides)
        print()

    def findArea(self):
        self.area = self.sides[0] * self.sides[1] * 0.5
        print("The area of this right triangle is %.2f" % self.area)
        print()

    def __str__(self):
        Polygon.__str__(self)

class Square(Polygon):

    def __init__(self, num_of_sides = 4):
        Polygon.__init__(self, num_of_sides)
        self.area = 0.0

    def findPerimeter(self):
        Polygon.findPerimeter(self)

    def dispSide(self):
        print("This square has %d sides" % len(self.sides))
        print("This square has sides with lengths", self.sides)
        print()

    def findArea(self):
        self.area = self.sides[0] * self.sides[1] 
        print("The area of this square is %.2f" % self.area)
        print()

    def __str__(self):
        Polygon.__str__(self)



class RegularPentagon(Polygon):

    def __init__(self, num_of_sides = 5):
        Polygon.__init__(self, num_of_sides)
        self.area = 0.0

    def findPerimeter(self):
        Polygon.findPerimeter(self)

    def dispSide(self):
        print("This pentagon has %d sides" % len(self.sides))
        print("This pentagon has sides with lengths", self.sides)
        print()

    def findArea(self):
        self.area = ( (5 * self.sides[0]) ** 2 ) / 4 * math.sqrt(5 - 2 * math.sqrt(5)) 
        print("The area of this pentagon is %.2f" % self.area)
        print()

    def __str__(self):
        Polygon.__str__(self)
    


if __name__ == "__main__":

    shape = Polygon(6)

    shape.findPerimeter()
    
    shape.dispSide()

    print(shape)

    tri = RightTriangle()

    tri.findPerimeter()
    
    tri.dispSide()

    tri.findArea()

    print(tri)

    square = Square()

    square.findPerimeter()
    
    square.dispSide()

    square.findArea()

    print(square)

    pentagon = RegularPentagon()

    pentagon.findPerimeter()
    
    pentagon.dispSide()

    pentagon.findArea()

    print(pentagon)
            
  
