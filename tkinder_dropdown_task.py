from tkinter import *
root=Tk()
class asr:
    def __init__(self,rootone):
        frame=Frame(rootone)
        frame.pack()
        self.qbutton=Button(frame,text="Exit",command=frame.quit)
        self.qbutton.pack()
mymenu=Menu(root)
root.config(menu=mymenu)
submenu=Menu(mymenu)

mymenu.add_cascade(label="File",menu=submenu)
submenu.add_command(label="New Project")
submenu.add_command(label="New")
submenu.add_separator()
submenu.add_command(label="New Scratch File")
submenu.add_command(label="Open")
submenu.add_separator()
submenu.add_command(label="Save as")
submenu.add_command(label="Recent projects")

newmenu=Menu(mymenu)

mymenu.add_cascade(label="Edit",menu=newmenu)
newmenu.add_command(label="Undo typing")
newmenu.add_command(label="Redo")
newmenu.add_separator()
newmenu.add_command(label="Cut")
newmenu.add_command(label="Copy")
newmenu.add_separator()
newmenu.add_command(label="Copy Path")
newmenu.add_command(label="Paste")

ourmenu=Menu(mymenu)

mymenu.add_cascade(label="View",menu=ourmenu)
ourmenu.add_command(label="Tool Windows")
ourmenu.add_command(label="Appearance")
ourmenu.add_separator()
ourmenu.add_command(label="Quick Definition")
ourmenu.add_command(label="Parameter Info")
ourmenu.add_separator()
ourmenu.add_command(label="Type Info")
ourmenu.add_command(label="Content Info")

yourmenu=Menu(mymenu)

mymenu.add_cascade(label="Navigate",menu=yourmenu)
yourmenu.add_command(label="Back")
yourmenu.add_command(label="Forward")
yourmenu.add_separator()
yourmenu.add_command(label="Search everywhere")
yourmenu.add_command(label="Class")
yourmenu.add_separator()
yourmenu.add_command(label="File")
yourmenu.add_command(label="Symbol")

amenu=Menu(mymenu)

mymenu.add_cascade(label="Code",menu=amenu)
amenu.add_command(label="Override methods")
amenu.add_command(label="Implement methods")
amenu.add_separator()
amenu.add_command(label="Generate")
amenu.add_command(label="Code completion")
amenu.add_separator()
amenu.add_command(label="Inspect code")
amenu.add_command(label="Code cleanup")

root.mainloop()





