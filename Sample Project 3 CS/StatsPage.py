import tkinter as tk
from tkinter import ttk
import random
#Group Functions up here
def change():
	print("Change")
	print(btnStat1["state"])
	if btnStat1["state"] == "disabled":
		sortByStat1()
		return
	if btnStat2["state"] == "disabled":
		sortByStat2()
		return
	if btnStat3["state"] == "disabled":
		sortByStat3()
		return
	if btnName["state"] == "disabled":
		sortByName()
		return




def clickedA():
	print("clicked")
	
	btnStat1.config(state = "disabled")
	btnStat2.config(state = "normal")
	btnStat3.config(state = "normal")
	btnName.config(state = "normal")
	sortByStat1()

def clickedB():
	print("clicked")
	
	btnStat1.config(state = "normal")
	btnStat2.config(state = "disabled")
	btnStat3.config(state = "normal")
	btnName.config(state = "normal")
	sortByStat2()

def clickedC():
	print("clicked")
	
	btnStat1.config(state = "normal")
	btnStat2.config(state = "normal")
	btnStat3.config(state = "disabled")
	btnName.config(state = "normal")
	sortByStat3()

def clickedN():
	btnStat1.config(state = "normal")
	btnStat2.config(state = "normal")
	btnStat3.config(state = "normal")
	btnName.config(state = "disabled")
	sortByName();
	

def randomizeData():

	for i in range(0,100,1):
		x = random.randint(0,len(names) - 1)
		y = random.randint(0,len(names) - 1)
		print(x,y)
		temp = names[x]
		names[x] = names[y]
		names[y] = temp

		temp = stat1[x]
		stat1[x] = stat1[y]
		stat1[y] = temp

		temp = stat2[x]
		stat2[x] = stat2[y]
		stat2[y] = temp

		temp = stat2[x]
		stat2[x] = stat1[y]
		stat2[y] = temp


def sortByName():

	print(v.get())

	if (v.get() == "1"): #ASCENDING
		for i in range(0,len(names) - 1,1):
			for j in range(i + 1,len(names),1):
				if names[i].lower() > names[j].lower():
					#Swap names
					temp = names[i]
					names[i] = names[j]
					names[j] = temp
					#Swap stat 1
					temp = stat1[i]
					stat1[i] = stat1[j]
					stat1[j] = temp
					#Swap stat 2
					temp = stat2[i]
					stat2[i] = stat2[j]
					stat2[j] = temp
					#Swap stat 3
					temp = stat3[i]
					stat3[i] = stat3[j]
					stat3[j] = temp
	elif (v.get() == "2"): #DECENDING
		for i in range(0,len(names) - 1,1):
			for j in range(i + 1,len(names),1):
				if names[i].lower() < names[j].lower():
					#Swap names
					temp = names[i]
					names[i] = names[j]
					names[j] = temp
					#Swap stat 1
					temp = stat1[i]
					stat1[i] = stat1[j]
					stat1[j] = temp
					#Swap stat 2
					temp = stat2[i]
					stat2[i] = stat2[j]
					stat2[j] = temp
					#Swap stat 3
					temp = stat3[i]
					stat3[i] = stat3[j]
					stat3[j] = temp
	elif (v.get() == "3"):
		randomizeData()
	
	display()
def sortByStat1():

	print(v.get())

	if (v.get() == "1"): #ASCENDING
		for i in range(0,len(stat1) - 1,1):
			for j in range(i + 1,len(stat1),1):
				if stat1[i] > stat1[j]:
					#Swap names
					temp = names[i]
					names[i] = names[j]
					names[j] = temp
					#Swap stat 1
					temp = stat1[i]
					stat1[i] = stat1[j]
					stat1[j] = temp
					#Swap stat 2
					temp = stat2[i]
					stat2[i] = stat2[j]
					stat2[j] = temp
					#Swap stat 3
					temp = stat3[i]
					stat3[i] = stat3[j]
					stat3[j] = temp
	elif (v.get() == "2"): #DECENDING
		for i in range(0,len(stat1) - 1,1):
			for j in range(i + 1,len(stat1),1):
				if stat1[i] < stat1[j]:
					#Swap names
					temp = names[i]
					names[i] = names[j]
					names[j] = temp
					#Swap stat 1
					temp = stat1[i]
					stat1[i] = stat1[j]
					stat1[j] = temp
					#Swap stat 2
					temp = stat2[i]
					stat2[i] = stat2[j]
					stat2[j] = temp
					#Swap stat 3
					temp = stat3[i]
					stat3[i] = stat3[j]
					stat3[j] = temp
	
	display()
def sortByStat2():

	print(v.get())

	if (v.get() == "1"): #ASCENDING
		for i in range(0,len(stat2) - 1,1):
			for j in range(i + 1,len(stat2),1):
				if stat2[i] > stat2[j]:
					#Swap names
					temp = names[i]
					names[i] = names[j]
					names[j] = temp
					#Swap stat 1
					temp = stat1[i]
					stat1[i] = stat1[j]
					stat1[j] = temp
					#Swap stat 2
					temp = stat2[i]
					stat2[i] = stat2[j]
					stat2[j] = temp
					#Swap stat 3
					temp = stat3[i]
					stat3[i] = stat3[j]
					stat3[j] = temp
	elif (v.get() == "2"): #DECENDING
		for i in range(0,len(stat1) - 1,1):
			for j in range(i + 1,len(stat1),1):
				if stat2[i] < stat2[j]:
					#Swap names
					temp = names[i]
					names[i] = names[j]
					names[j] = temp
					#Swap stat 1
					temp = stat1[i]
					stat1[i] = stat1[j]
					stat1[j] = temp
					#Swap stat 2
					temp = stat2[i]
					stat2[i] = stat2[j]
					stat2[j] = temp
					#Swap stat 3
					temp = stat3[i]
					stat3[i] = stat3[j]
					stat3[j] = temp
	
	display()
def sortByStat3():

	print(v.get())

	if (v.get() == "1"): #ASCENDING
		for i in range(0,len(stat2) - 1,1):
			for j in range(i + 1,len(stat2),1):
				if stat3[i] > stat3[j]:
					#Swap names
					temp = names[i]
					names[i] = names[j]
					names[j] = temp
					#Swap stat 1
					temp = stat1[i]
					stat1[i] = stat1[j]
					stat1[j] = temp
					#Swap stat 2
					temp = stat2[i]
					stat2[i] = stat2[j]
					stat2[j] = temp
					#Swap stat 3
					temp = stat3[i]
					stat3[i] = stat3[j]
					stat3[j] = temp
	elif (v.get() == "2"): #DECENDING
		for i in range(0,len(stat1) - 1,1):
			for j in range(i + 1,len(stat1),1):
				if stat3[i] < stat3[j]:
					#Swap names
					temp = names[i]
					names[i] = names[j]
					names[j] = temp
					#Swap stat 1
					temp = stat1[i]
					stat1[i] = stat1[j]
					stat1[j] = temp
					#Swap stat 2
					temp = stat2[i]
					stat2[i] = stat2[j]
					stat2[j] = temp
					#Swap stat 3
					temp = stat3[i]
					stat3[i] = stat3[j]
					stat3[j] = temp
	
	display()

def display():
	output.delete("1.0",tk.END)
	output.insert(tk.END,"Name:\tStat1\tStat2\tStat3\n------------------------------------------\n")

	for i in range(0,len(names),1):
		value = names[i] + "\t"+str(stat1[i])+"\t"+str(stat2[i])+"\t"+str(stat3[i])+"\n"
		output.insert(tk.END,value)

#Group Data Variables here!
names = ["Paul", "Francesco","Stephanie","Bill","Connor","Jihoo"]
stat1 = [1,2,3,4,5,6]
stat2 = [6,5,4,3,2,1]
stat3 = [1,3,2,5,4,6]






root = tk.Tk()




output = tk.Text(root, background = "#ffd0aa", height = 10, width = 50, font = ("Helvitica",16))
#output.config(state = "disable")
output.grid(row = 0, column = 0, columnspan = 2)

#**********Configure Output Data


output.insert(tk.END,"Name:\tStat1\tStat2\tStat3\n------------------------------------------\n")
for i in range(0,len(names),1):
	value = names[i] + "\t"+str(stat1[i])+"\t"+str(stat2[i])+"\t"+str(stat3[i])+"\n"
	output.insert(tk.END,value)



btnStat1 = tk.Button(root, text = "Stat 1", height = 2, width = 10, command = clickedA)
btnStat1.config(state = "disabled")
btnStat1.grid(row = 1, column =0, sticky = "NESW")

btnStat2 = tk.Button(root, text = "Stat 2", height = 2, width = 10, command = clickedB)
btnStat2.grid(row = 2, column =0, sticky = "NESW")

btnStat3 = tk.Button(root, text = "Stat 3", height = 2, width = 10, command = clickedC)
btnStat3.grid(row = 3, column =0, sticky = "NESW")

btnName = tk.Button(root, text = "Name", height = 2, width = 10, command = clickedN)
btnName.grid(row = 4, column = 0, sticky = "NESW")


MODES = [
("Ascending", "1"),
("Descending", "2"),
("Random","3")
]

v = tk.StringVar() #v keeps track of which button is selected. 
v.set("1") # initialize

for r in range(0,len(MODES),1):
	b = ttk.Radiobutton(root, text=MODES[r][0], variable=v, value=MODES[r][1], command = change)
	b.grid(row = 1 + r, column = 1, sticky = "W", padx = 40)


root.mainloop()