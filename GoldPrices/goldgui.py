import tkinter
from PIL import Image, ImageTk
from GoldPrices import goldprices

def last(days):
    goldprices.GoldPrices().draw_graph(goldprices.GoldPrices().goldprice_last_days, days)
    image = Image.open('graph.jpg')
    graph_img = ImageTk.PhotoImage(image)
    display = tkinter.Label(image=graph_img)
    display.image = graph_img
    display.grid(row=1, column=0, columnspan=4)

root = tkinter.Tk()
today = goldprices.GoldPrices().goldprice_today()
root.title(f'Gold prices. {today}')

last3 = tkinter.Button(master=root, text='Last 3 days', command=lambda: last(3), width=17)
last3.grid(row=0, column=0)
last10 = tkinter.Button(master=root, text='Last 10 days', command=lambda: last(10), width=17)
last10.grid(row=0, column=1)
last30 = tkinter.Button(master=root, text='Last 30 days', command=lambda: last(30), width=17)
last30.grid(row=0, column=2)
last90 = tkinter.Button(master=root, text='Last 90 days', command=lambda: last(90), width=17)
last90.grid(row=0, column=3)

root.mainloop()

