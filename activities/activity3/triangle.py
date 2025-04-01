import math

class RightTriangle():
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        area = (self.base * self.height) / 2
        return area

    def pythagorean(self):
        hypotenuse = math.sqrt(self.base**2 + self.height**2)
        return hypotenuse
    
    def perimeter(self):
        hypotenuse = self.pythagorean()
        perimeter = self.base + self.height + hypotenuse
        return perimeter