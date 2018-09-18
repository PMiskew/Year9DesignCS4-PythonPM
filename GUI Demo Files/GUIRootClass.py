#Accessing tkinter module and us tk to call it
import tkinter as tk 
#class is a blueprint and object is an instance of a class

class Display:

	def __init__(self):
		#Setup our GUI

		print("Running Constructor")
		self.root = tk.Tk()

		self.root.mainloop()
		print("DONE")


d = Display() #constructors a display object


