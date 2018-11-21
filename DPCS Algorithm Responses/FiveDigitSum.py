def genList(n):

	list = []

	for i in range(1,n+1,1):
		list.append(i)

	return list

def genPossibleValues(list):

	gList = []
	
	for j in range(0,len(list),1):
		for i in range(1,len(list),1):
			temp = list[i]
			list[i] = list[i - 1]
			list[i - 1] = temp
			gList.append(genNum(list))

	return gList

def genNum(list):

	nstr = ""
	for i in range(0,len(list),1):
		nstr = nstr + str(list[i])

	return int(nstr)


print(genList(9))
list = genList(9)
list = genPossibleValues(list)
print(list)


