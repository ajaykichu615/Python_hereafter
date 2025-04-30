"""Create a function convert_temperature() that takes Celsius temp and return equivalent Fahrenheit.
Ask the user for input and display the result
Formula => °F = (°C × 9/5) + 32"""

def convert_temperature(c:float):
    return (c * 9/5) + 32

c = float(input("Enter the temperature in Celsius: "))
print(f'Fahrenheit equivalent is {convert_temperature(c)}')