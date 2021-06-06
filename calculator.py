from tkinter import *

root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=20, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def btClick(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def Clear():
    e.delete(0, END)

def Add():
    firstNum = e.get()
    global input
    input = float(firstNum)
    global type 
    type = "add"
    e.delete(0, END)

def Minus():
    firstNum = e.get()
    global input
    input = float(firstNum)
    global type 
    type = "minus"
    e.delete(0, END)

def Multiply():
    firstNum = e.get()
    global input
    input = float(firstNum)
    global type 
    type = "multiply"
    e.delete(0, END)

def Divide():
    firstNum = e.get()
    global input
    input = float(firstNum)
    global type 
    type = "divide"
    e.delete(0, END)

def Negate():
    firstNum = e.get()
    if len(firstNum) == 0:
        e.insert(0, "-")
    elif len(firstNum) == 1 and firstNum[0] == '-':
        e.delete(0, END)
    else:
        e.delete(0, END)
        e.insert(0, float(firstNum) * -1)

def Percentage():
    firstNum = e.get()
    if len(firstNum) == 0:
        return
    elif len(firstNum) == 1 and firstNum[0] == '-':
        return
    else:
        e.delete(0, END)
        e.insert(0, float(firstNum) / 100)

def Dot():
    firstNum = e.get()
    if len(firstNum) == 0:
        e.insert(0, '0.')
        return
    for i in range (0, len(firstNum)):
        if firstNum[i] == '.':
            return
    e.delete(0, END)
    e.insert(0, firstNum + '.')

def Equal():
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

# make buttons
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
btAdd = Button(root, text='+', width=5, pady=10, command=Add, highlightbackground='#ACF4A8', fg='#2F4858')
btEqual = Button(root, text='=', width=5, pady=10, command=Equal, highlightbackground='#ACF4A8', fg='#2F4858')
btClear = Button(root, text='AC', width=5, pady=10, command=Clear, highlightbackground='#71D3A9', fg='#2F4858')
btMinus = Button(root, text="-", width=5, pady=10, command=Minus, highlightbackground='#ACF4A8', fg='#2F4858')
btMul = Button(root, text="×", width=5, pady=10, command=Multiply, highlightbackground='#ACF4A8', fg='#2F4858')
btDiv = Button(root, text="÷", width=5, pady=10, command=Divide, highlightbackground='#ACF4A8', fg='#2F4858')
btPercentage = Button(root, text="%", width=5, pady=10, command=Percentage, highlightbackground='#71D3A9', fg='#2F4858')
btNegate = Button(root, text="±", width=5, pady=10, command=Negate, highlightbackground='#71D3A9', fg='#2F4858')
btDot = Button(root, text=".", width=5, pady=10, command=Dot, highlightbackground='#45B0A3', fg='#2F4858')

# place buttons

# row 1
btClear.grid(row=1, column=0, sticky="nsew")
btNegate.grid(row=1, column=1, sticky="nsew")
btPercentage.grid(row=1, column=2, sticky="nsew")
btDiv.grid(row=1, column=3, sticky="nsew")

# row 2
bt7.grid(row=2, column=0, sticky="nsew")
bt8.grid(row=2, column=1, sticky="nsew")
bt9.grid(row=2, column=2, sticky="nsew")
btMul.grid(row=2, column=3, sticky="nsew")

# row 3
bt4.grid(row=3, column=0, sticky="nsew")
bt5.grid(row=3, column=1, sticky="nsew")
bt6.grid(row=3, column=2, sticky="nsew")
btMinus.grid(row=3, column=3, sticky="nsew")

# row 4
bt1.grid(row=4, column=0, sticky="nsew")
bt2.grid(row=4, column=1, sticky="nsew")
bt3.grid(row=4, column=2, sticky="nsew")
btAdd.grid(row=4, column=3, sticky="nsew")

# row 5
bt0.grid(row=5, column=0, columnspan=2, sticky="nsew")
btDot.grid(row=5, column=2, sticky="nsew")
btEqual.grid(row=5, column=3, sticky="nsew")

root.resizable(False, False)
root.mainloop()