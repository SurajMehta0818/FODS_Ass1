'''Write a program that will convert Celsius value to Fahrenheit.[5]'''
def celsius_to_fahrenheit(celsius):
    """Convert temperature from Celsius to Fahrenheit"""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Get input from user
celsius_input = float(input("Enter temperature in Celsius: "))

# Convert and display the result
fahrenheit_output = celsius_to_fahrenheit(celsius_input)
print(f"{celsius_input}°C is equal to {fahrenheit_output:.2f}°F")