relation1 = input("What is the first family relation: ")
relation2 = input("What is the second family relation:")
crelation = ""

#relation1.lower() creates a lower case version. This means
#you don't have to check Dad, dad, DaD etc
if relation1.lower() == "dad":
	print("relation 1 is dad")
	crelation = "baba"

if relation2.lower() == "mom":
	print("relation 2 is mom")
	crelation = crelation + " mama"

if relation1.lower() == "mom":
	print("relation 1 is dad")
	crelation = "mama"

if relation2.lower() == "dad":
	print("relation 2 is mom")
	crelation = crelation + " baba"

print(crelation)