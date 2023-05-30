from tkinter import *
root=Tk()
def fun1():
    print("Undo clicked")
mymenu=Menu(root)
root.config(menu=mymenu)

submenu=Menu(mymenu)

mymenu.add_cascade(label="File",menu=submenu)
submenu.add_command(label='save1')
submenu.add_command(label='save2')
submenu.add_separator()
submenu.add_command(label='save3')
submenu.add_command(label='save4')

newmenu=Menu(mymenu)

mymenu.add_cascade(label="Edit",menu=newmenu)
newmenu.add_command(label="Undo",command=fun1)

toolbar=Frame(root,bg="green")
inbutton=Button(toolbar,text="Run")
inbutton.pack(side=LEFT,padx=3,pady=4)
inbutton=Button(toolbar,text="Help")
inbutton.pack(side=LEFT,padx=3,pady=4)
toolbar.pack(side=TOP,fill=X)

statusbar=Label(root,text="This is status bar",bg="White",fg="Black",relief=SUNKEN,bd=2)
statusbar.pack(side=BOTTOM,fill=X)
root.mainloop()
