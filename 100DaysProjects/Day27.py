#Day 27 Project: Mile to Kilometers Converter

import tkinter

screen =tkinter.Tk()
screen.title("Mile to Km Converter")
screen.minsize(width=300, height=300)
screen.config(padx= 100, pady= 150)



label_equal_to = tkinter.Label(text="is equal to", font=("Arial", 10, "bold"))
label_equal_to.grid(column=0, row=1)

input = tkinter.Entry(width=10)
input.insert(10, string= 0)
input.grid(column=1, row=0)


result = tkinter.Label(text= 0)
result.grid(column=1, row=1)


def calculate():
    Miles = input.get()
    Km = int(Miles) * 1.60934
    result.config(text= Km)
    print(Miles)


button = tkinter.Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)

Label_miles = tkinter.Label(text= "Miles") 
Label_miles.grid(column= 2, row=0)

Label_km = tkinter.Label(text= "Km")
Label_km.grid(column= 2, row=1)



screen.mainloop()