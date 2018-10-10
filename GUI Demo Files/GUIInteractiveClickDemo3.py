import tkinter as tk

#This example is the same cade of Demo2, but the code 
#has been optimized for better algorithm design. 

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



#Optimization 1: We can use a loop to print out 
#the horizontal and vertical loops.  This gives us
#the ability to be creative by changing intx and 
#inty

#inc must be a factor of width 
incx = 100
incy = 100

for i in range(incx,500,incx):
	canvas.create_line(i,0,i,500)

#Vertical Lines
for i in range(incy,500,incy):
	canvas.create_line(0,i,500,i)


#Optimization 2: We can use two concepts here
#1. A loop to manage position of the letters.  I noticed that
#	there was a pattern for each line 50, 150, 250, 350, 450
#	I set the loop parameters so that it counted through those 
#	values and used them for the x position of the letters
#2. All characters are mapped to integer values.  This is 
#	standardized across all languages.  
#	To change a char to an int we use the ord function
#	ord('a') --> 97
#	To change an int to a char we use the chr function
#	chr(97) --> 'a'
#	This is called casting, which is the process of changing
#	one type to another. 
#	How can we use this? 
#	Since we know that there is a pattern in the letters being
#	displayed we can set up a counter using their decimal (int)
#	value, stated in the ASCII table. 
#	http://www.asciitable.com/
#	values ord("A") --> 65
#	values ord("F") --> 65 + 5
#	values ord("K") --> 65 + 10
#	values ord("P") --> 65 + 15
#	values ord("U") --> 65 + 20
#	We create a decValue to keep track of the decimal value
#	and we create a ctr value to move increase the decValue 
#	each time the loop runs.  

decValue = 65
ctr = 0
for i in range(50,500,100):
	canvas.create_text(i,50, text = chr(decValue + ctr))
	canvas.create_text(i,150, text = chr(decValue + 5 + ctr))
	canvas.create_text(i,250, text = chr(decValue + 10 + ctr))
	canvas.create_text(i,350, text = chr(decValue + 15 + ctr))
	canvas.create_text(i,450, text = chr(decValue + 20 + ctr))
	ctr = ctr + 1

canvas.bind("<Enter>",mouseEnter)
canvas.bind("<Motion>",mouseMove)
canvas.bind("<Leave>",mouseLeave)

root.mainloop()

