import tkinter
from GoldPrices import goldprices

def graph():
    start_date = dates_entry.get()
    end_date = datee_entry.get()
    return goldprices.GoldPrices().draw_graph(goldprices.GoldPrices().goldprice_daterange, start_date, end_date)

root = tkinter.Tk()
root.title('Gold prices')

header = tkinter.Label(master=root, text="Enter dates")
header.grid(row=0, column=0, columnspan=3)
dates_label = tkinter.Label(master=root, text='From:')
dates_label.grid(row=1, column=0)
dates_entry = tkinter.Entry(master=root)
dates_entry.grid(row=1, column=1, columnspan=2)
datee_label = tkinter.Label(master=root, text='To:')
datee_label.grid(row=2, column=0)
datee_entry = tkinter.Entry(master=root)
datee_entry.grid(row=2, column=1, columnspan=2)

c_price = tkinter.Label(master=root, text=goldprices.GoldPrices().goldprice_today())
c_price.grid(row=4, column=0, columnspan=3)

showbutton = tkinter.Button(master=root, text='SHOW', command=graph)
showbutton.grid(row=3, column=0, columnspan=3)

root.mainloop()

