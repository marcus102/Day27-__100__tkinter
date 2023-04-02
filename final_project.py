from tkinter import *

window = Tk()
window.title('MILES to KM')
window.minsize(width=600, height=300)
window.config(padx=20, pady=20)

input = Entry()
input.config(width=20, )
input.place(x=200, y=20) 

mile = Label(text='Miles', font=('arial', 10, 'bold'))
mile.place(x=350, y=20)

km1 = Label(text='is equel to', font=('arial', 10, 'bold'))
km1.place(x=100, y=80)

km2 = Label(text='0', font=('arial', 10, 'bold'))
km2.place(x=250, y=80)

def converter():
  recieved_input = float(input.get())
  result = recieved_input * 1.609344
  km2.config(text=round(result, 2))

km3 = Label(text='KM', font=('arial', 10, 'bold'))
km3.place(x=350, y=80)

button = Button(text='Calculate', font=('arial', 10, 'bold'), command=converter)
button.place(x=230, y=140)

window.mainloop()