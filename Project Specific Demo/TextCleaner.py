import tkinter as tk


root = tk.Tk()


levelLab = tk.Label(root, text = "LEVELS")
levelLab.grid(row = 0, column = 0)

customLab = tk.Label(root, text = "CUSTOM", font = ("Arial, 20"))
customLab.grid(row = 0, column = 1, columnspan = 2)

cleanCheck = tk.Checkbutton(root, text = "Clean")
cleanCheck.grid(row = 1, column = 0)

cust1Rem = tk.Entry(root)
cust1Rem.grid(row = 1, column = 1)

cust1Rep = tk.Entry(root)
cust1Rep.grid(row = 1, column = 2)

root.mainloop()