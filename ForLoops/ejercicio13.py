print("Welcome to the factorial calculator!")
n = int(input("Enter a number: "))

a = 1
for i in range(2, n + 1):
 a *= i
 print(a) 