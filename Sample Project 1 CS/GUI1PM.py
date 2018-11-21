#This imports the tkinter "tool box" this contains
#all the support material to make GUI elements. 
#by including "as tk" we are giving a short name to use. 
import tkinter as tk


#Main Window
root = tk.Tk() #creates the standard main window. 


#***************WIDGET 1*******************
#Three stages to build elements/objects
#1. CONSTRUCT the Object:  We build and configure it. 
#2. Configure the Object:  We specify behaviours and settings (OPTIONAL)
#3. Pack the Object: Put it in the window
output = tk.Text(root,height = 10, width = 30) #Parameters are what we send to the function.  
#ordered parameters: The order we send them matters. (COMMON)
#named parameters: JavaScript and Python specific
output.config(state = "disabled", background = "blue")
output.grid(row = 0, column = 0, rowspan = 5)


#***************WIDGET 2,3,4 (Labels)*******************
labInput1 = tk.Label(root, text = "Input 1")
labInput1.config(background = "blue", foreground = "red")
labInput1.grid(row = 5, column = 0, sticky = "NESW")

labInput2 = tk.Label(root, text = "Input 2")
labInput2.grid(row = 6, column = 0 )

labInput3 = tk.Label(root, text = "Input 3")
labInput3.grid(row = 7, column = 0)

#***************WIDGET 5,6 (Checkboxs)*******************
#How do I track the checkbox state. 
var1 = tk.IntVar()
var2 = tk.IntVar()

#What the named parameter variable does is binds the IntVar to the 
#checkbox.  If there is a change in the box, there is a change in the 
#variable.  This is called BINDING
cHC = tk.Checkbutton(root, text="Expand", variable=var1)
cHC.grid(row = 0, column = 1)


cLF = tk.Checkbutton(root, text="Expand", variable=var2)
cLF.grid(row = 1, column = 1)


#We are writing an EVENT DRIVE PROGRAM. 
#Build the GUI
#Start it running
#Wait for "EVENT"
root.mainloop() #Starts the program. 




