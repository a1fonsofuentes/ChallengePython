print("Welcome to the multiplication/Exponent Table App") #primero multiplicación, luego potencias.
name = (input("What is your name? ")).title()
number = float(input("What number would you like to work with? "))

print(f"Multiplication table for {number}")
print(f"""
1.0 * {number} = {number * 1}
2.0 * {number} = {number * 2}
3.0 * {number} = {number * 3}
4.0 * {number} = {number * 4}
5.0 * {number} = {number * 5}
6.0 * {number} = {number * 6}
7.0 * {number} = {number * 7}
8.0 * {number} = {number * 8}
9.0 * {number} = {number * 9} 
""")
print(f"""
1.0 * {number} = {number ** 1}
2.0 * {number} = {number ** 2}
3.0 * {number} = {number ** 3}
4.0 * {number} = {number ** 4}
5.0 * {number} = {number ** 5}
6.0 * {number} = {number ** 6}
7.0 * {number} = {number ** 7}
8.0 * {number} = {number ** 8}
9.0 * {number} = {number ** 9}
""")

print(f"{name} math is cool.")