
#Parallel lists are lists that are designed to share common information in an index
#Let's image a game where there are weapons that have damage and defense options

weapon = ["sword","gun","sheild"]
attack = [65,95,30]
defense = [65,10,95]

value = 1

while value != -1:
	print("1: Sword")
	print("2: Gun")
	print("3: Sheild")
	
	value = int(input("What option do you want?"))

	print("You chose "+weapon[value - 1])
	print("Attack: ",attack[value - 1])
	print("Defense: ",defense[value - 1])

print("DONE")