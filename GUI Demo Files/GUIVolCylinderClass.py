import tkinter as tk
import math

class CylinderCalc:

	def __init__(self):


		self.root = tk.Tk();
		self.root.title("Cylinder Calc")

		self.labr = tk.Label(self.root, text="radius:")
		self.labr.pack()

		self.entr = tk.Entry(self.root)
		self.entr.pack()

		self.labh = tk.Label(self.root, text="height")
		self.labh.pack()

		self.enth = tk.Entry(self.root)
		self.enth.pack();

		self.btn = tk.Button(self.root, text="Calculate", command=self.calculate)
		self.btn.pack()

		self.output = tk.Text(self.root, height = 10, width=50, borderwidth=3, relief=tk.GROOVE)
		self.output.config(state="disabled")
		self.output.pack()

		self.root.mainloop()


	def calculate(self):
			print("caluclating")

			r = float(self.entr.get())
			h = float(self.enth.get())

			v = math.round(math.pi*r*r*h,2);

			self.output.config(state="normal")

			outputValue = "Given\nradius:"+str(r)+" units\nheight:"+str(h)+" units\nThe volume is:"+str(v)+" units cubed\n"

			self.output.delete(1.0,tk.END)
			self.output.insert(tk.INSERT,outputValue)
			self.output.config(state="disabled")
			print(v)




calc = CylinderCalc();
