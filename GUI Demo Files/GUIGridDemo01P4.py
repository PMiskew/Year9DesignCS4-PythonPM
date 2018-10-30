'''
PHASE 4:

In this Phase we will 
- create a counter and use it to only allow two buttons to be displayed at
  a time


'''
#tkinter is a module that holds all the function
#that let us easily make GUI elements
import tkinter as tk

#Control Variables

#By giving clicked a parameter that we can pass a value to
#we can check which button is clicked
def clicked(e, ctr):
	ctr = ctr + 1
	print(ctr)
	#check e with an if statement and set the appropriate button image
	if (e == 1):
		btn1.config(image = photoCheck)
	elif (e == 2):
		btn2.config(image = photoCheck)
	elif (e == 3):
		btn3.config(image = photoCheck)
	elif (e == 4):
		btn4.config(image = photoCheck)
#creating the main window.  To do this
#we need to call the Tk() funciton
root = tk.Tk()

ctr = 0

photoCheck= tk.PhotoImage(file="images/check.png")
photoX = tk.PhotoImage(file="images/x.png")
photoQuestion = tk.PhotoImage(file ="images/question.png")

label = tk.Label(root, text = "Welcome to Concentration!")
label.grid(row = 0, column = 0, columnspan = 2)


btn1 = tk.Button(root, image = photoQuestion, text = "1", command = ctr = lambda: clicked(1,ctr))
btn1.grid(row = 1, column = 0)

btn2 = tk.Button(root, image = photoQuestion, text = "2", command = ctr = lambda: clicked(2,ctr))
btn2.grid(row = 1, column = 1)

btn3 = tk.Button(root, image = photoQuestion, text = "3", command = ctr = lambda: clicked(3,ctr))
btn3.grid(row = 2, column = 0)

btn4 = tk.Button(root, image = photoQuestion, text = "4", command = ctr = lambda: clicked(4,ctr))
btn4.grid(row = 2, column = 1)

#This line displays the root and sets the program
#in an infinit loop.  This is an EVENT DRIVEN PROGRAM
root.mainloop()



