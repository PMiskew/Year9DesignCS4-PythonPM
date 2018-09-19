#Attributes and Behaviours
import os
import tkinter as tk 	#tkinter is a module that stores
						#built in functions to create
						#GUI interfaces. 


class Display:

	#Constructor: Is a special method called only once
	#when I instantiate (create) the object for the first
	#time. 
	def __init__(self):

		print("Running display constructor")
		#instance variables in python are self.<variable name>
		self.root = tk.Tk() #Tk is the constructor that builds a basic window

		#To add elements we have to construct them then pack them
		#constructs elements
		self.ent = tk.Entry(self.root)
		self.btn = tk.Button(self.root, text = "Speak", command=self.runMe)

		#pack elements: Pack is the most basic geometry manager
		self.ent.pack()
		self.btn.pack()

		self.root.mainloop()
		print("program end")

	def runMe(self):
		print("Running")
		statement = self.ent.get()
		os.system("say "+statement)



#Start of program
d = Display() #Creates a display object called d.  It runs the 
			  #constructor
