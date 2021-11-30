def Favorite_teacher_program():
    print("\tWelcome to the Favorite Teachers Program")
    fav_teachers = []

    for i in range(1,5):
        teacher = input(f"\tWho is your number {i} favorite teacher:\t")
        fav_teachers.append(teacher)
#Creamos la función arriba.
#Creamos f prints junto con sorted para probarlo.
    print(f"\nYour favorite teachers ranked are: {fav_teachers}")
    print(f"Your favorite teachers alphabetically order are: {sorted(fav_teachers)}")
    print(f"Your favorite teachers in reverse alphabetically order are: {sorted(fav_teachers, reverse=True)}")
    print(f"Your top two teachers are: {fav_teachers[:2]}")
    print(f"Your next two teachers are: {fav_teachers[2:4]}")
    print(f"Your last favorite teacher is: {fav_teachers[len(fav_teachers)-1]}")
    print(f"Your have a total of 4 favorite teachers.")
    print(f"Oops, {fav_teachers[0]} is no longer your favorite teacher.")

    new_teacher  = input("\tWho is your new FAVORITE teacher:\t")

    fav_teachers.insert(0,new_teacher)
    print(f"\nYour top two teachers are: {fav_teachers[:2]}")
    print(f"Your next two teachers are: {fav_teachers[2:4]}")
    print(f"Your last favorite teacher is: {fav_teachers[len(fav_teachers)-1]}")
    print(f"Your have a total of 5 favorite teachers.\n")

    print(f"You've decided you no longer like a teacher.")

    removed_teacher  = input("\tWhich teacher would you like to remove from your list:\t")

    fav_teachers.remove(removed_teacher)
    print(f"\nYour favorite teachers ranked are: {fav_teachers}")
    print(f"Your favorite teachers alphabetically order are: {sorted(fav_teachers)}")
    print(f"Your favorite teachers in reverse alphabetically order are: {sorted(fav_teachers, reverse=True)}")
    print(f"Your top two teachers are: {fav_teachers[:2]}")
    print(f"Your next two teachers are: {fav_teachers[2:4]}")
    print(f"Your last favorite teacher is: {fav_teachers[len(fav_teachers)-1]}")
    print(f"Your have a total of 4 favorite teachers.")

#Ejecuto la función
Favorite_teacher_program()