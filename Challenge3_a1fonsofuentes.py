print("Welcome of the Temperature Conversion App.")
fahrenheit = float(input("Enter the temperature in degrees Fahrenheit: "))
celsius = round((fahrenheit - 32) * 5/9, 4)
kelvin = celsius + 273.15

print(f"""
Degrees Fahrenheit: {fahrenheit}
Degrees Celsius: {celsius}
Degrees Kelvin: {kelvin}
""")
