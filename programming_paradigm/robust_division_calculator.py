# robust_division_calculator.py
def safe_divide(numerator, denominator):
    try:
        # Convert inputs to float for division
        num = float(numerator)
        denom = float(denominator)
        result = num / denom
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."