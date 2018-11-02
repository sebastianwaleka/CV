import tkinter
from PIL import Image, ImageTk
from GoldPrices import goldprices

def last_three():
    goldprices.GoldPrices().draw_graph(goldprices.GoldPrices().goldprice_last_days, 3)
    image = Image.open('graph.jpg')
    graph_img = ImageTk.PhotoImage(image)
    return graph_img

def last_ten():
    goldprices.GoldPrices().draw_graph(goldprices.GoldPrices().goldprice_last_days, 10)
    with open('graph.jpg'):
        image = Image.open('graph.jpg')
        graph_img = ImageTk.PhotoImage(image)
    return graph_img

def last_thirty():
    goldprices.GoldPrices().draw_graph(goldprices.GoldPrices().goldprice_last_days, 30)
    image = Image.open('graph.jpg')
    graph_img = ImageTk.PhotoImage(image)
    return graph_img

def last_ninety():
    goldprices.GoldPrices().draw_graph(goldprices.GoldPrices().goldprice_last_days, 90)
    image = Image.open('graph.jpg')
    graph_img = ImageTk.PhotoImage(image)
    return graph_img

root = tkinter.Tk()
root.title('Gold prices - graph')
image = Image.open('graph.jpg')
graph_img = ImageTk.PhotoImage(image)

last3 = tkinter.Button(master=root, text='Last 3 days', command=last_three)
last3.pack()#grid(row=0, column=0)
last10 = tkinter.Button(master=root, text='Last 10 days', command=last_ten)
last10.pack()#grid(row=0, column=1)
last30 = tkinter.Button(master=root, text='Last 30 days', command=last_thirty)
last30.pack()#grid(row=0, column=2)
last90 = tkinter.Button(master=root, text='Last 90 days', command=last_ninety)
last90.pack()#grid(row=0, column=3)

display = tkinter.Label(image=graph_img)
display.image = graph_img
display.pack()#grid(row=1, column=0, columnspan=4)
# graph_img.pack()
# with open('graph.jpg') as graph:
#     graph_img = tkinter.Label(master=root, image=graph)

# # Use PIL (Pillow) to convert the NumPy ndarray to a PhotoImage
# photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(cv_img))
#
# # Add a PhotoImage to the Canvas
# canvas.create_image(0, 0, image=photo, anchor=tkinter.NW)

# header = tkinter.Label(master=root, text="Enter dates")

# dates_label = tkinter.Label(master=root, text='From:')
# dates_label.grid(row=1, column=0)
# dates_entry = tkinter.Entry(master=root)
# dates_entry.grid(row=1, column=1, columnspan=2)
# datee_label = tkinter.Label(master=root, text='To:')
# datee_label.grid(row=2, column=0)
# datee_entry = tkinter.Entry(master=root)
# datee_entry.grid(row=2, column=1, columnspan=2)
#
# c_price = tkinter.Label(master=root, text=goldprices.GoldPrices().goldprice_today())
# c_price.grid(row=4, column=0, columnspan=3)
#
# showbutton = tkinter.Button(master=root, text='SHOW', command=graph)
# showbutton.grid(row=3, column=0, columnspan=3)

# img = tkinter.PhotoImage(open("graph.jpg"))
# panel = tkinter.Label(master=root, image = img)
# panel.pack(side = "bottom", fill = "both", expand = "yes")

root.mainloop()

