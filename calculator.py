from tkinter import *
root = Tk()
root.title("Calculator")
e=Entry(root,width=60,bg='red',fg='white' )
e.grid(row=0,column=0,columnspan=4)

def click(number):
    x=e.get()
    e.delete(0,END)
    e.insert(0,str(x) + str(number))

def clear():
    e.delete(0,END)

def add():
    first=e.get()
    global fnum
    global sign
    sign = 'add'
    fnum = first
    e.delete(0,END)

    
def sub():
    first=e.get()
    global fnum
    global sign
    sign = 'sub'
    fnum = first
    e.delete(0,END)

def mul():
    first=e.get()
    global fnum
    global sign
    sign = 'mul'
    fnum = first
    
    e.delete(0,END)

def div():
    first=e.get()
    global fnum
    global sign
    sign = 'div'
    
    fnum = first
    
    e.delete(0,END)

def equal():
    last=e.get()
    if sign == 'add':
        e.delete(0,END)
        e.insert(0,int(fnum) + int(last))
    elif sign == 'sub':
        e.delete(0,END)
        e.insert(0,int(fnum) - int(last))
    elif sign == 'mul':
        e.delete(0,END)
        e.insert(0,int(fnum) * int(last))
    elif sign == 'div':
        e.delete(0,END)
        e.insert(0,int(fnum) / int(last))

button_1 = Button(root,text='1',command=lambda: click(1),padx=40,pady=20,fg="white",bg="red").grid(row='3',column='0')
button_2 = Button(root,text='2',command=lambda: click(2),padx=40,pady=20,fg="white",bg="red").grid(row='3',column='1')
button_3 = Button(root,text='3',command=lambda: click(3),padx=40,pady=20,fg="white",bg="red").grid(row='3',column='2')

button_4 = Button(root,text='4',command=lambda: click(4),padx=40,pady=20,fg="white",bg="red").grid(row='2',column='0')
button_5 = Button(root,text='5',command=lambda: click(5),padx=40,pady=20,fg="white",bg="red").grid(row='2',column='1')
button_6 = Button(root,text='6',command=lambda: click(6),padx=40,pady=20,fg="white",bg="red").grid(row='2',column='2')

button_7 = Button(root,text='7',command=lambda: click(7),padx=40,pady=20,fg="white",bg="red").grid(row='1',column='0')
button_8 = Button(root,text='8',command=lambda: click(8),padx=40,pady=20,fg="white",bg="red").grid(row='1',column='1')
button_9 = Button(root,text='9',command=lambda: click(9),padx=40,pady=20,fg="white",bg="red").grid(row='1',column='2')
button_0 = Button(root,text='0',command=lambda: click(0),padx=40,pady=20,fg="white",bg="red").grid(row='4',column='0')

button_add = Button(root,text='+',command=add,padx=40,pady=20,fg="white",bg="red").grid(row='1',column='3')
button_sub = Button(root,text='-',command=sub,padx=40,pady=20,fg="white",bg="red").grid(row='2',column='3')
button_mul = Button(root,text='*',command=mul,padx=40,pady=20,fg="white",bg="red").grid(row='3',column='3')
button_div= Button(root,text='/',command=div,padx=40,pady=20,fg="white",bg="red").grid(row='4',column='3')
button_clear = Button(root,text='clear',command=clear,padx=31,pady=20,fg="white",bg="red").grid(row='4',column='1')
button_equal = Button(root,text='=',command=equal,padx=40,pady=20,fg="white",bg="red").grid(row='4',column='2')

root.mainloop()
