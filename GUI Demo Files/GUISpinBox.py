import tkinter as tk
master = tk.Tk()

#w = tk.Spinbox(master, from_=0, to=10)
w = tk.Spinbox(master, values=(1, 2, 4, 8))
w.pack()

master.mainloop()

