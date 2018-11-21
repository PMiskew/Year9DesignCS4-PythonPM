

provincesns = [
"BRITISHCOLUMBIA",
"ALBERTA",
"SASKATCHEWAN",
"MANITOBA",
"ONTARIO",
"QUEBEC",
"NOVASCOTIA",
"NEWFOUNDLAND",
"NEWBRUNSWICK",
"PRINCEEDWARDISLAND"
]

provinces = [
"BRITISH COLUMBIA",
"ALBERTA",
"SASKATCHEWAN",
"MANITOBA",
"ONTARIO",
"QUEBEC",
"NOVA SCOTIA",
"NEWFOUNDLAND",
"NEW BRUNSWICK",
"PRINCE EDWARD ISLAND"
]

testCases = [
	"For the best value in food and amusements, ask at Chew and View",
	"The protesters are prepared to confront a riot squad.",
	"Should I jump on to the red target, or on the blue one?"	
]

str = testCases[1]
#Step 1: Remove punctuation - How could I handle all puncuation?
str = str.replace(" ","")
str = str.replace(".","")
str = str.replace(",","")
str = str.replace("!","")
str = str.replace("?","")
str = str.upper()
print(str)

results = []
for i in range(0,len(provincesns),1):
	#A try structure is designed to hold code that might result in a RunTime error.  
	#A RunTime error is an error where the code is running and it crashes
	#Three borad Errors types are, 
	#	RunTime - Starts running and crashes
	#	Syntax - Won't run because error in code
	#	Logic - Runs completly but incorrectly (acircle = 2*r)
	#
	# We add to a structure an except structure.  This is like your elseif.  What this means is that if the 
	# program hits a runTime error it just jumps to the except code. 
	try:

		#In Java the index function returns -1 if the substring isn't found. 
		# "Paul".index("au") --> 1
		# "Paul".index("zzz") -- -1 in Java but a ValueError in Python
		results.append(str.index(provincesns[i]))
	except ValueError:
		results.append(300) #I chose 300 instead -1 because of the final processing step. 

print(results)

#When performing a linear search (look at each element in sequence for what you are looking for) to find
#max or min value, ALWAYS SET MAX/MIN to an element in the list. 
smallestIndex = results[0]
smallestIndexLoc = 0
for i in range(0, len(results), 1):
	if smallestIndex > results[i]:
		smallestIndex = results[i]
		smallestIndexLoc = i

print(smallestIndex)
print(smallestIndexLoc)

if smallestIndex < len(provinces):
	print(provinces[smallestIndexloc])
else:
	print("NO PROVINCE FOUND")






