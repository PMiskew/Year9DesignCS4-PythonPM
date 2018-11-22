import tkinter as tk

#Classes: A blueprint to make objects. 
#Object: An instance of the class. 
#Three parts
#Constructor:  This is special method only run once when we first instantiate "Make" the object
#Attributes: These are variables that describe the state of the object. 
#Behaviours: These are functions that can be called that deal with the object. 

class LoginPage():

	#The first thing is always the constructor all the code that 
	#you write now will be put in the constructor
	def __init__(self):
		print("Running Constructor")
		#all variables are to instance variables
		self.root = tk.Tk()
		
		self.labUN = tk.Label(self.root, text = "User Name", font = ("Ariel",20))

		self.labUN.pack()

		self.entUN = tk.Entry(self.root)
		self.entUN.pack(padx = 10)

		self.labPassword = tk.Label(self.root, text = "Password")
		self.labPassword.pack()

		self.entPassword = tk.Entry(self.root, show = "*")
		self.entPassword.pack()

		self.btnSubmit = tk.Button(self.root, text = "Submit",command = self.clicked)
		self.btnSubmit.pack()

		self.root.mainloop()

	def clicked(self):
		print("clicked")




mainpage = LoginPage() #Creates an instance of the class



