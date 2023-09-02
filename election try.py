from tkinter import*

global dmk
global admk
global nk

dmk=[]
admk=[]
nk=[]
w=Tk()
w.title('Election')
x=IntVar()
a=Label(w,text='NAME',bg='pink')
name=Entry(w,bg="black",fg='white')
k=Entry(w)
b=Label(w,text='Adhar no:',bg='pink')
c=Entry(w)

a.pack()
k.pack()
b.pack()
c.pack()
Radiobutton(w,text='DMK',variable=x,value=1).pack()
Radiobutton(w,text='ADMK',variable=x,value=2).pack()
Radiobutton(w,text='Nandha kumar',variable=x,value=3).pack()
def click():

    
    
    k.delete(0,END)
    c.delete(0,END)
    if(x.get()==1):
        dmk.append(1)
    if(x.get()==2):
        admk.append(1)
        
    if(x.get()==3):
        nk.append(1)
        
h=Button(w,text="Submit",width=20,bg='pink',fg='red',command=click)
h.pack()
def com():
    h=Tk()
    h.title("Result")
    a=Label(h,text="DMK:")
    b=Label(h,text=len(dmk))
    c=Label(h,text="ADMK:")
    d=Label(h,text=len(admk))
    e=Label(h,text="NANDHA KUMAR:")
    f=Label(h,text=len(nk))
    a.pack()
    b.pack()
    c.pack()
    d.pack()
    e.pack()
    f.pack()
    global g
    global s
    global l
    g=len(dmk)
    s=len(admk)
    l=len(nk)
    if(g>l and g>s):
           f=Tk()
           f.title("Winner")
           a=Label(f,text="##DMK IS WINNER ##",fg="red",bg='pink')
           a.pack()
    if(s>l and s>g):
           f=Tk()
           f.title("Winner")
           a=Label(f,text="##ADMK IS WINNER ##",fg="red",bg='pink')
           a.pack()
    if(l>g and l>s):
           f=Tk()
           f.title("Winner")
           a=Label(f,text="##NANDHA KUMAR  IS WINNER ##",fg="red",bg='pink')
           a.pack()
z=Button(w,text="Complete",width=20,bg='pink',fg='red',command=com)
z.pack()

