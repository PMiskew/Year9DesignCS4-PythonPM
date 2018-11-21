
def sum(number):

	sum = 0
	ctr = 0
	strNum = str(number)



	while (number > 0):
		
		x = number%10

		if (ctr % 2 == 1):
			x = x * 2
			while (x > 0):
				sum = sum + x % 10
				x = x // 10
		else:
			sum = sum + x

		ctr = ctr + 1
		number = number // 10

	return sum

def isValid(number):

	total = sum(number)
	if (total%10 == 0):
		return "Valid"
	else:
		return "Invalid"

fin = open("DwiteCreditCardCheckDigitalData.txt","r")
fout = open("DwiteCreditCardCheckDigitalDataOut.txt","w")

for aline in fin:

	print(fin.readline())