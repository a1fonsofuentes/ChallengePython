#Introducción
print("Welcome to the Average Calculator App")
name = input("What is your name? ")
num_grades = int(input(f"{name}, how many grades would you like to enter? "))
spaces = " " * 7

count = 0
list_grades = []
while count < num_grades:
    a = float(input("Enter grade: "))
    list_grades.append(a)
    count += 1
list_grades.sort(reverse = True)

print("Grades Highest to Lowest:")
for i in list_grades:
    print(spaces, round(i))

average_list = round(sum(list_grades) / len(list_grades), 1)

print(f"""
{name}'s Grade Summary:
{spaces}Total number of Grades: {num_grades}
{spaces}Highest grade: {round(max(list_grades))}
{spaces}Lowest grade: {round(min(list_grades))}
{spaces}Average: {average_list}
""")    

#Nueva varibale 
desire = float(input("What is your desired average? "))
key_grade = (desire * (num_grades+1)) - (sum(list_grades))
print(f"Good luck {name}!\nYou will need to get a {key_grade} on your next assignment to earn a {desire} average.")

print("Let's see what your average would've been if you did better/worse on an assignment.")
grade_change = float(input("What grade would you like to change: "))
new_grade = float(input(f"What grade would you like to change {grade_change} to: "))

#for loop para reemplazar la nota
for i in range(0, num_grades):
    if list_grades[i] == grade_change:
        list_grades[i] = new_grade

print("Grades Highest to Lowest:")
for i in list_grades:
    print(spaces, round(i))

new_average_list = round(sum(list_grades) / len(list_grades), 1)

print(f"""
{name}'s Grade Summary:
{spaces}Total number of Grades: {num_grades}
{spaces}Highest grade: {round(max(list_grades))}
{spaces}Lowest grade: {round(min(list_grades))}
{spaces}Average: {round(average_list, 1)}
""")    
print(f"""Your new average would be {new_average_list} compared to your real average of {average_list}!
That is a change of {round(new_average_list - average_list, 1)} points!

Too bad your original grades are still the same.
{list_grades}
You should go ask for extra credit.
""")

        
