import tkinter as tk


def execute():

	x = eval(ent.get())
	print(x)


root = tk.Tk()

ent = tk.Entry(root)
ent.pack()

btn = tk.Button(root,text = "Solve", command = execute)
btn.pack()


root.mainloop()