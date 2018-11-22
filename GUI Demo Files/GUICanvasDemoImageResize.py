from tkinter import *
from PIL import Image, ImageTk

def resize(event):
    size = (event.width, event.height)
    resized = original.resize(size,Image.ANTIALIAS)
    image = ImageTk.PhotoImage(resized)
    display.delete("IMG")
    display.create_image(0, 0, image=image, anchor=NW, tags="IMG")
    print("resizing")

root = Tk()
root.columnconfigure(0,weight=1)
root.rowconfigure(0,weight=1)
original = Image.open('images/question.png')
image = ImageTk.PhotoImage(original)
display = Canvas(root)
display.create_image(0, 0, image=image, anchor=NW, tags="IMG")
display.grid(row=0, sticky=W+E+N+S)
#display.pack(fill=BOTH, expand=1)

root.bind("<Configure>", resize)


root.mainloop()
