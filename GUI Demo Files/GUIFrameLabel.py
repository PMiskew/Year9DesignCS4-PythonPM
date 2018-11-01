import tkinter as tk

master = tk.Tk()

group = tk.LabelFrame(master, text="Group", padx=5, pady=5)
group.pack(padx=10, pady=10)

w1 = tk.Entry(group)
w1.pack()
w2 = tk.Entry(group)
w2.pack()
master.mainloop()