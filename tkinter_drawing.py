from tkinter import *
root=Tk()
canvas=Canvas(root,width=100,height=200)
canvas.pack()
draw1=canvas.create_oval(10,10,80,90,fill="Red")
root.mainloop()