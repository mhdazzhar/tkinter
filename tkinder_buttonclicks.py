from tkinter import *
root=Tk()
def fun():
    print("Click here")
but1=Button(root,text="OK",command=fun)
but1.pack()
root.mainloop()