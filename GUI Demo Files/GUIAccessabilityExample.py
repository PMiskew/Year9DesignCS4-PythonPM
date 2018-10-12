import tkinter as tk

def changeStateContrast(*args):
	print("Change Contrast")
	print(var1.get())
	if var1.get() == 1:
		root.config(bg = "black")
		cbox1.config(bg = "black", fg = "yellow")
		cbox2.config(bg = "black", fg = "yellow")
	if var1.get() == 0:
		root.config(bg = "white")
		cbox1.config(bg = "white",fg = "black")
		cbox2.config(bg = "white",fg = "black")

def changeStateFont(*args):
	print("changed font")
	print(var1.get())
	if var2.get() == 1:
		cbox1.config(font=("Courier", 44))
		cbox2.config(font=("Courier", 44))

	if var2.get() == 0:
		cbox1.config(font=("Courier", 20))
		cbox2.config(font=("Courier", 20))

root = tk.Tk()

var1 = tk.IntVar()
cbox1 = tk.Checkbutton(root, text="High Contrast", variable=var1)
cbox1.config(font=("Courier", 20))
var1.trace("w",changeStateContrast)
cbox1.pack(fill = "both")

var2 = tk.IntVar()
cbox2 = tk.Checkbutton(root, text="Large Font", variable=var2)
cbox2.config(font=("Courier", 20))
var2.trace("w",changeStateFont)
cbox2.pack(fill = "both")






root.mainloop()
