from tkinter import *
window=Tk()
window.title("Calculator")
window.geometry('165x185')
textin=StringVar()
opr=""
def click(num):
    global opr
    opr=opr+str(num)
    textin.set(opr)
def equal():
    global opr
    cal=str(eval(opr))
    textin.set(cal)
    opr=''
def clear():
    textin.set('')

txt=Entry(window,textvar=textin,width=25,bd=5)
txt.grid(column=0,row=0)
btn_c=Button(window,text="C",command=clear,padx=4,pady=45)
btn_c.place(x=130,y=30)
sev=Button(window,text="7",command=lambda:click(7))
sev.place(x=10,y=30)
eight=Button(window,text="8",command=lambda:click(8))
eight.place(x=40,y=30)
nine=Button(window,text="9",command=lambda:click(9))
nine.place(x=70,y=30)
four=Button(window,text="4",command=lambda:click(4))
four.place(x=10,y=60)
five=Button(window,text="5",command=lambda:click(5))
five.place(x=40,y=60)
six=Button(window,text="6",command=lambda:click(6))
six.place(x=70,y=60)
one=Button(window,text="1",command=lambda:click(1))
one.place(x=10,y=90)
two=Button(window,text="2",command=lambda:click(2))
two.place(x=40,y=90)
thr=Button(window,text="3",command=lambda:click(3))
thr.place(x=70,y=90)
zero=Button(window,text="0",command=lambda:click(0),padx=17,pady=1)
zero.place(x=10,y=120)
ad=Button(window,text="+",command=lambda:click("+"))
ad.place(x=100,y=30)
su=Button(window,text="-",command=lambda:click("-"))
su.place(x=100,y=60)
mu=Button(window,text="x",command=lambda:click("*"))
mu.place(x=100,y=90)
di=Button(window,text="/",command=lambda:click("/"))
di.place(x=100,y=120)
dot=Button(window,text=".",command=lambda:click("."),padx=3,pady=1)
dot.place(x=70,y=120)
equ=Button(window,text="=",command=equal,padx=63,pady=1)
equ.place(x=10,y=150)
window.mainloop()
