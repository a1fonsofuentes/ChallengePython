import math
print("Welcome to the Right Triangle Solver App.")
first_leg = float(input("What is the first leg of the triangle: "))
second_leg = float(input("What is the second leg of the triangle: "))
hypotenuse = round(math.sqrt((first_leg**2) + (second_leg**2)), 4)
area = (first_leg*second_leg)/2

print(f"""
For a triangle with the given legs, the hypotenuse is {hypotenuse}.
For a triangle with the given legs, the area is {area}.
""")