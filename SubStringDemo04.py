#This program will show how to effectivly use substring
#Prompt the User for their first name and their last name

#Input
fName = input("What is your first: ")
lName = input("What is your last name: ")

#Process
result = fName[0] + "." + lName
#Create a code name by using letters of their first and last name
lenlName = len(lName) #Generate the length of last name
codeName = fName[0] + fName[1] + fName[2] + "." + lName[2] + lName[4]


#Output
print("Hi "+result)
print("Your code name is: "+codeName)