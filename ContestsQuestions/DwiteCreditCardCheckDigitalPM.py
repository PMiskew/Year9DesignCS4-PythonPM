sum = 0
ctr = 0
number = 49927398716
strNum = str(number)



while (number > 0):
	x = number%10
	if (ctr % 2 == 0):
		while (x > 1):
			print("A:",x)
			sum = sum + x % 10
			x = x // 10

	else:
		print(x)
		sum = sum + x

	ctr = ctr + 1
	number = number // 10




print(sum) 