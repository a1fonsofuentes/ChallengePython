name = input("What is your name? ") #pedimos el nombre de la persona
print(f"Hi {name}! I will be counting the amount of times a letter appears on a message.")
message = (input("Please enter a message: ")).lower() #pedimos el mensaje y lo guardamos en una variable
letter = (input("Which letter do you want to count? ")).lower() #pedimos la letra que quiera contar.
count = message.count(letter) #usamos la función para calcular la cuenta y lo guardamos en una nueva variable
print(f"{name}, your message has {count}'s in it.") #printf para imprimir.