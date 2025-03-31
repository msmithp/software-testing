import math

class Triangle():
    def area(base, height):
        area = (base * height) / 2
        return area

    def pythagorean(base, height):
        hypotenuse = math.sqrt(base**2 + height**2)
        return hypotenuse
    
    def perimeter(base, height, hypotenuse):
        hypotenuse = Triangle.pythagorean(base, height)
        perimeter = base + height + hypotenuse
        return perimeter