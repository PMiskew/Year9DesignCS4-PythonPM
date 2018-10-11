import tkinter as tk
#This example is designed very poorly, but it helps see 
#the patterning and understand the ideas. 

#This is considered POOR CODE DESIGN.  See demo3 for an 
#updated more efficent design

def mouseClicked(event):
	if (event.x > 100 and event.x < 200 and event.y > 100 and event.y < 200 ):
		canvas.config(bg = "blue")
	if (event.x > 300 and event.x < 400 and event.y > 200 and event.y < 300 ):
		canvas.config(bg = "yellow")
	if (event.x > 0 and event.x < 100 and event.y > 400 and event.y < 500 ):
		canvas.config(bg = "red")
	
def mouseEnter(event):
	print("Enter")


def mouseMove(event):
	#print("Moving")
	#print(event) #prints information about teh event that called method
	#print(event.x) #prints the x location of mouse on canvas
	#print(event.y) #prints the y location of mouse on canvas

	x = event.x
	y = event.y

	if (y > 0 and y <= 100):
		if (x <= 100):
			print("A")
		elif (x <= 200):
			print("B")
		elif (x <= 300):
			print("C")
		elif (x <= 400):
			print("D")
		elif (x <= 500):
			print("E")
	elif (y > 100 and y <= 200):
		if (x <= 100):
			print("F")
		elif (x <= 200):
			print("G")
		elif (x <= 300):
			print("H")
		elif (x <= 400):
			print("I")
		elif (x <= 500):
			print("J")
	elif (y > 200 and y <= 300):
		if (x <= 100):
			print("K")
		elif (x <= 200):
			print("L")
		elif (x <= 300):
			print("M")
		elif (x <= 400):
			print("N")
		elif (x <= 500):
			print("O")
	elif (y > 300 and y <= 400):
		if (x <= 100):
			print("P")
		elif (x <= 200):
			print("Q")
		elif (x <= 300):
			print("R")
		elif (x <= 400):
			print("S")
		elif (x <= 500):
			print("T")
	elif (y > 400 and y <= 500):
		if (x <= 100):
			print("U")
		elif (x <= 200):
			print("V")
		elif (x <= 300):
			print("W")
		elif (x <= 400):
			print("X")
		elif (x <= 500):
			print("Y")
		

def mouseLeave(event):
	print("Leaving")

root = tk.Tk()

canvas = tk.Canvas(root, bg = "red", width = 500, height = 500)
canvas.pack()

#create_line(x1,y1,x2,y2)
#Horizontal Lines
canvas.create_line(100,0,100,500)
canvas.create_line(200,0,200,500)
canvas.create_line(300,0,300,500)
canvas.create_line(400,0,400,500)

#Vertical Lines
canvas.create_line(0,100,500,100)
canvas.create_line(0,200,500,200)
canvas.create_line(0,300,500,300)
canvas.create_line(0,400,500,400)
#Draw

canvas.create_text(50,50, text = "A")
canvas.create_text(150,50, text = "B")
canvas.create_text(250,50, text = "C")
canvas.create_text(350,50, text = "D")
canvas.create_text(450,50, text = "E")

canvas.create_text(50,150, text = "F")
canvas.create_text(150,150, text = "G")
canvas.create_text(250,150, text = "H")
canvas.create_text(350,150, text = "I")
canvas.create_text(450,150, text = "J")

canvas.create_text(50,250, text = "K")
canvas.create_text(150,250, text = "L")
canvas.create_text(250,250, text = "M")
canvas.create_text(350,250, text = "N")
canvas.create_text(450,250, text = "O")

canvas.create_text(50,350, text = "P")
canvas.create_text(150,350, text = "Q")
canvas.create_text(250,350, text = "R")
canvas.create_text(350,350, text = "S")
canvas.create_text(450,350, text = "T")


canvas.create_text(50,450, text = "U")
canvas.create_text(150,450, text = "V")
canvas.create_text(250,450, text = "W")
canvas.create_text(350,450, text = "X")
canvas.create_text(450,450, text = "Y")

canvas.bind("<Enter>",mouseEnter)
canvas.bind("<Motion>",mouseMove)
canvas.bind("<Leave>",mouseLeave)
canvas.bind("<Button-1>",mouseClicked)

root.mainloop()

