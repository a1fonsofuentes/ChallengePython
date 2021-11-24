import cmath

print("Welcome to the Quadratic Equation Solver App.")
times = int(input("How many equations do you want to solve today? "))
for range in (1, times):
    a = float(input("Please enter your value of a (coefficient of x^2): "))
    b = float(input("Please enter your value of b (coefficient of x): "))
    c = float(input("Please enter your value of c (coefficient): "))

    d = (b**2) - (4*a*c)
    x1 = (-b -cmath.sqrt(d))/(2*a)
    x2 = (-b +cmath.sqrt(d))/(2*a)

    print(f"""
    The solutions to {a}x^2 + {b}x + {c} = 0 are: 
    x1 = {x1}
    x2 = {x2}
    """)

