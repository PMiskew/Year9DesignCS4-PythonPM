import os

#We use the input function to take an input
#We have to have an asssignment statement to store an input

#input is a function.  It runs a small program that 
#causes the computer to stop and wait for input
fName = input("What is your fist name: ")
lName = input("What is your last name: ")

print("Hi, "+fName+" "+lName)

initialName = fName[0] + " . " + lName #adding strings is concatination 
print("Hi, "+initialName)

os.system("say "+fName+" "+lName)