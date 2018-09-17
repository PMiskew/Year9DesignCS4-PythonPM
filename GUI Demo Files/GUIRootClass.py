#Accessing tkinter module and us tk to call it
import tkinter as tk 
#class is a blueprint and object is an instance of a class

class Display:

	def __init__(self):
		#Setup our GUI

		print("Running Constructor")
		self.root = tk.Tk()

		#Step 1: Create an instance of the widget
		self.labelx1 = tk.Label(self.root,text="x1")
		self.entryx1 = tk.Entry(self.root)

		#Step 2: Pack the widget
		self.labelx1.pack()
		self.entryx1.pack()

		#use a normal pack
		#use a grid layoumanager




		self.root.mainloop()
		print("DONE")


d = Display() #constructors a display object


