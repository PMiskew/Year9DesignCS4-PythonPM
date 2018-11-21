import tkinter as tk

master = tk.Tk()

w = tk.Canvas(master, width=250, height=250)
# pack the canvas into a frame/form
w.pack(expand=YES, fill=BOTH)

# load the .gif image file
gif1 = PhotoImage(file='images/100_Fermium.jpg')

# put gif image on canvas
# pic's upper left corner (NW) on the canvas is at x=50 y=10
w.create_image(50, 10, image=gif1, anchor=NW)

scale_w = 250/500
scale_h = 250/500
photoImg.zoom(scale_w, scale_h)

master.mainloop()