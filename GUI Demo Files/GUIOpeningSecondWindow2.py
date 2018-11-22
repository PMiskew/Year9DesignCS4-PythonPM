import tkinter as tk


def entry(ent):
	list.append("test")
	print(ent.get())

def entryWindow():
	eroot = tk.Tk()
	ent = tk.Entry(eroot)
	ent.pack()
	ebtn = tk.Button(eroot,text="Submit",command=lambda:entry(ent))
	ebtn.pack()
	eroot.mainloop()


list = []
root = tk.Tk()

btn = tk.Button(root, text = "Press Me", command = entryWindow)
btn.pack()

root.mainloop()


