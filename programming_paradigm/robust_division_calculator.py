# A script containing division logic including error handling.

# Function definition
def safe_divide(numerator, denominator):
    """This function safely divides numbers with error handling for zeros and non-numerics"""
    # Code to try
    try:
        result = float(numerator) / float(denominator)
        return f"The result of the division is {result}"
    # Except division by zero printing exactly Error: Cannot divide by zero.
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    # Except valueError for non-numeric division
    except ValueError:
        return "Error: Please enter numeric values only."


