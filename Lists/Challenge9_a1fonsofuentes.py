import random

roster = []
roster_input = (input("Enter the last names of the players in the team, separated by a coma: ")).title()
roster1 = roster_input.split(", ")
roster.extend(roster1)

injured = random.choice(roster) #Usé el modulo random para que el programa escoja aleatoriamente quien se lesiona
new_player = (input(f"Yikes, {injured} got hurt. Who do you want to replace him with? ")).title()
roster.remove(injured)
roster.append(new_player)

print(f"The players who made it to the final roster are: {roster}\nGood luck to all of you, specially to {new_player}!")