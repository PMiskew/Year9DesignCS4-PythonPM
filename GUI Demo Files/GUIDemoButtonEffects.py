import tkinter as tk


def on_enter(e):
	print("enter")
	btn1.config(highlightbackground = "#724C8F")
def on_leave(e):
	print("exit")
	btn1.config(highlightbackground="#391356")
	btn1.config(text = "Button1")
root = tk.Tk()
root.title("Button Effect")

btn1 = tk.Button(text = "Button1", height = 10, width = 10, highlightbackground="#391356")

btn1.bind("<Enter>", on_enter)
btn1.bind("<Leave>", on_leave)
btn1.pack()


btn2 = tk.Button(text = "Button2", background = "red")
btn2.pack()


btn3 = tk.Button(text = "Button3")
btn3.pack()


btn4 = tk.Button(text = "Button4")
btn4.pack()


root.mainloop()