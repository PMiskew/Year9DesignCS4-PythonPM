import tkinter as tk
from PIL import ImageTk, Image

def clicked(*args):
	print("Running")
	filectr = filectr + 1
	path = "images/"+files[filectr]
	img = ImageTk.PhotoImage(Image.open(path))
	panel.confgure(image = img)

#This creates the main window of an application
window = tk.Tk()
window.title("Join")
window.geometry("600x830")
window.configure(background='grey')
filectr = 0
files = ["1_Hydrogen.jpg","2_Helium.jpg","3_Lithum.jpg","4_Beryllium.jpg","5_Boron.jpg"]
path = "images/"+files[filectr]

#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img = ImageTk.PhotoImage(Image.open(path))

#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = tk.Label(window, image = img)

#The Pack geometry manager packs widgets in rows or columns.
panel.pack()

btn = tk.Button(window, text = "NEXT", command = clicked)
btn.pack(side = "bottom", fill = "both", expand = "yes")

#Start the GUI
window.mainloop()