import tkinter as tk

master = tk.Tk()

groupA = tk.LabelFrame(master, text="Group A", padx=5, pady=5)
groupA.pack(padx=10, pady=10)


groupB = tk.LabelFrame(master, text="Group B", padx=5, pady=5)
groupB.pack(padx=10, pady=10)

#******************** Group A elements
wA1 = tk.Entry(groupA)
wA1.pack()
wA2 = tk.Entry(groupA)
wA2.pack()

#******************** Group A elements
wB1 = tk.Entry(groupB)
wB1.grid(row = 0, column = 0)
wB2 = tk.Entry(groupB)
wB2.grid(row = 0, column = 1)
master.mainloop()


