import tkinter

root = tkinter.Tk()
root.title('Gold prices')

date_label = tkinter.Label(master=root, text='Date:')
date_label.grid(row=0, column=0)
date_entry = tkinter.Entry(master=root)
date_entry.grid(row=0, column=1, columnspan=2)

showbutton = tkinter.Button(master=root, text='SHOW')
showbutton.grid(row=1, column=0, columnspan=3)

root.mainloop()