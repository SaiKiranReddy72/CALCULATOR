from tkinter import *

calc = Tk()
calc.title('Simple Calculator')
calc.configure(bg='white')

title_label = Label(calc, text='My Simple Calculator', font=('Arial', 16), bg='white')
title_label.grid(row=0, column=0, columnspan=4, pady=10)

eq = StringVar()

entry = Entry(calc, textvariable=eq, font=('Arial', 21), bd=10, insertwidth=4, width=14, justify='right')
entry.grid(row=0, column=0, columnspan=4)

exp = ''


def on_click(t):
    global exp
    exp = exp + str(t)
    eq.set(exp)


def equal():
    global exp
    try:
        result = str(eval(exp))
        exp = result
        eq.set(exp)
    except:
        eq.set('Math Error')
        exp = ''


def clear():
    global exp
    exp = ''
    eq.set(exp)


def one_clear():
    global exp
    exp = ''
    eq.set('')


buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'DEL', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    if button == '=':
        btn = Button(calc, text=button, activebackground='pink', width=10, height=2, bg='green', fg='white',
                     command=lambda: equal())
    elif button == 'DEL':
        btn = Button(calc, text=button, activebackground='pink', width=10, height=2, bg='green', fg='white',
                     command=lambda: one_clear())
    else:
        btn = Button(calc, text=button, activebackground='pink', width=10, height=2, bg='lightgray', fg='black',
                     command=lambda b=button: on_click(b))

    btn.grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

calc.mainloop()