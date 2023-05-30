from tkinter import *
class myfile:
    def __init__(self,rootone):
        frame=Frame(rootone)
        frame.pack()
        self.pbutton=Button(frame,text="click",command=self.prntmsg)
        self.pbutton.pack()

        self.msbutton = Button(frame, text="info")
        self.msbutton.pack()
        from tkinter import messagebox
        messagebox.showinfo("New message", "canceled")

        self.qbutton=Button(frame,text="exit",command=frame.quit)
        self.qbutton.pack()

    def prntmsg(self):
        print("clicked")

root=Tk()
obj=myfile(root)
root.mainloop()