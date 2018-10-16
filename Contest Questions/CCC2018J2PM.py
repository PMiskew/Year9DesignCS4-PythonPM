a = int(input(""))
w1 = input("")
w2 = input("")

ctr = 0

for i in range(1,len(w1),1):
	if (w1[i] == "C" and w2[i] == "C" ):
		ctr = ctr + 1

print(ctr)