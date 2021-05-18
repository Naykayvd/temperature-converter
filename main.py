import tkinter as tk
from tkinter import LabelFrame, Button, Entry, END, messagebox,INSERT

window = tk.Tk()
window.geometry("600x400")
window.title("Temperature Converter")

c2f = tk.LabelFrame(window, text="Celsius to Fahrenheit")
c2f.place(x=50, y=60, height=100, width=180)
f2c = tk.LabelFrame(window, text="Fahrenheit to Celsius")
f2c.place(x=300, y=60, height=100, width=180)
celsius = tk.Entry(c2f, state="readonly")
celsius.place(x=40, y=20, width=100)
fahrenheit = tk.Entry(f2c, state="readonly")
fahrenheit.place(x=40, y=20, width=100)
conversion = tk.Entry(window, state="readonly")
conversion.place(x=170, y=300, height=50, width=200)

def convert():
    try:
        if celsius['state'] == "normal":
            convert1 = int(celsius.get()) * 1.8 + 32
            conversion.config(state="normal")
            conversion.insert(INSERT, str(round(convert1, 1)))
    except:
        messagebox.showinfo("ERROR", "Must be numbers")
    try:
        if fahrenheit['state'] == "normal":
            convert2 = (int(fahrenheit.get()) - 32) * (5 / 9)
            conversion.config(state="normal")
            conversion.insert(INSERT, str(round(convert2, 1)))
    except:
        messagebox.showinfo("ERROR", "Must be numbers")


def activate1():
    celsius.config(state="normal")
    fahrenheit.config(state="readonly")


btnactivate = tk.Button(window, text="Activate- C to F", command=activate1)
btnactivate.place(x=70, y=180)


def activate2():
    fahrenheit.config(state="normal")
    celsius.config(state="readonly")


btnactivate2 = tk.Button(window, text="Activate- F to C", command=activate2)
btnactivate2.place(x=320, y=180)

btnConv = tk.Button(window, text="Calculate Conversion", command=convert)
btnConv.place(x=190, y=250)


def clear():
    fahrenheit.delete(0, tk.END)
    celsius.delete(0, tk.END)
    conversion.delete(0, tk.END)


btnclear = tk.Button(window, text="Clear", command=clear)
btnclear.place(x=470, y=300)

btnexit = tk.Button(window, text="Exit Program", command=exit)
btnexit.place(x=450, y=350)

window.mainloop()
