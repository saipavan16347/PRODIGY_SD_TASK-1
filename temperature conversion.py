import tkinter as tk
from functools import partial

def store_temp(sel_temp):
    global tempVal
    tempVal = sel_temp

def call_convert(rlabel1, rlabel2, inputn):
    tem = inputn.get()
    if not tem:
        rlabel1.config(text="Please enter a temperature.")
        rlabel2.config(text="")
        return
    try:
        tem_float = float(tem)
        if tempVal == 'Celsius':
            f = (tem_float * 9 / 5) + 32
            k = tem_float + 273.15
            rlabel1.config(text="%.2f Fahrenheit" % f)
            rlabel2.config(text="%.2f Kelvin" % k)
        elif tempVal == 'Fahrenheit':
            c = (tem_float - 32) * 5 / 9
            k = c + 273.15
            rlabel1.config(text="%.2f Celsius" % c)
            rlabel2.config(text="%.2f Kelvin" % k)
        elif tempVal == 'Kelvin':
            c = tem_float - 273.15
            f = (tem_float - 273.15) * 1.8 + 32
            rlabel1.config(text="%.2f Celsius" % c)
            rlabel2.config(text="%.2f Fahrenheit" % f)
    except ValueError:
        rlabel1.config(text="Invalid input. Please enter a number.")
        rlabel2.config(text="")

root = tk.Tk()
root.geometry('500x350+350+200')
root.title('Temperature Converter')
root.configure(background='#09A3BA')
root.resizable(width=False, height=False)

numberInput = tk.StringVar()
var = tk.StringVar()
tempVal = "Celsius" #initial value

input_label = tk.Label(root, text="Enter temperature", background='#09A3BA', foreground="#FFFFFF")
input_entry = tk.Entry(root, textvariable=numberInput)
input_label.grid(row=1, column=0, padx=5, pady=5)
input_entry.grid(row=1, column=1, padx=5, pady=5)

result_label_title = tk.Label(root, text="Converted to:", background='#09A3BA', foreground="#FFFFFF")
result_label_title.grid(row=2, columnspan=2)

result_label1 = tk.Label(root, background='#09A3BA', foreground="#FFFFFF")
result_label1.grid(row=3, columnspan=2)
result_label2 = tk.Label(root, background='#09A3BA', foreground="#FFFFFF")
result_label2.grid(row=4, columnspan=2)

dropDownList = ["Celsius", "Fahrenheit", "Kelvin"]
dropdown = tk.OptionMenu(root, var, *dropDownList, command=store_temp)
var.set(dropDownList[0])
dropdown.grid(row=1, column=2, padx=5, pady=5)
dropdown.config(background='#09A3BA', foreground="#FFFFFF")
dropdown["menu"].config(background='#09A3BA', foreground="#FFFFFF")

call_convert = partial(call_convert, result_label1, result_label2, numberInput)
result_button = tk.Button(root, text="Convert", command=call_convert, background='#09A3BA', foreground="#FFFFFF")
result_button.grid(row=5, columnspan=3, padx=5, pady=5)

root.mainloop()
