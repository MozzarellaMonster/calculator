# Calculator GUI
import PySimpleGUI as sg
import Calculations

# Create the calculator
calc = Calculations.Calc()

# Define the window layout
sg.set_options(font="Arial 12")

input = sg.In(size=(25, 4), enable_events=True, key="input", readonly=True, default_text="0", pad=(0, 5), justification="right")

layout = [
    [input],
    [sg.Button("MC", tooltip="Clear All Memory", expand_x=True), sg.Button("MR", tooltip="Memory Recall", expand_x=True), sg.Button("M+", tooltip="Add to Memory", expand_x=True), sg.Button("M-", tooltip="Subtract from Memory", expand_x=True), sg.Button("MS", tooltip="Save to Memory", expand_x=True)],
    [sg.Button("%", expand_x=True), sg.Button("CE", tooltip="Clear Last Entry", expand_x=True), sg.Button("C", tooltip="Clear", expand_x=True), sg.Button("\u2190", tooltip="Backspace", expand_x=True)],
    [sg.Button("1/x", expand_x=True), sg.Button("x²", expand_x=True), sg.Button("√x", expand_x=True), sg.Button("/", expand_x=True)],
    [sg.Button("7", expand_x=True), sg.Button("8", expand_x=True), sg.Button("9", expand_x=True), sg.Button("*", expand_x=True)],
    [sg.Button("4", expand_x=True), sg.Button("5", expand_x=True), sg.Button("6", expand_x=True), sg.Button("-", expand_x=True)],
    [sg.Button("1", expand_x=True), sg.Button("2", expand_x=True), sg.Button("3", expand_x=True), sg.Button("+", expand_x=True)],
    [sg.Button("+/-", expand_x=True), sg.Button("0", expand_x=True), sg.Button(".", expand_x=True), sg.Button("=", expand_x=True)],
    ]

window = sg.Window(title="Calculator", layout=layout, margins=(7, 7), element_padding=(1, 1))

# Helper functions
def update_input(in_value, in_math_op=False):
    if in_math_op:
        input.update(value="0")
    if input.get() == "0":
        input.update(value=in_value)
    elif in_value == ".":
        if dec_in_input():
            pass
        else:
            input.update(value=input.get() + in_value)
    else:
        input.update(value=input.get() + in_value)

def delete_last():
    if len(input.get()) == 1:
        input.update(value="0")
    else:
        input.update(value=input.get()[:-1])

def add_to_mem():
    if dec_in_input():
        calc.store(float(input.get()))
    else:
        calc.store(int(input.get()))

def arithmetic(op):
    if op == "+":
        if calc.get_temp() is not None:
            if dec_in_input():
                input.update(str(calc.add(calc.get_temp(), float(input.get()))))
            else:
                input.update(str(calc.add(calc.get_temp(), int(input.get()))))
        else:
            if dec_in_input():
                calc.set_temp(float(input.get()))
            else:    
                calc.set_temp(int(input.get()))
            calc.op = "+"
            
    if op == "-":
        if calc.get_temp() is not None:
            if dec_in_input():
                input.update(str(calc.subtract(calc.get_temp(), float(input.get()))))
            else:
                input.update(str(calc.subtract(calc.get_temp(), int(input.get()))))
        else:
            if dec_in_input():
                calc.set_temp(float(input.get()))
            else:    
                calc.set_temp(int(input.get()))
            calc.op = "-"
    if op == "*":
        if calc.get_temp() is not None:
            if dec_in_input():
                input.update(str(calc.multiply(calc.get_temp(), float(input.get()))))
            else:
                input.update(str(calc.multiply(calc.get_temp(), int(input.get()))))
        else:
            if dec_in_input():
                calc.set_temp(float(input.get()))
            else:
                calc.set_temp(int(input.get()))
            calc.op = "*"
    if op == "/":
        if calc.get_temp() is not None:
            if dec_in_input():
                input.update(str(calc.divide(calc.get_temp(), float(input.get()))))
            else:
                input.update(str(calc.divide(calc.get_temp(), int(input.get()))))
        else:
            if dec_in_input():
                calc.set_temp(float(input.get()))
            else:
                calc.set_temp(int(input.get()))
            calc.op = "/"
    input.update(value="0")

def dec_in_input():
    return "." in input.get()


# Event loop
while True:
    event, values = window.read()
    
    # Close button
    if event == sg.WIN_CLOSED:
        break

    # Special Keys
    if event == "MC":
        calc.clear()

    if event == "MR":
        input.update(str(calc.recall()))

    if event == "M+":
        add_to_mem()

    if event == "M-":
        calc.delete()

    if event == "MS":
        add_to_mem()

    if event == "CE":
        delete_last()

    if event == "C":
        input.update(value="0")

    if event == "\u2190":
        delete_last()

    # Mathematic operators
    if event == "%":
        if dec_in_input():
            input.update(str(calc.multiply(float(input.get()), 0.01)))    
        else:
            input.update(str(calc.multiply(int(input.get()), 0.01)))

    if event == "1/x":
        if dec_in_input():
            input.update(str(calc.frac(float(input.get()))))
        else:
            input.update(str(calc.frac(int(input.get()))))

    if event == "x²":
        if dec_in_input():
            input.update(str(calc.square(float(input.get()))))    
        else:
            input.update(str(calc.square(int(input.get()))))

    if event == "√x":
        if dec_in_input():
            input.update(str(calc.root(float(input.get()))))
        else:
            input.update(str(calc.root(int(input.get()))))

    if event == "/":
        arithmetic("/")

    if event == "-":
        arithmetic("-")

    if event == "*":
        arithmetic("*")

    if event == "+":
        arithmetic("+")

    if event == "+/-":
        if dec_in_input():
            input.update(str(calc.multiply(float(input.get()), -1)))
        else:    
            input.update(str(calc.multiply(int(input.get()), -1)))

    if event == "=":
        if calc.op == "+":
            if type(calc.get_temp()) == float:
                input.update(str(calc.add(calc.get_temp(), float(input.get()))))
            else:
                input.update(str(calc.add(calc.get_temp(), int(input.get()))))
        if calc.op == "-":
            if type(calc.get_temp()) == float:
                input.update(str(calc.subtract(calc.get_temp(), float(input.get()))))
            else:
                input.update(str(calc.subtract(calc.get_temp(), int(input.get()))))
        if calc.op == "*":
            if type(calc.get_temp()) == float:
                input.update(str(calc.multiply(calc.get_temp(), float(input.get()))))
            else:
                input.update(str(calc.multiply(calc.get_temp(), int(input.get()))))
        if calc.op == "/":
            if type(calc.get_temp()) == float:
                input.update(str(calc.divide(calc.get_temp(), float(input.get()))))
            else:
                input.update(str(calc.divide(calc.get_temp(), int(input.get()))))
        calc.set_temp(None)
        calc.op = None

    if event == ".":
        update_input(".")

    # Numbers
    if event == "0":
        update_input("0")

    if event == "1":
        update_input("1")

    if event == "2":
        update_input("2")

    if event == "3":
        update_input("3")

    if event == "4":
        update_input("4")

    if event == "5":
        update_input("5")

    if event == "6":
        update_input("6")

    if event == "7":
        update_input("7")

    if event == "8":
        update_input("8")

    if event == "9":
        update_input("9")

window.close()