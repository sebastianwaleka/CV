'''
GUI - Simple calculator
'''
import tkinter

root = tkinter.Tk()
root.title('Simple calculator')

result = tkinter.Label(master=root, text='Result:')
result.grid(row=0, column=0, columnspan=4)

seven = tkinter.Button(master=root, text='7', command=enter)
seven.grid(row=1, column=1)
eight = tkinter.Button(master=root, text='8', command=enter)
eight.grid(row=1, column=2)
nine = tkinter.Button(master=root, text='9', command=enter)
nine.grid(row=1, column=3)
four = tkinter.Button(master=root, text='4', command=enter)
four.grid(row=2, column=1)
five = tkinter.Button(master=root, text='5', command=enter)
five.grid(row=2, column=2)
six = tkinter.Button(master=root, text='6', command=enter)
six.grid(row=2, column=3)
one = tkinter.Button(master=root, text='1', command=enter)
one.grid(row=3, column=1)
two = tkinter.Button(master=root, text='2', command=enter)
two.grid(row=3, column=2)
three = tkinter.Button(master=root, text='3', command=enter)
three.grid(row=3, column=3)

multiply = tkinter.Button(master=root, text='x')
multiply.grid(row=1, column=4)
multiply.config(width=1)
divide = tkinter.Button(master=root, text='/')
divide.grid(row=2, column=4)
divide.config(width=1)
minus = tkinter.Button(master=root, text='-')
minus.grid(row=3, column=4)
minus.config(width=1)
plus = tkinter.Button(master=root, text='+')
plus.grid(row=4, column=4)
plus.config(width=1)
equal_sign = tkinter.Button(master=root, text='=')
equal_sign.grid(row=4, column=1, columnspan=3)
equal_sign.config(width=10)

root.mainloop()