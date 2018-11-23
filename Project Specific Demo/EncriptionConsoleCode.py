def encryptionMode(encryptionAlgorithm):
	modeInput = input("What would you like to do? ")

	return modeInput

def shiftSelect(shift):
	

	shiftInput = -26 #initalize shift input to an invalid input


	while shiftInput > 25 or shiftInput < -25:

		#I have cast here instead as in this case I only have to do 
		#it once
		shiftInput = int(input("What is your shift? "))

		#I want it to restart from the top of this function is these conditions are made.
		#If this condition is not met, then it returns the shift.
		#I will use this in the function that is specific for each algorithm.
			#Solution:
			#You want to put it in a loop.  You could do this a variety of ways
			#We need to know more about what you want to return. I am going to assume
			#that you want to do something with this function after the shiftinput is
			#taken

		if shiftInput > 25 or shiftInput < -25:
			print("Try Again")

	print("Out of loop") #Just to show you have exited loop


#You have to actually call the function
shiftSelect(9)

#One other question, should I use a different class for each algorithm?
#So depending on the requested algorithm and the requested shift(if appliable)
#Then it would run a specific class etc. (Is that the best use of the class?)

	#Comment:  
	#Note that you would not create a class for each encription algorithm. 
	#What you might do is create a Message class that contains a string as 
	#a field that stores the message.  Then you would have the encription 
	#algorithms as methods (behviours) that you apply. 