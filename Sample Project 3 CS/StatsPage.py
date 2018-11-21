import tkinter as tk


root = tk.Tk()

output = tk.Text(root, background = "blue", height = 10, width = 50, font = ("Helvitica",16))
#output.config(state = "disable")
output.grid(row = 0, column = 0, columnspan = 2)

btnStat1 = tk.Button(root, text = "Stat 1")
btnStat1.grid(row = 1, column =0, stick = "NESW", padx = 10, pady = 10)

btnStat2 = tk.Button(root, text = "Stat 2")
btnStat2.grid(row = 2, column =0, padx = 10, pady = 10)

btnStat3 = tk.Button(root, text = "Stat 3")
btnStat3.grid(row = 3, column =0)




root.mainloop()