#Reading from files is not technically tricky, but
#does present some problems if you don't consider the
#design of the file.  You must know exactly what the 
#file looks like and recognize that spaces and enters
#at the end of the file impact the process.  

f = open("data.txt", "r")

content = f.read() #read the entire file in one go
print(content) 
f.close()

f = open("data.txt", "r")
print("**************")
line1 = f.readline()
line2 = f.readline()
line3 = f.readline()
print(line1+""+line2+""+line3)
