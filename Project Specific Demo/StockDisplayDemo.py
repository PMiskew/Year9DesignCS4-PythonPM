import tkinter as tk

#Group Data Variables here!
names = ["Stock 1","Stock 2","Stock 3","Stock 4"] #Names entered 
number = [3,1,5,4,5,6] #NUMBER OWNED 
value = [6,5,4,3,2,1] #VALUE AT TIME OF PURCHASE

'''
READING THE TABLE
names[0] = "Stock 1"
number[0] = 3
value [0] = 6

3 units of stock 1 valued at 6 dollars. 
Total value = number[0] * value[0]




'''

root = tk.Tk()


titleLabel = tk.Label(root, text = "STOCK MANAGER")
titleLabel.grid(row = 0, column = 0, columnspan = 3)

#Output box is where we will display the stock information
output = tk.Text(root, background = "grey", height = 10, width = 50, font = ("Helvitica",16))
#output.config(state = "disable")
output.grid(row = 1, column = 0, columnspan = 3)

nameLabel = tk.Label(root, text = "Name")
nameLabel.grid(row = 2, column = 0)

nameEntry = tk.Entry(root)
nameEntry.grid(row = 2,column = 1)

root.mainloop()