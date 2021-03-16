from tkinter import *


def mileTOKm():
    miles = float(mileInput.get())
    km = miles *1.609
    kmLabel.config(text=f"{km}")
window = Tk()
window.title('Miles to Kilometer Converter')
window.config(padx=20,pady=20)

mileInput  = Entry(width=7)
mileLabel = Label(text='Miles')

is_equal = Label(text='is equal to')
kmLabel = Label(text='0')
klabel = Label(text='Km')

cal_button = Button(text='Calculate',command=mileTOKm)

mileInput.grid(column=1,row=0)
mileLabel.grid(column=2,row=0)
is_equal.grid(column=0,row=1)
kmLabel.grid(column=1,row=1)
klabel.grid(column=2,row=1)
cal_button.grid(column=1,row=2)




window.mainloop()