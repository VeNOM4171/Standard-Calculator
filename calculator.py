import tkinter
from tkinter import *
from tkinter import messagebox

root = tkinter.Tk()

root.geometry("400x500+500+100")
root.resizable(0, 0)
root.title("CALCULATOR")
root.wm_attributes('-alpha', '0.8')

val = ''
a = 0.0
b = 0.0
operator = ''
dot_ct = 0



def div_x_clicked():
    global val
    global a

    a = float(val)
    a = 1/a
    val = str(a)
    data.set(val)

def sq_clicked():
    global val
    global a

    a = float(val)
    a = a * a
    val = str(a)
    data.set(val)

def neg_clicked():
    global val
    global operator


def sq_root_clicked():
    global val
    global a


def ce_clicked():
    c_clicked()

def c_clicked():
    global val
    global a
    global operator
    global dot_ct
    val = ''
    operator = ''
    a = 0
    data.set(val)
    dot_ct = 0

def del_clicked():
    global val
    global dot_ct

    last = val[-1]
    if last == '.':
        dot_ct = 0
    val = val[:-1]
    data.set(val)

    if last == '+' or last == '-' or last == 'x' or last == '/':
        if val.find('.') != -1: #found
            dot_ct = 1
        elif val.find('.') == -1:   #notFound
            dot_ct = 0


def percent_clicked():
    global dot_ct
    dot_ct = 0


def seven_clicked():
    global val
    val = val + '7'
    data.set(val)

def eight_clicked():
    global val
    val = val + '8'
    data.set(val)

def nine_clicked():
    global val
    val = val + '9'
    data.set(val)

def div_clicked():
    global val
    global a
    global dot_ct
    a = float(val)


    val = val + '/'
    data.set(val)
    dot_ct = 0


def four_clicked():
    global val
    val = val + '4'
    data.set(val)



def five_clicked():
    global val
    val = val + '5'
    data.set(val)


def six_clicked():
    global val
    val = val + '6'
    data.set(val)


def mul_clicked():
    global val
    global operator
    global a
    global dot_ct
    a = float(val)
    operator = 'x'
    val = val + 'x'
    data.set(val)
    dot_ct = 0


def one_clicked():
    global val
    val = val + '1'
    data.set(val)


def two_clicked():
    global val
    val = val + '2'
    data.set(val)


def three_clicked():
    global val
    val = val + '3'
    data.set(val)


def minus_clicked():
    global val
    global operator
    global a
    global dot_ct
    a = float(val)
    operator = '-'
    val = val + '-'
    data.set(val)
    dot_ct = 0


def zero_clicked():
    global val
    val = val + '0'
    data.set(val)

def dot_clicked():
    global val
    global dot_ct

    if dot_ct == 0:
        val = val + '.'
        data.set(val)
        dot_ct = 1


def plus_clicked():
    global val
    global operator
    global a
    global dot_ct
    a = float(val)
    operator = '+'
    val = val + '+'
    data.set(val)
    dot_ct = 0



def result():
    global val
    global operator
    global a
    val2 = val
    if operator == '+':
        b = float(val2.split('+')[1])
        ans = a + b
        data.set(ans)
        val = str(ans)
    elif operator == '-':
        b = float(val2.split('-')[1])
        ans = a - b
        data.set(ans)
        val = str(ans)
    elif operator == 'x':
        b = float(val2.split('x')[1])
        ans = a * b
        data.set(ans)
        val = str(ans)
    elif operator == '/':
        b = float(val2.split('/')[1])
        if b == 0:
            tkinter.messagebox.showerror('ERROR', 'Division Tends To Infinite')
        else:
            ans = a / b
            data.set(ans)
            val = str(ans)



def close_clicked():
    close = tkinter.messagebox.askyesno("calculator", "Click  YES if you want to exit")

    if close == TRUE:
        root.destroy()
        return



menu = Menu(root)
root.config(menu=menu)
moremenu = Menu(menu)
moremenu = Menu(menu, tearoff=0)
moremenu.add_command(label='Exit', command=close_clicked)


data = StringVar()
lbl = Label(root, text='Label', anchor=SE, font=("Verdana", 40), textvariable=data, background='#ffffff', fg='#000000', )

lbl.pack(expand=True, fill="both", )

btnrow1 = Frame(root)
btnrow1.pack(expand=True, fill="both")

btnrow2 = Frame(root)
btnrow2.pack(expand=True, fill="both")

btnrow3 = Frame(root)
btnrow3.pack(expand=True, fill="both")

btnrow4 = Frame(root)
btnrow4.pack(expand=True, fill="both")

btnrow5 = Frame(root)
btnrow5.pack(expand=True, fill="both")

btnrow6 = Frame(root)
btnrow6.pack(expand=True, fill="both")

btn1 = Button(btnrow1, text='1/x', font=("Verdana", 20), relief=GROOVE, border=0, command=div_x_clicked)
btn1.pack(side=LEFT, expand=True, fill="both", )

btn2 = Button(btnrow1, text='x^2', font=("Verdana", 22), relief=GROOVE, border=0, command=sq_clicked)
btn2.pack(side=LEFT, expand=True, fill="both", )

btn3 = Button(btnrow1, text='(-)', font=("Verdana", 25), relief=GROOVE, border=0, command=neg_clicked)
btn3.pack(side=LEFT, expand=True, fill="both", )

btn4 = Button(btnrow1, text='\u221A', font=("Verdana", 25), relief=GROOVE, border=0, command=sq_root_clicked)
btn4.pack(side=LEFT, expand=True, fill="both", )

btn1 = Button(btnrow2, text='CE', font=("Verdana", 25), relief=GROOVE, border=0, command=ce_clicked)
btn1.pack(side=LEFT, expand=True, fill="both", )

btn2 = Button(btnrow2, text='C', font=("Verdana", 25), relief=GROOVE, border=0, command=c_clicked)
btn2.pack(side=LEFT, expand=True, fill="both", )

btn3 = Button(btnrow2, text='del', font=("Verdana", 25), relief=GROOVE, border=0, command=del_clicked)
btn3.pack(side=LEFT, expand=True, fill="both", )

btn4 = Button(btnrow2, text='%', font=("Verdana", 25), relief=GROOVE, border=0, command=percent_clicked)
btn4.pack(side=LEFT, expand=True, fill="both", )

btn1 = Button(btnrow3, text='7', font=("Verdana", 25), relief=GROOVE, border=0, command=seven_clicked)
btn1.pack(side=LEFT, expand=True, fill="both", )

btn2 = Button(btnrow3, text='8', font=("Verdana", 25), relief=GROOVE, border=0, command=eight_clicked)
btn2.pack(side=LEFT, expand=True, fill="both", )

btn3 = Button(btnrow3, text='9', font=("Verdana", 25), relief=GROOVE, border=0, command=nine_clicked)
btn3.pack(side=LEFT, expand=True, fill="both", )

btn4 = Button(btnrow3, text='/', font=("Verdana", 25), relief=GROOVE, border=0, command=div_clicked)
btn4.pack(side=LEFT, expand=True, fill="both", )

btn1 = Button(btnrow4, text='4', font=("Verdana", 25), relief=GROOVE, border=0, command=four_clicked)
btn1.pack(side=LEFT, expand=True, fill="both", )

btn2 = Button(btnrow4, text='5', font=("Verdana", 25), relief=GROOVE, border=0, command=five_clicked)
btn2.pack(side=LEFT, expand=True, fill="both", )

btn3 = Button(btnrow4, text='6', font=("Verdana", 25), relief=GROOVE, border=0, command=six_clicked)
btn3.pack(side=LEFT, expand=True, fill="both", )

btn4 = Button(btnrow4, text='x', font=("Verdana", 25), relief=GROOVE, border=0, command=mul_clicked)
btn4.pack(side=LEFT, expand=True, fill="both", )

btn1 = Button(btnrow5, text='1', font=("Verdana", 25), relief=GROOVE, border=0, command=one_clicked)
btn1.pack(side=LEFT, expand=True, fill="both", )

btn2 = Button(btnrow5, text='2', font=("Verdana", 25), relief=GROOVE, border=0, command=two_clicked)
btn2.pack(side=LEFT, expand=True, fill="both", )

btn3 = Button(btnrow5, text='3', font=("Verdana", 25), relief=GROOVE, border=0, command=three_clicked)
btn3.pack(side=LEFT, expand=True, fill="both", )

btn4 = Button(btnrow5, text='-', font=("Verdana", 25), relief=GROOVE, border=0, command=minus_clicked)
btn4.pack(side=LEFT, expand=True, fill="both", )

btn1 = Button(btnrow6, text='0', font=("Verdana", 25), relief=GROOVE, border=0, command=zero_clicked)
btn1.pack(side=LEFT, expand=True, fill="both", )

btn2 = Button(btnrow6, text='.', font=("Verdana", 25), relief=GROOVE, border=0, command=dot_clicked)
btn2.pack(side=LEFT, expand=True, fill="both", )

btn3 = Button(btnrow6, text='=', font=("Verdana", 25), relief=GROOVE, border=0, command=result)
btn3.pack(side=LEFT, expand=True, fill="both", )

btn4 = Button(btnrow6, text='+', font=("Verdana", 25), relief=GROOVE, border=0, command=plus_clicked)
btn4.pack(side=LEFT, expand=True, fill="both", )

mainloop()