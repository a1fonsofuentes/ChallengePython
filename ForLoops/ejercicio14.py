n = int(input("Ingresa un numero :"))
a = 0 
b = 1
sum = 0 
count = 1

while (count<= n):
    print( sum,end = "")
    # el comando end va a hacer print de la suma y terminar con un espacio.
    # es un parametro de print.
    count += 1
    a = b
    b = sum 
    sum = a +b
    