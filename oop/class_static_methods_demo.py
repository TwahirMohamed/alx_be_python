# A python script that defines a class Calculator which has both class method and static method.
class Calculator:
    """Base Class to perform calculations."""
    calculation_type = "Arithmetic Operations"
    @staticmethod
    def add(a, b):
        """Method to add the sum of two numbers and return the value."""
        return a + b
    
    @classmethod
    def multiply(cls, a, b): # class method takes class as the argument.
        """Method to multiply two numbers."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
    
