import tkinter as tk

def change():
	print("Change")
root = tk.Tk()

OPTIONS = ["Player 1","Player 2","Player 3",]#Create our list that holds all the players
var = tk.StringVar(root) #keeps track of what the dropdown menu has selected
var.set(OPTIONS[0]) #Sets the var to our first element in the list
var.trace("w",change) #What a trace does it when every there is a write chane to var it runs change 


dropDownMenu = tk.OptionMenu(root,var, OPTIONS[0],OPTIONS[1],OPTIONS[2])
dropDownMenu.grid(row = 0, column = 0, columnspan = 2)

canvas = tk.Canvas(root, height = 300, width = 200, background = "black")
canvas.grid(row = 1, column = 0,columnspan = 2)

submitBtn = tk.Button(root, text = "Submit")
submitBtn.grid(row = 2, column = 0)

rapidBtn = tk.Button(root, text = "Rapid")
rapidBtn.grid(row = 2, column = 1)
root.mainloop()