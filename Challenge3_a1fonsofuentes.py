print("Welcome of the Temperature Conversion App.")
fahrenheit = float(input("Enter the temperature in degrees Fahrenheit: "))
celsius = round((fahrenheit - 32) * 5/9, 4) #operacion para convertir a celsius 
kelvin = celsius + 273.15 #operacion para convertir a kelvin

print(f"""
Degrees Fahrenheit: {fahrenheit}
Degrees Celsius: {celsius}
Degrees Kelvin: {kelvin}
""")
#printf con 3 comillas para poder escribir todo en muchas líneas.
