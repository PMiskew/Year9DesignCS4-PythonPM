#This program is a nice example of a core algorithm
#Remove Individual Digits
# To remove individual digits you use two operations
# 1 MOD:
	# mod return the remainder after division.  5%2 = 1.
	# If we mod by 10 we get the units digit. 723%10 = 3
# 2 Integer Division:
#	Integer division is when we divide and remove decimals;
#	we DO NOT round, simply cut them off. To integer divide 
# 	in Python we use //.  For example 723//10 = 72.  This is 
# 	a quick way to remove decimals. 

#Hi Nikhil
def findSum(n):
	s = 0	#store the sum of the values
	while (n > 0):
		x = n % 10 #chop off units digit store in x
		s = s + x #add unit digit to sum, stored in s
		n = n // 10 #remove unit digit from n
		
	return s

def isHarshad(n):

	if (n % findSum(n) == 0): #note that if a % b == 0 b is a factor of a
		return True
	return False


def findHarshad(low, high):
	low = 500
	high = 525
	streak = 0
	maxStreak = 0

	for i in range(low,high + 1,1):
		if (isHarshad(i)):
			streak = streak + 1;
		else:
			maxStreak = max(streak,maxStreak)
			streak = 0;
		#print(i,streak) #Test code for debugging

	maxStreak = max(streak,maxStreak)
	print(maxStreak)

f = open("DwiteHarshadNumbersData.txt", "r")
for line in f:
	l = f.readline()
	h = f.readline()
	findHarshad(l,h)

f.close()
