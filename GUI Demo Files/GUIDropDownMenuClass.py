import tkinter as tk

class Display:

	def __init__(self):
		print("Constructing Object")
		self.root = tk.Tk()

		self.OPTIONS = ["eggs","bunny","chicken"]

		self.var = tk.StringVar(self.root)
		self.var.set(self.OPTIONS[1])
		self.var.trace("w",self.change)


		self.dropDownMenu = tk.OptionMenu(self.root,self.var, self.OPTIONS[0],self.OPTIONS[1],self.OPTIONS[2])
		self.dropDownMenu.pack()


		self.root.mainloop()

	def change(self, *args):
			print("changing")
			print(self.var.get())






display1 = Display() 
