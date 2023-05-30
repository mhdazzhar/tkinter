import parser
from tkinter import *
root=Tk()
root.title("Calculator")
display=Entry(root)
display.grid(row=0,columnspan=5)

i=0
def get_digits(num):
   global i
   display.insert(i,num)
   i=i+1

def clear_all():
    display.delete(0,END)

def undo():
    entire_digits=display.get()
    if len(entire_digits):
        new_digits=entire_digits[:-1]
        clear_all()
        display.insert(0,new_digits)

def operation(opr):
    global i
    length=len(opr)
    display.insert(i,opr)
    i+=length

def calculate():
    entire_digits=display.get()
    a=parser.expr(entire_digits).compile()
    result=eval(a)
    clear_all()
    display.insert(0,result)






Button(root,text="(",command=lambda:operation('(')).grid(row=1,column=0)
Button(root,text="(",command=lambda:operation('(')).grid(row=1,column=0)
Button(root,text="->",command=lambda:undo()).grid(row=1,column=2)
Button(root,text="AC",command=lambda:clear_all()).grid(row=1,column=3)
Button(root,text="%",command=lambda:operation('%')).grid(row=2,column=0)
Button(root,text="pi",command=lambda:operation('*3.14')).grid(row=2,column=1)
Button(root,text="^2",command=lambda:operation('**2')).grid(row=2,column=2)
Button(root,text="=",command=lambda:calculate()).grid(row=2,column=3)
Button(root,text="1",command=lambda:get_digits(1)).grid(row=3,column=0)
Button(root,text="2",command=lambda:get_digits(2)).grid(row=3,column=1)
Button(root,text="3",command=lambda:get_digits(3)).grid(row=3,column=2)
Button(root,text="*",command=lambda:operation('*')).grid(row=3,column=3)
Button(root,text="4",command=lambda:get_digits(4)).grid(row=4,column=0)
Button(root,text="5",command=lambda:get_digits(5)).grid(row=4,column=1)
Button(root,text="6",command=lambda:get_digits(6)).grid(row=4,column=2)
Button(root,text="/",command=lambda:operation('/')).grid(row=4,column=3)
Button(root,text="7",command=lambda:get_digits(7)).grid(row=5,column=0)
Button(root,text="8",command=lambda:get_digits(8)).grid(row=5,column=1)
Button(root,text="9",command=lambda:get_digits(9)).grid(row=5,column=2)
Button(root,text="+",command=lambda:operation('+')).grid(row=5,column=3)
Button(root,text="0",command=lambda:get_digits(0)).grid(row=6,column=1)

root.mainloop()