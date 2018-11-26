import tkinter as tk

#VARIABLES
#Q:	How do I store data
#A:	Using a list and the append function is the way to go

#store all the passwords I generate 
password = [] #emprty list called password
#When I process I need to access each word
word1 = ""
word2 = ""
word3 = ""
outputStr = ""


#Step 1: I need to get the data from the fileds.
#To do this we add a button and we BIND a function

#FUNCTIONS
def submit():

	#Get values from entry boxes
	print("Submit Pressed")
	word1 = ent1.get()
	print(word1)
	word2 = ent2.get()
	print(word2)
	word3 = ent3.get()
	print(word3)

	#Build an output string
	#To make a new line we use an escape code 
	outputStr = "Word 1: "+word1+"\nWord 2: "+word2+"\nWord 3: "+word3

	print(outputStr)

	#outputs to the Text area outputStr
	output.config(state = "normal")
	output.insert(tk.END,outputStr)

	output.config(state = "disabled")



root = tk.Tk()


titleLabel = tk.Label(root, text = "PASSWORD GENERATOR", font=("Helvetica", 16))
titleLabel.grid(row = 0, column = 0, columnspan = 2)

output = tk.Text(root, height = 10, width = 50, background = "#F0F0F0")
output.config(state = "disable")
output.grid(row = 1, column = 0, columnspan = 2)


word1Label = tk.Label(root, text = "Word 1")
word1Label.grid(row = 2, column = 0, sticky = "NESW")

word2Label = tk.Label(root, text = "Word 2")
word2Label.grid(row = 3, column = 0)

word3Label = tk.Label(root, text = "Word 3")
word3Label.grid(row = 4, column = 0)

ent1 = tk.Entry(root)
ent1.grid(row = 2, column = 1)

ent2 = tk.Entry(root)
ent2.grid(row = 3, column = 1)

ent3 = tk.Entry(root)
ent3.grid(row = 4, column = 1)

btnGo = tk.Button(root, text = "GENERATE", command = submit)
btnGo.grid(row = 5, column = 0, columnspan = 2, sticky = "NESW")



root.mainloop() 


