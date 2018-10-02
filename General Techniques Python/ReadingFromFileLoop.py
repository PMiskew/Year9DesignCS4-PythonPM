f = open("data.txt", "r")

for lines in f:
	print("*")
	print(f.readline())

f.close()