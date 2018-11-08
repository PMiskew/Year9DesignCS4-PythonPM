import random
result = []
#Part 1:
for i in range(0,5,1):
	for j in range(0,100,1):
		result.append(random.randint(1,6))

print(result)
#Part 2:
biasCheck = [0,0,0,0,0,0]


for i in range(0,len(result),1):
	biasCheck[result[i] - 1] = biasCheck[result[i] - 1] + 1
#Not Efficent (BAD CODE- GOOD LEARNING)
'''
tolerance = 20
bias = False
for i in range(0, len(biasCheck),1):
	for j in range(i+1, len(biasCheck),1):
		if abs(biasCheck[i] - biasCheck[j]) > tolerance:
			bias = True

print(biasCheck)
print(bias)
total = 0

#'''

#Good Code:
for i in range(0,len(biasCheck),1):
	total = total + biasCheck[i]

print(total/6)


