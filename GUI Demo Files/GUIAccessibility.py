import tkinter as tk


colorshm1bg = "red"
def change():
	print("In change")
	if checkVar1.get() == 1:
		for i in range(0,len(widget),1):
			widget[i].config(background = "blue")
	else:
		for i in range(0,len(widget),1):
			widget[i].config(background = "red")
	
root = tk.Tk()
widget = []
#variables
checkVar1 = tk.IntVar()
checkBox1 = tk.Checkbutton(root, var = checkVar1, text = "High Contrast", background = colors[0], command = change)
widget.append(checkBox1)
checkBox1.pack()

entry1 = tk.Entry(root, background = colorshm1bg)
entry1.pack()
widget.append(entry1)

label1 = tk.Label(root, text = "I am a label", background = colors[0])
label1.pack()
widget.append(label1)

root.mainloop()

