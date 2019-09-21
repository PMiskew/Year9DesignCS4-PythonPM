import tkinter as tk
from PIL import Image
import time
import threading

root = tk.Tk()
root.title("WordHang")
root.configure(background='grey21')



#[font size, font trigger]
fontdata = [15,1]
font = 15
fontrigger = 1

if fontrigger == -1:
	fontdata[0] = 40
else:
	fontdata[0] = 15


def bigfont():
		fontdata[0] = 40

def settings():
	fontdata[0] = 100
	
	root2 = tk.Tk()
	root2.title("Settings")

	accesslabel = tk.Label(root2, text = "Accessibility Options")
	accesslabel.pack(pady = (20,2), padx = 50, ipady=9)

	accessbtn = tk.Button(root2, text = "Bigger Text", command=bigfont)
	accessbtn.pack(padx = 50, ipadx= 25, ipady=7)

	accessbtn2 = tk.Button(root2, text = "Color Contrast")
	accessbtn2.pack(pady = 10, padx = 50, ipadx= 15, ipady=7)

	accessbtn3 = tk.Button(root2, text = "Text to Speech")
	accessbtn3.pack(padx = 50, ipadx= 15, ipady=7)

	accesslabel2 = tk.Label(root2, text = "Vocabulary List")
	accesslabel2.pack(pady = (20,2), padx = 50, ipady=9)





def reset():
	answer = []


def on_enter(e):
    btnStat1['background'] = 'white'

def on_leave(e):
    btnStat1 ['background'] = 'red'


def move(event):
	x = event.x
	y = event.y
	print("(",x,",",y,")")


def keypressed(event):
	key = event.keysym.upper()

	print (key)

	#Loop through and check if key is in canswer
	for i in range(0, len(canswer),1):
		if canswer[i] == key:
			print("CORRECT LETTER")
			answer[i] = key

#	for i in range(0,len(answer),1):
#		print(80 + xshift * i)

		canvas.create_text(200 + xshift * i, 120, text = answer[i]+" ", anchor = 'center', font = ("Times",30), disabledfill='grey1', activefill = 'red')

#************************************* TOTAL POINTS *********************************


#************************************* SHOWN CODE *********************************

incorrect = []
canswer = []
#canswer = ["M","O","N","K","E","Y","S"]
strans = "IGNORE"
for i in range (0, len(strans),1):
	canswer.append(strans[i])

#I woudl have hte computer generate the answer list
answer = []
#answer = ["_","_","_","_","_","_"]
for i in range (0, len(canswer),1):
	answer.append("__")

#************************************* CANVAS IMAGE *********************************
#output = tk.Text(root, background = "grey", height = 30, width = 20, font = ("cambria", ))
#output.config(state = "disable") #Can't type inside it
#output.grid(row = 0, column = 0, columnspan = 2)

canvas = tk.Canvas(root, width = 800, height = 490)
canvas.grid(row = 0, column = 3, columnspan = 6, rowspan = 15)
#photo = tk.PhotoImage(file = 'background.png')
#canvas.create_image(0,0, image=photo, anchor=tk.NW)
xshift = 75
for i in range(0,len(answer),1):
	print(100 + xshift * i)




canvas.bind("<Motion>",move)
root.bind("<Key>",keypressed)


#********** WORD BOX ***********************
wordbox = canvas.create_rectangle(177, 85, 632, 162, fill='#fff', outline='grey4')

#********** DEFINITION BOX *****************
definitionbox = canvas.create_rectangle(177, 196, 632, 248, fill='#fff', outline='grey4')
defintiontext = canvas.create_text(181, 200, anchor="nw", text= "Definition: ", font = font, disabledfill='grey1', activefill = 'red')
definitionword = canvas.create_text(245, 200, text= "Refuse to take notice of or acknowledge; disregard intentionally.", anchor="nw", font = (15), fill='red', activefill = 'grey1')


#********** GUESSED LETTERS BOX ************
guessedlettersbox = canvas.create_rectangle(22, 335, 248, 400, fill='grey90', outline='grey4')
guessedletterslabel = canvas.create_rectangle(22, 295, 248, 325, fill='grey75', outline='grey4')
guessedlettersword = canvas.create_text(137, 310, text= "Guessed Letters", anchor="center", font = font, fill='grey1', activefill = 'white')

timebox = canvas.create_rectangle(267, 335, 493, 400, fill='grey90', outline='grey4')
timelabel = canvas.create_rectangle(267, 295, 493, 325, fill='grey75', outline='grey4')
timeword = canvas.create_text(380, 310, text= "Time Left", anchor="center", font = fontdata[0], fill='grey1', activefill = 'white')

pointswbox = canvas.create_rectangle(514, 335, 740, 400, fill='grey90', outline='grey4')
pointswlabel = canvas.create_rectangle(514, 295, 740, 325, fill='grey75', outline='grey4')
pointswword = canvas.create_text(627, 310, text= "Points Worth", anchor="center", font = font, fill='grey1', activefill = 'white')

#sysdef = canvas.create_rectangle(172, 80, 627, 157, fill='#fff', outline='snow')
#canvas.move(sysdef, 0, 0)

#systxt1 = canvas.create_rectangle(250, 20, 50, 210, fill='#fff', outline='snow')
#canvas.move(sysdef, 0, 0)





#************************************* EXECUTION CODE *********************************




#************************************* SIDE WIDGETS *********************************

btnStat1 = tk.Button(root, text = "Menu", font= font, padx = 50, relief = tk.RAISED)
btnStat1.grid(row = 0, column = 0, stick = "NESW", columnspan = 2, padx = 14 ,pady = (14,7))
btnStat1.bind("<Enter>", on_enter)
btnStat1.bind("<Leave>", on_leave)

btnsettings = tk.Button(root, text = "Settings", command=settings)
btnsettings.grid(row = 1, column = 0, stick = "NESW", columnspan = 2, padx = 14 ,pady = (7,7))

btnStat3 = tk.Button(root, text = "Vocabulary")
btnStat3.grid(row = 2, column = 0, stick = "NESW", columnspan = 2, padx = 14 ,pady = (7,14))

btnStat4 = tk.Button(root, text = "Reset", command= reset)
btnStat4.grid(row = 3, column = 0, stick = "NESW", columnspan = 2, padx = 14 ,pady = (45,14))

pointbox = tk.Text(root, width = 10, height = 2, background = 'grey75')
pointbox.insert(tk.INSERT, " Total Points:")
pointbox.config(state="disabled")
pointbox.grid(row = 4, column = 0, columnspan = 2, stick = "NESW",pady = 25)

#**************************INSTRUCTIONS***********************

sys = tk.Text(root, width = 10, height = 7, background = 'grey90')
sys.grid(row = 14, column = 0, columnspan = 2, stick = "NESW", padx = 7 ,pady = 14)

instruction = 1

if instruction == 1:
	text = ("Hello, welcome to   WordHang! Look at the definition and try to guess the word.   Just type the guessed letters on your keyboard!")

sys.insert(tk.INSERT, text)
sys.config(state="disabled")

#************************** TIMER *****************************

def countdown(t):
    root.mainloop()
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        t -= 1
    print('Goodbye!\n\n\n\n\n')

#Start coutdown as thread

tcount = threading.Thread(target = countdown(145))
t.start()

