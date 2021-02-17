from tkinter import *

expression = ""
def press(num):
    
    global expression

    expression = expression + str(num)
    equation.set(expression)

def equalpress():

    try:

        global expression
        total = str(eval(expression))

        equation.set(total)
        expression = ""

    except:

        equation.set(" error ")
        expression = ""
def clear():
    global expression
    expression = ""
    equation.set("")

if __name__ == "__main__":
    
    cal = Tk()

    cal.configure(background="light blue")

    cal.title("Calculator")
    
    cal.geometry("250x300")

    equation = StringVar()
    
    expression_field = Entry(cal, textvariable=equation)

    expression_field.grid(columnspan=1700, ipadx=1800)
    
    button1 = Button(cal, text=' 1 ', fg='black', bg='light pink',
                    command=lambda: press(1), height=3, width=7)
    button1.grid(row=1, column=0)

    button2 = Button(cal, text=' 2 ', fg='black', bg='light pink',
                    command=lambda: press(2), height=3, width=7)
    button2.grid(row=1, column=1)

    button3 = Button(cal, text=' 3 ', fg='black', bg='light pink',
                    command=lambda: press(3), height=3, width=7)
    button3.grid(row=1, column=2)

    button4 = Button(cal, text=' 4 ', fg='black', bg='light pink',
                    command=lambda: press(4), height=3, width=7)
    button4.grid(row=3, column=0)

    button5 = Button(cal, text=' 5 ', fg='black', bg='light pink',
                    command=lambda: press(5), height=3, width=7)
    button5.grid(row=3, column=1)

    button6 = Button(cal, text=' 6 ', fg='black', bg='light pink',
                    command=lambda: press(6), height=3, width=7)
    button6.grid(row=3, column=2)

    button7 = Button(cal, text=' 7 ', fg='black', bg='light pink',
                    command=lambda: press(7), height=3, width=7)
    button7.grid(row=4, column=0)

    button8 = Button(cal, text=' 8 ', fg='black', bg='light pink',
                    command=lambda: press(8), height=3, width=7)
    button8.grid(row=4, column=1)

    button9 = Button(cal, text=' 9 ', fg='black', bg='light pink',
                    command=lambda: press(9), height=3, width=7)
    button9.grid(row=4, column=2)

    button0 = Button(cal, text=' 0 ', fg='black', bg='light pink',
                    command=lambda: press(0), height=3, width=7)
    button0.grid(row=5, column=0)

    plus = Button(cal, text=' + ', fg='black', bg='light pink',
                command=lambda: press("+"), height=3, width=7)
    plus.grid(row=1, column=3)

    minus = Button(cal, text=' - ', fg='black', bg='light pink',
                command=lambda: press("-"), height=3, width=7)
    minus.grid(row=3, column=3)

    multiply = Button(cal, text=' * ', fg='black', bg='light pink',
                    command=lambda: press("*"), height=3, width=7)
    multiply.grid(row=4, column=3)

    divide = Button(cal, text=' / ', fg='black', bg='light pink',
                    command=lambda: press("/"), height=3, width=7)
    divide.grid(row=5, column=3)

    equal = Button(cal, text=' = ', fg='black', bg='light pink',
                command=equalpress, height=3, width=7)
    equal.grid(row=5, column=2)

    clear = Button(cal, text='Clear', fg='black', bg='light pink',
                command=clear, height=3, width=7)
    clear.grid(row=5, column='1')

    Decimal= Button(cal, text='.', fg='black', bg='light pink',
                    command=lambda: press('.'), height=3, width=7)
    Decimal.grid(row=6, column=0)
    
    cal.mainloop()
    