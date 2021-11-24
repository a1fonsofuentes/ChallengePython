from datetime import datetime, date

shopping = ["meat", "cheese"]
new = input("Add three new items to the list separated by a coma: ")
new_items = new.split(", ")
shopping.extend(new_items)
#Creé la variable new y metí un input ahí. despues creé la variable new_items para crear una lista con el input de new
#Después junté la nueva lista con la lista de shopping.

ciao = input("Which item you just purchased? ")
shopping.remove(ciao)

ciao1 = input("Which item you just purchased? ")
shopping.remove(ciao1)

ciao2 = input("Which item you just purchased? ")
shopping.remove(ciao2)

new1 = input(f"Sorry, the store is out of {shopping.pop(1)}. Which other item would you like to purchase instead? ")
shopping.append(new1) #usamos pop para que se muestre en la pantalla

print(f"The final version of your grocery list looks like this: {shopping}")
print(f"\n{date.today().month}/{date.today().day} {datetime.today().hour}:{datetime.today().day}")