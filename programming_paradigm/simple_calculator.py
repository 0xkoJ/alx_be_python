class SimpleCalculator:
    """A simple calculator class that support basic arithematic operations"""
    def add( self, a, b):
     """return the addition of a and b"""
     return a + b
    def subtract(self, a, b):
       """return the subtravtion of a and b"""
       return a - b
    def multiply(self, a , b):
       """return the multiplication of a and b """
       return a * b
    def divide(self, a, b):
       """return the division of a by b. Return None if b is zero"""
       if b == 0:
           raise ZeroDivisionError("Division by zero is not allowed") 
        
       return a / b