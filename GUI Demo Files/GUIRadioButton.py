import tkinter as tk

def change():
	print("change")
	print(v.get()) #Accesses element associated with MODES

root = tk.Tk()

MODES = [
("Monochrome", "1"),
("Grayscale", "L"),
("True color", "RGB"),
("Color separation", "CMYK"),
]

v = tk.StringVar() #v keeps track of which button is selected. 
v.set("L") # initialize

for text, mode in MODES:
	b = tk.Radiobutton(root, text=text, variable=v, value=mode, command = change)
	b.pack(anchor=tk.W)

root.mainloop()