import tkinter as tk


root = tk.Tk()


labTitle = tk.Label(root,text = "TTC Around UCC", font = ("Helvitica",20))
labTitle.grid(row = 0, column = 0, columnspan = 2)

btn1 = tk.Button(root, text = "Bus", height = 1, width = 20)
btn1.grid(row = 1, column = 0)

btn2 = tk.Button(root, text = "Streetcar", height = 1, width = 20)
btn2.grid(row = 1, column = 1)

lab1 = tk.Label(root, text = "Number: ",background = "red")
lab1.grid(row = 2, column = 0,sticky = "NESW")



root.mainloop()