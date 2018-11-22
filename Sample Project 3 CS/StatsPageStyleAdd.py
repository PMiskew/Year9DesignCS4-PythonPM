import tkinter as tk
from tkinter import ttk
#Group Functions up here
def change():
	print("Change")

def clicked():
	print("clicked")
#Group Data Variables here!
names = ["Paul", "Francesco","Stephanie","Bill","Connor","Jihoo"]
stat1 = [1,2,3,4,5,6]
stat2 = [6,5,4,3,2,1]
stat3 = [1,3,2,5,4,6]





root = tk.Tk()



#Styles
ttk.Style().configure('green/black.TButton', foreground='green', bg = "black", height = 20, width = 20)


output = tk.Text(root, background = "#ffd0aa", height = 10, width = 50, font = ("Helvitica",16))
#output.config(state = "disable")
output.grid(row = 0, column = 0, columnspan = 2)

btnStat1 = ttk.Button(root, text = "Stat 1", style = 'green/black.TButton', command = clicked)
btnStat1.grid(row = 1, column =0, stick = "NESW")

btnStat2 = ttk.Button(root, text = "Stat 2", style = 'green/black.TButton', command = clicked)
btnStat2.grid(row = 2, column =0, sticky = "NESW")

btnStat3 = ttk.Button(root, text = "Stat 3", style = 'green/black.TButton', command = clicked)
btnStat3.grid(row = 3, column =0, sticky = "NESW")

MODES = [
("Ascending", "1"),
("Descending", "2")
]

v = tk.StringVar() #v keeps track of which button is selected. 
v.set("L") # initialize

for r in range(0,len(MODES),1):
	b = ttk.Radiobutton(root, text=MODES[r][0], variable=v, value=MODES[r][1], command = change)
	b.grid(row = 1 + r, column = 1, sticky = "W", padx = 40)

btnReduce = ttk.Button(root, text = "Reduce Data", style = 'green/black.TButton', command = clicked)
btnReduce.grid(row = 3, column = 1, sticky = "NESW")
root.mainloop()