from tkinter import *

root = Tk()
root.title("Siimple Calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def btClick(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def btClear():
    e.delete(0, END)

def btAdd():
    firstNum = e.get()
    global input
    input = int(firstNum)
    e.delete(0, END)

def btEqual():
    secondNum = e.get()
    e.delete(0, END)
    e.insert(0, input + int(secondNum))

bt1 = Button(root, text='1', padx=40, pady=20, command=lambda:btClick(1))
bt2 = Button(root, text='2', padx=40, pady=20, command=lambda:btClick(2))
bt3 = Button(root, text='3', padx=40, pady=20, command=lambda:btClick(3))
bt4 = Button(root, text='4', padx=40, pady=20, command=lambda:btClick(4))
bt5 = Button(root, text='5', padx=40, pady=20, command=lambda:btClick(5))
bt6 = Button(root, text='6', padx=40, pady=20, command=lambda:btClick(6))
bt7 = Button(root, text='7', padx=40, pady=20, command=lambda:btClick(7))
bt8 = Button(root, text='8', padx=40, pady=20, command=lambda:btClick(8))
bt9 = Button(root, text='9', padx=40, pady=20, command=lambda:btClick(9))
bt0 = Button(root, text='0', padx=40, pady=20, command=lambda:btClick(0))
btadd = Button(root, text='+', padx=40, pady=20, command=btAdd)
btequal = Button(root, text='=', padx=100, pady=20, command=btEqual)
btclear = Button(root, text='Clear', padx=88, pady=20, command=btClear)

bt1.grid(row=3, column=0)
bt2.grid(row=3, column=1)
bt3.grid(row=3, column=2)

bt4.grid(row=2, column=0)
bt5.grid(row=2, column=1)
bt6.grid(row=2, column=2)

bt7.grid(row=1, column=0)
bt8.grid(row=1, column=1)
bt9.grid(row=1, column=2)

bt0.grid(row=4, column=0)
btclear.grid(row=4, column=1, columnspan=2)
btadd.grid(row=5, column=0)
btequal.grid(row=5, column=1, columnspan=2)

root.mainloop()