a = int(input(""))
w1 = input("")
w2 = input("")

ctr = 0

for i in range(1,len(w1),1):
	if (w1[i] == w2[i]):
		ctr = ctr + 1

print(ctr)