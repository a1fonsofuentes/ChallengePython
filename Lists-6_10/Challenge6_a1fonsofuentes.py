g1 = float(input("What is your first grade? (0-100): " )) #Pedimos los inputs
g2 = float(input("What is your second grade? (0-100): "))
g3 = float(input("What is your third grade? (0-100): "))
g4 = float(input("What is your fourth grade? (0-100): "))
 
 #unimos todo a la lista vacía
notas = []
notas.append(g1)
notas.append(g2)
notas.append(g3)
notas.append(g4)

#printeamos los datos.
print(f"Your grades are: {notas}")
notas = sorted(notas, reverse = True)
print(f"Your grades from highest to lowest are: {notas}")

print("The lowest two grades will now be dropped.")
print(f"Removed grade: {notas.pop(2)}\nRemoved grade: {notas.pop(2)}")
#Ponemos la posición dos ambas veces porque al eliminar el primero, el segundo se vuelve el 2.

print(f"Your remaining grades are: {notas}\nNice work! Your highest grade is {notas[0]}")
