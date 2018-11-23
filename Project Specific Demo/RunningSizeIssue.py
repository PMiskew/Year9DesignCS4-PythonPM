#This imports the tkinter "Tool box" that contains
#All the support material to make GUI elements.
#by including "as tk"we are giving a short name to use.
import tkinter as tk




root = tk.Tk()
#Three stages to build elements/objects
#1. Construct the object: We build and configure it.
#2. COnfigure the object: We specufy behaviours and settings (OPTIONAL)
#3. Pack the object: Put it in the window
titleLabel = tk.Label(root, text = "Your Daily Running Tracker", font=("Helvetica", 16))
#ordered parameters: The order we send the matters. (COMMON)
#Named parameters: JavaScript and Python specific
titleLabel.grid(row = 0, column = 0, columnspan = 2)

#Widget 2: Text *********************
output = tk.Text(root,background = "grey", font=("Helvetica", 16))
output.grid(row = 1, column = 0, columnspan = 2, sticky = "NESW")
#Height = Lines up and down, Width = characters across
output.insert(tk.END,"Welcome to your daily running tracker! Before you begin, you need to input some facts about you.")


#Widget 3: Labels ********************
word1Label = tk.Label(root, text = "Height (Feet)", background = "red", foreground = "white")
word1Label.grid(row = 2, column = 0, sticky = "NESW", padx = 30, pady = 30)

word2Label = tk.Label(root, text = "Weight (Kg)", background = "red", foreground = "white")
word2Label.grid(row = 6, column = 0, sticky = "NESW", padx = 30, pady = 30)

word3Label = tk.Label(root, text = "Age (Years)", background = "red", foreground = "white")
word3Label.grid(row = 8, column = 0, sticky = "NESW", padx = 30, pady = 30)

contrast = tk.IntVar()
check1 = tk.Checkbutton(root, text="High Contrast On/Off", variable=contrast)
check1.grid()

#Widget 4: Entry ***********************

ent1 = tk.Entry(root)
ent1.grid(row = 2, column = 1, sticky = "EW")

ent2 = tk.Entry(root)
ent2.grid(row = 6, column = 1)

ent3 = tk.Entry(root)
ent3.grid(row = 8, column = 1)

btnGo = tk.Button(root, text = "Input Data")
btnGo.grid(row = 9, column = 1)




#We are writing an EVENT DRIVEN PROGRAM
#Build the GUI
#Start it running
#Wait for "EVENT"
root.mainloop() #Starts the program