'''
PHASE 2:

In this Phase we will 
- place a standar image on each of the buttons 


'''
#tkinter is a module that holds all the function
#that let us easily make GUI elements
import tkinter as tk

#creating the main window.  To do this
#we need to call the Tk() funciton
root = tk.Tk()



photoCheck= tk.PhotoImage(file="images/check.png")
photoX = tk.PhotoImage(file="images/x.png")
photoQuestion = tk.PhotoImage(file ="images/question.png")

label = tk.Label(root, text = "Welcome to Concentration!")
label.grid(row = 0, column = 0, columnspan = 2)


btn1 = tk.Button(root, image = photoQuestion, text = "1")
btn1.config(relief = tk.RAISED)
btn1.grid(row = 1, column = 0)


btn2 = tk.Button(root, image = photoQuestion, text = "2")
btn2.grid(row = 1, column = 1)

btn3 = tk.Button(root, image = photoQuestion, text = "3")
btn3.grid(row = 2, column = 0)



btn4 = tk.Button(root, image = photoQuestion, text = "4")
btn4.grid(row = 2, column = 1)

#This line displays the root and sets the program
#in an infinit loop.  This is an EVENT DRIVEN PROGRAM
root.mainloop()



