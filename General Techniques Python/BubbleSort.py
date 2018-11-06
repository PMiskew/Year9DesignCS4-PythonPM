

list = [6,5,4,1,2]

for j in range(0, len(list),1):
	for i in range (0,len(list) - j - 1, 1):
		if list[i] > list[i + 1]:
			temp = list[i]
			list[i] = list[i + 1]
			list[i + 1] = temp
			print("     ",list)
	print(list)

print(list)

