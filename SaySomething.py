import os

#Loop Structure
#Two types of loops and you can use any type in any
#situation
# Counted loops: We know in advance how many times
#				 something should run. 
#				 for loops
# Conditional loops: We don't know how many times
#					 somethign will run before entering
#					 the loop
#					 while loops
while (True):
	statement = input("What would you like me to say: ")
	os.system("say "+statement)
