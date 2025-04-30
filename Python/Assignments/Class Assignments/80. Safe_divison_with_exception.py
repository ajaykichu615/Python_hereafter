"""Safe Division with Exceptions
Q: Divide two numbers. Handle errors. Input the numbers from the user.
Input: divide(10, 0)
Output: "Error: Cannot divide by zero"""

def divide():
    try:
        numerator = float(input())
        denominator = float(input())
        result = numerator / denominator
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    except ValueError:
        return "Error: Please enter valid numbers"

# Example usage
print(divide())

