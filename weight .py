# weight converter using Tkinter 
from tkinter import *
window = Tk()
def from_kg():
    GRAM = float(e2_value.get())*1000
    POUND = float(e2_value.get())*2.20462
    OUNCE = float(e2_value.get())*35.274
    TON     =     float(e2_value.get())*2000
    MILIGRAM= float(e2_value.get())*0.001
    t1.delete("1.0", END)
    t1.insert(END,GRAM)
    t2.delete("1.0", END)
    t2.insert(END,POUND)
    t3.delete("1.0", END)
    t3.insert(END,OUNCE) 
    t4.delete("1.0",END)
    t4.insert(END,TON)
    t5.delete("1.0" ,END)
    t5.insert(END,MILIGRAM)
e1 = Label(window, text = "Enter the weight in Kg")
e2_value = StringVar()
e2 = Entry(window, textvariable = e2_value)
e3 = Label(window, text = 'GRAM',bg="yellow",fg="black")
e4 = Label(window, text = 'POUNDS',
bg="yellow",fg="black")
e5 = Label(window, text = 'OUNCE',bg="yellow",fg="black")
e6 = Label(window,text = 'TON',bg="yellow",fg="black")
e7 = Label(window,text="MILIGRAM",bg="yellow",fg="black")
t1 = Text(window, height = 1, width = 5)
t2 = Text(window, height = 1, width = 5)
t3 = Text(window, height = 1, width = 5)
t4 = Text(window, height = 1, width = 5)
t5=Text(window, height =1,width = 6)
b1 = Button(window, text = "CONVERT",bg="black",fg="red",command = from_kg)
e1.grid(row = 0, column = 0)
e2.grid(row = 0, column = 1)
e3.grid(row = 1, column = 0)
e4.grid(row = 1, column = 1)
e5.grid(row = 1, column = 2)
e6.grid(row = 1,column = 3)
e7.grid(row =1, column =7)
t1.grid(row = 2, column = 0)
t2.grid(row = 2, column = 1)
t3.grid(row = 2, column = 2)
t4.grid(row = 2, column = 3)
t5.grid(row =2, column = 7)
b1.grid(row = 0, column = 2) 
# Start the GUI 
window.mainloop()