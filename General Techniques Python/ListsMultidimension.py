#You can also create multi dimensional lists

list1D = [1,2,3]

for i in range(0, len(list1D),1):
	print(list1D[i])

list2D = [
[1,"A"],
[2,"B"],
[3,"C"],]

#To access 2D I need a row and a column
print(list2D[0][1])
print(list2D[2][0])
print(list2D[1])
