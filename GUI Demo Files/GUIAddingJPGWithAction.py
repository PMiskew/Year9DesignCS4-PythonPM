import tkinter as tk
from PIL import ImageTk, Image
import random

#This is the first time we are forced to setup a class structure
#The reason is that it is hard to manage the variables
class Program:

	def __init__(self):

		#This creates the main window of an application
		self.root = tk.Tk()
		self.root.title("Image Cycling")
		self.root.geometry("600x880")
		self.root.configure(background='grey')
		self.filectr = 0
		self.files = ["1_Hydrogen.jpg","2_Helium.jpg","3_Lithium.jpg","4_Beryllium.jpg","5_Boron.jpg"]
		self.path = "images/"+self.files[self.filectr]

		#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
		self.img = ImageTk.PhotoImage(Image.open(self.path))

		#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
		self.panel = tk.Label(self.root, image = self.img)

		#The Pack geometry manager packs widgets in rows or columns.
		self.panel.pack()

		self.btnNext = tk.Button(self.root, text = "NEXT", command = self.clickedNext)
		self.btnNext.pack(fill = "both", expand = "yes")


		self.btnRandom = tk.Button(self.root, text = "RANDOM", command = self.clickedRandom)
		self.btnRandom.pack(fill = "both", expand = "yes")

		#Start the GUI
		self.root.mainloop()
	#This method is called when the next button is selected
	#it access the next image in the sequence
	def clickedNext(self):
		#A great use of MOD
		#Run the program with line 1 and you run into a problem
		#self.filectr = self.filectr + 1 #LINE 1
		#Run the program with line 2 and mod makes things work
		self.filectr = (self.filectr + 1)%len(self.files)
		img2 = ImageTk.PhotoImage(Image.open("images/"+self.files[self.filectr]))
		self.panel.configure(image=img2)
		self.panel.image = img2

	#This method is called when we click the random button
	def clickedRandom(self):
		#sets filectr to a random value we put it in a while loop
		#to ensure we don't get the same image twice
		filectrprevious = self.filectr
		self.filectr = random.randint(0, len(self.files) - 1)

		while (self.filectr == filectrprevious):
			self.filectr = random.randint(0, len(self.files) - 1)
			print(self.filectr)
		#creates  new image
		img2 = ImageTk.PhotoImage(Image.open("images/"+self.files[self.filectr]))
		#configure panel with new image
		self.panel.configure(image=img2)
		#set the panel image to img 2
		self.panel.image = img2


display = Program()