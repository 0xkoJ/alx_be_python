import sys
def safe_divide(numerator, denominator):
    #convert input into floats for division
    try:
        num = float(numerator)
        denom = float(denominator)
        result = num/denom
        return result
    except ZeroDivisionError:
      return "Error: Cannot be divide by zero."
    except ValueError:
        return "Error: Please provide numeric values."