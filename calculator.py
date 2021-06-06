from tkinter import *

root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=20, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def btClick(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def btClear():
    e.delete(0, END)

def btAdd():
    firstNum = e.get()
    global input
    input = float(firstNum)
    global type 
    type = "add"
    e.delete(0, END)

def btMinus():
    firstNum = e.get()
    global input
    input = float(firstNum)
    global type 
    type = "minus"
    e.delete(0, END)

def btMultiply():
    firstNum = e.get()
    global input
    input = float(firstNum)
    global type 
    type = "multiply"
    e.delete(0, END)

def btDivide():
    firstNum = e.get()
    global input
    input = float(firstNum)
    global type 
    type = "divide"
    e.delete(0, END)

def btEqual():
    secondNum = e.get()
    e.delete(0, END)

    if type == "add":
        e.insert(0, input + float(secondNum))
    elif type == "minus":
        e.insert(0, input - float(secondNum))
    elif type == "multiply":
        e.insert(0, input * float(secondNum))
    elif type == "divide":
        e.insert(0, input / float(secondNum))

bt1 = Button(root, text='1', width=5, pady=10, command=lambda:btClick(1), highlightbackground='#45B0A3', fg='#2F4858')
bt2 = Button(root, text='2', width=5, pady=10, command=lambda:btClick(2), highlightbackground='#45B0A3', fg='#2F4858')
bt3 = Button(root, text='3', width=5, pady=10, command=lambda:btClick(3), highlightbackground='#45B0A3', fg='#2F4858')
bt4 = Button(root, text='4', width=5, pady=10, command=lambda:btClick(4), highlightbackground='#45B0A3', fg='#2F4858')
bt5 = Button(root, text='5', width=5, pady=10, command=lambda:btClick(5), highlightbackground='#45B0A3', fg='#2F4858')
bt6 = Button(root, text='6', width=5, pady=10, command=lambda:btClick(6), highlightbackground='#45B0A3', fg='#2F4858')
bt7 = Button(root, text='7', width=5, pady=10, command=lambda:btClick(7), highlightbackground='#45B0A3', fg='#2F4858')
bt8 = Button(root, text='8', width=5, pady=10, command=lambda:btClick(8), highlightbackground='#45B0A3', fg='#2F4858')
bt9 = Button(root, text='9', width=5, pady=10, command=lambda:btClick(9), highlightbackground='#45B0A3', fg='#2F4858')
bt0 = Button(root, text='0', width=10, pady=10, command=lambda:btClick(0), highlightbackground='#45B0A3', fg='#2F4858')
btadd = Button(root, text='+', width=5, pady=10, command=btAdd, highlightbackground='#ACF4A8', fg='#2F4858')
btequal = Button(root, text='=', width=5, pady=10, command=btEqual, highlightbackground='#ACF4A8', fg='#2F4858')
btclear = Button(root, text='AC', width=5, pady=10, command=btClear, highlightbackground='#71D3A9', fg='#2F4858')
btminus = Button(root, text="-", width=5, pady=10, command=btMinus, highlightbackground='#ACF4A8', fg='#2F4858')
btmul = Button(root, text="×", width=5, pady=10, command=btMultiply, highlightbackground='#ACF4A8', fg='#2F4858')
btdiv = Button(root, text="÷", width=5, pady=10, command=btDivide, highlightbackground='#ACF4A8', fg='#2F4858')
btremainder = Button(root, text="%", width=5, pady=10, command=btDivide, highlightbackground='#71D3A9', fg='#2F4858')
btnegate = Button(root, text="±", width=5, pady=10, command=btDivide, highlightbackground='#71D3A9', fg='#2F4858')
btdot = Button(root, text=".", width=5, pady=10, command=btDivide, highlightbackground='#45B0A3', fg='#2F4858')

btclear.grid(row=1, column=0, sticky="nsew")
btnegate.grid(row=1, column=1, sticky="nsew")
btremainder.grid(row=1, column=2, sticky="nsew")
btdiv.grid(row=1, column=3, sticky="nsew")

bt7.grid(row=2, column=0, sticky="nsew")
bt8.grid(row=2, column=1, sticky="nsew")
bt9.grid(row=2, column=2, sticky="nsew")
btmul.grid(row=2, column=3, sticky="nsew")

bt4.grid(row=3, column=0, sticky="nsew")
bt5.grid(row=3, column=1, sticky="nsew")
bt6.grid(row=3, column=2, sticky="nsew")
btminus.grid(row=3, column=3, sticky="nsew")

bt1.grid(row=4, column=0, sticky="nsew")
bt2.grid(row=4, column=1, sticky="nsew")
bt3.grid(row=4, column=2, sticky="nsew")
btadd.grid(row=4, column=3, sticky="nsew")

bt0.grid(row=5, column=0, columnspan=2, sticky="nsew")
btdot.grid(row=5, column=2, sticky="nsew")
btequal.grid(row=5, column=3, sticky="nsew")

root.resizable(False, False)
root.mainloop()