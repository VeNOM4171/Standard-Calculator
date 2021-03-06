import tkinter
from tkinter import *
from tkinter import messagebox

root = tkinter.Tk()

root.geometry("400x500+500+100")
root.resizable(0, 0)
root.title("CALCULATOR")
root.iconbitmap('cal_images/logo.ico')
root.wm_attributes('-alpha', '0.9')

val = ''
a = 0.0
b = 0.0
operator = ''
dot_ct = 0
neg_ct = 0


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
    global a
    global operator
    global neg_ct
    global dot_ct

    a = float(val)
    if a<0:
        a = abs(a)
        val = str(a)
    else:
        neg_ct = 1
        val = '-' + str(a)

    data.set(val)
    dot_ct = 1

def sq_root_clicked():
    global val
    global a

    a = float(val)
    a = a ** (1 / 2)
    val = str(a)
    data.set(val)

#change the button.
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
    global a
    global val
    global operator
    val2 = val
    dot_ct = 0

    if operator=='x':
        b = float(val2.split('x')[1])
        ans = (a * b)/100
        val = str(ans)
    elif operator=='/':
        b = float(val2.split('/')[1])
        ans = (a / b) * 100
        val = str(ans)

    data.set(val)
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
    global operator
    global dot_ct

    operator = '/'
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
    global b
    global dot_ct
    dot_ct =1
    val2 = val
    if operator == '+':
        b = float(val2.split('+')[1])
        ans = a + b
        data.set(ans)
        val = str(ans)
    elif operator == '-':
        if neg_ct==1:
            b = float(val2.split('-')[2])
        else:
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
lbl = Label(root, text='Label', anchor=SE, font=("Verdana", 40), textvariable=data, background='#1D1F1E', fg='#ffffff', )

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


onePhoto = PhotoImage(file="cal_images/1.png")
twoPhoto = PhotoImage(file="cal_images/2.png")
threePhoto = PhotoImage(file="cal_images/3.png")
fourPhoto = PhotoImage(file="cal_images/4.png")
fivePhoto = PhotoImage(file="cal_images/5.png")
sixPhoto = PhotoImage(file="cal_images/6.png")
sevenPhoto = PhotoImage(file="cal_images/7.png")
eightPhoto = PhotoImage(file="cal_images/8.png")
ninePhoto = PhotoImage(file="cal_images/9.png")
zeroPhoto = PhotoImage(file="cal_images/zero.png")
dotPhoto = PhotoImage(file="cal_images/dot.png")
equalPhoto = PhotoImage(file="cal_images/equal.png")
plusPhoto = PhotoImage(file="cal_images/plus.png")
minusPhoto = PhotoImage(file="cal_images/minus.png")
multiplyPhoto = PhotoImage(file="cal_images/multiply.png")
dividePhoto = PhotoImage(file="cal_images/divide.png")
modulePhoto = PhotoImage(file="cal_images/module.png")
rootPhoto = PhotoImage(file="cal_images/root.png")
plusMinusPhoto = PhotoImage(file="cal_images/plusMinus.png")
squarePhoto = PhotoImage(file="cal_images/square.png")
delPhoto = PhotoImage(file="cal_images/delete.png")
cPhoto = PhotoImage(file="cal_images/c.png")
oneByXPhoto = PhotoImage(file="cal_images/oneByX.png")
cePhoto = PhotoImage(file="cal_images/ce.png")

btn1 = Button(btnrow1, image=oneByXPhoto, relief=GROOVE, border=0, command=div_x_clicked)
btn1.pack(side=LEFT, expand=True, fill="both", )

btn2 = Button(btnrow1, image=squarePhoto, relief=GROOVE, border=0, command=sq_clicked)
btn2.pack(side=LEFT, expand=True, fill="both", )

btn3 = Button(btnrow1, image=plusMinusPhoto, relief=GROOVE, border=0, command=neg_clicked)
btn3.pack(side=LEFT, expand=True, fill="both", )

btn4 = Button(btnrow1, image=rootPhoto, relief=GROOVE, border=0, command=sq_root_clicked)
btn4.pack(side=LEFT, expand=True, fill="both", )

btn1 = Button(btnrow2, image=cePhoto, relief=GROOVE, border=0, command=ce_clicked)
btn1.pack(side=LEFT, expand=True, fill="both", )

btn2 = Button(btnrow2, image=cPhoto, relief=GROOVE, border=0, command=c_clicked)
btn2.pack(side=LEFT, expand=True, fill="both", )

btn3 = Button(btnrow2, image = delPhoto, relief=GROOVE, border=0, command=del_clicked)
btn3.pack(side=LEFT, expand=True, fill="both", )

btn4 = Button(btnrow2, image=modulePhoto, relief=GROOVE, border=0, command=percent_clicked)
btn4.pack(side=LEFT, expand=True, fill="both", )

btn1 = Button(btnrow3, image=sevenPhoto, relief=GROOVE, border=0, command=seven_clicked)
btn1.pack(side=LEFT, expand=True, fill="both", )

btn2 = Button(btnrow3, image=eightPhoto, relief=GROOVE, border=0, command=eight_clicked)
btn2.pack(side=LEFT, expand=True, fill="both", )

btn3 = Button(btnrow3, image=ninePhoto, relief=GROOVE, border=0, command=nine_clicked)
btn3.pack(side=LEFT, expand=True, fill="both", )

btn4 = Button(btnrow3, image=dividePhoto, relief=GROOVE, border=0, command=div_clicked)
btn4.pack(side=LEFT, expand=True, fill="both", )

btn1 = Button(btnrow4, image=fourPhoto, relief=GROOVE, border=0, command=four_clicked)
btn1.pack(side=LEFT, expand=True, fill="both", )

btn2 = Button(btnrow4, image=fivePhoto, relief=GROOVE, border=0, command=five_clicked)
btn2.pack(side=LEFT, expand=True, fill="both", )

btn3 = Button(btnrow4, image=sixPhoto, relief=GROOVE, border=0, command=six_clicked)
btn3.pack(side=LEFT, expand=True, fill="both", )

btn4 = Button(btnrow4, image=multiplyPhoto, relief=GROOVE, border=0, command=mul_clicked)
btn4.pack(side=LEFT, expand=True, fill="both", )

btn1 = Button(btnrow5, image=onePhoto, relief=GROOVE, border=0, command=one_clicked)
btn1.pack(side=LEFT, expand=True, fill="both", )

btn2 = Button(btnrow5, image=twoPhoto, relief=GROOVE, border=0, command=two_clicked)
btn2.pack(side=LEFT, expand=True, fill="both", )

btn3 = Button(btnrow5, image=threePhoto, relief=GROOVE, border=0, command=three_clicked)
btn3.pack(side=LEFT, expand=True, fill="both", )

btn4 = Button(btnrow5, image=minusPhoto, relief=GROOVE, border=0, command=minus_clicked)
btn4.pack(side=LEFT, expand=True, fill="both", )

btn1 = Button(btnrow6, image=zeroPhoto, relief=GROOVE, border=0, command=zero_clicked)
btn1.pack(side=LEFT, expand=True, fill="both", )

btn2 = Button(btnrow6, image=dotPhoto, relief=GROOVE, border=0, command=dot_clicked)
btn2.pack(side=LEFT, expand=True, fill="both", )

btn3 = Button(btnrow6, image=equalPhoto, relief=GROOVE, border=0, command=result)
btn3.pack(side=LEFT, expand=True, fill="both", )

btn4 = Button(btnrow6, image=plusPhoto, relief=GROOVE, border=0, command=plus_clicked)
btn4.pack(side=LEFT, expand=True, fill="both", )






mainloop()