list = [

	[1,2,3],
	[4,5,6],
	[7,8,9],
	[10,11,12]


]

#A multi-dimensional list is a list of lists. 
#For a 2D list you can pull out a row using the single
#[] notation

print(list[0]) #prints [1,2,3]
print(len(list[0])) #prints 3, the lenght of that row. 

#If we, for example, wanted to find the sum of the elements of
#this list of intergers we have to look at each element and pull
#out the value and add it to sum

sum = 0

for r in range(0,len(list),1):
	for c in range(0,len(list[r]),1):
		sum = sum + list[r][c]

print(sum)
