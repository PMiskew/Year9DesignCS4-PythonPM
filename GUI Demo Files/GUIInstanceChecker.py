import tkinter as tk

def func1(event):

	print("FUNKY")
	print(event.widget)

root = tk.Tk()

btn = tk.Button(root,text = "I'm a Button")
btn.pack()
btn.bind("<Enter>",func1)

lab = tk.Label(root, text = "I'm a Label")
lab.pack()
lab.bind("<Enter>",func1)

root.mainloop()