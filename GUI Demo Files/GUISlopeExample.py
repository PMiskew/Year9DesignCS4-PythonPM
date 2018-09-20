#This is an example of a slope calculator as 

import tkinter as tk

def calculate(*args):

	print("Calculating")

	x1 = ex1.get()
	y1 = ey2.get()
	x2 = ex2.get()
	y2 = ey2.get()

	print(x1)
#FIX ERROR

root = tk.Tk()

lx1 = tk.Label(root,text = "x1", padx = 10, pady = 10)
ex1 = tk.Entry(root, padx = 10)

ly1 = tk.Label(root,text = "y1", padx = 10, pady = 10)
ey1 = tk.Entry(root, padx = 10)

lx2 = tk.Label(root, text = "x2", padx = 10, pady = 10)
ex2 = tk.Entry(root, padx = 10)

ly2 = tk.Label(root,text = "y2", padx = 10, pady = 10)
ey2 = tk.Entry(root, padx = 10)

submitBtn = tk.Button(root, text = "Submit", command = calculate)

result = tk.Text(root, width = 20, height = 20, borderwidth=3, relief=tk.GROOVE)
result.config(state = "disabled")

lx1.pack()
ex1.pack()

ly1.pack()
ey1.pack()

lx2.pack()
ex2.pack()

ly2.pack()
ey2.pack()

submitBtn.pack()
result.pack()



root.mainloop()



