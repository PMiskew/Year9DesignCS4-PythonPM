import random
import time

list = ["NI","RN","AJ","MC","NM"]
print(list)
time.sleep(0.5)
for i in range(0,random.randint(10,50),1):
	
	x = random.randint(0,len(list) - 1)
	y = random.randint(0,len(list) - 1)

	temp = list[x]
	list[x] = list[y]
	list[y] = temp
	print(list)
	time.sleep(0.5)

print(list)


