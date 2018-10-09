#tkinter is a module (tool box) that
#holds code that you can use
#by using as tk we just are shortening the name
import tkinter as tk

def runme():
	print("Running")
	str = ent.get()

	strRev = ""

	for i in range(len(str) - 1, -1, -1):
		strRev = strRev + str[i]

	label.configure(text = strRev)
#root is a variable that holds the information
#about the main window.  That is the window
#with the close, min, max buttons in the top 
#left
#tk.Tk() go in the tk tool box and use the function Tk()
root = tk.Tk() 

#If we wan to better position the elements we use
#the grid geometry manager, not the pack
ent = tk.Entry(root)
ent.config(fg = "grey", text = "insert text")
ent.grid(row = 0, column = 0)

btn = tk.Button(root, text = "Press Me", command = runme)
btn.grid(row = 0, column = 1)



label = tk.Label(root, text = "...")
label.grid(row = 1, column = 0, columnspan = 2)




#sets up your program in an infinit loop waiting for
#the user to do somthing.  This is an EVENT DRIVE PROGRAM
#This means a function is called when we "do something"
root.mainloop()
