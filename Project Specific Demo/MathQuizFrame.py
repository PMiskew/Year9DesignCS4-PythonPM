import tkinter as tk

root = tk.Tk()

questionFrame = tk.LabelFrame(root,text = "Question")
questionFrame.grid(row = 0, column = 0)

calcFrame = tk.LabelFrame(root,text = "Calculator")
calcFrame.grid(row = 0, column = 1)

#****************Question Frame
qfBtn1 = tk.Button(questionFrame,text = "Button")
qfBtn1.pack()

#****************Calc Frame
cfBtn1 = tk.Button(calcFrame,text = "Button")
cfBtn1.pack()




root.mainloop()