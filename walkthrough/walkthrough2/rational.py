import math

class Rational():
    """ A rational number class to represent fractions """
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

        if denominator == 0:
            raise ZeroDivisionError

        self.__simplify()

    def __add__(self, other):
            return Rational(
                self.numerator * other.denominator + other.numerator * self.denominator,
                self.denominator * other.denominator
            )
        
    def __sub__(self, other):
        self + (-other)

    def __mul__(self, other):
        return Rational(
            self.numerator * other.numerator,
            self.denominator * other.denominator
        )
    
    def __truediv__(self, other):
        if other.numerator == 0:
            raise ZeroDivisionError
        
        return self * other.reciprocal()

    def __neg__(self):
        return Rational(-self.numerator, self.denominator)

    def __eq__(self, other):
        return self.numerator == other.numerator and self.denominator == other.denominator
    
    def __ne__(self, other):
        return not self == other
    
    def __lt__(self, other):
        return (self.numerator / self.denominator) < (other.numerator / other.denominator)
    
    def __gt__(self, other):
        return (self.numerator / self.denominator) > (other.numerator / other.denominator)
    
    def __le__(self, other):
        return self < other or self == other
    
    def __ge__(self, other):
        return self > other or self == other
        
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
    
    def __simplify(self):
        gcd = math.gcd(self.numerator, self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd

        if self.numerator < 0 and self.denominator < 0:
            self.numerator = -self.numerator
            self.denominator = -self.denominator

    def reciprocal(self):
        return Rational(self.denominator, self.numerator)
