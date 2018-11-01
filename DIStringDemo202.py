#INPUT

#Step 1 Take input for first name
fName = input("Input First Name: ")
#Step 2 Take input for last name
lName = input("Input Last Name: ")

#Process
#Step 1: Lower Case everything
fName = fName.lower()
lName = lName.lower()
#Step 2: Construct User Name
userName = fName[0] + lName
#Step 3: Reverse User Name
#Step 3.0 Create empty String
newUserName = "" #Create empty String
#Step 3.1 Loop from last index to 0 and add each letter to newUserName
#Example: 
#			 0123456
# useName = "pmiskew"
#
# Loop from i = 6 to i = 0
# The i has to start at the length - 1
# The loop has to go as long as i > -1
# 
#Concept: String construction is the process of adding strings
#		  together to make new strings
for i in range(len(userName) - 1, -1,-1):
	newUserName = newUserName + userName[i]


#Step 3.2 The first character is lower case
#		  we need to pull it out and uppercase it
newUserName = newUserName[0].upper() + newUserName[1:len(newUserName)]
#Output
print(newUserName)