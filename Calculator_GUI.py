# Calculator GUI
import PySimpleGUI as sg
import Calculations

# Create the calculator
calc = Calculations.Calc()

# Define the window layout
sg.set_options(font="Arial 12")

input = sg.Input(size=(25, 4), enable_events=True, key="input", readonly=True, default_text="0", pad=(0, 5), justification="right")

layout = [
    [input],
    [sg.Button("MC", tooltip="Clear All Memory", expand_x=True, button_color="#4169E1"), sg.Button("MR", tooltip="Memory Recall", expand_x=True, button_color="#4169E1"), sg.Button("M+", tooltip="Add to Memory", expand_x=True, button_color="#4169E1"), sg.Button("M-", tooltip="Subtract from Memory", expand_x=True, button_color="#4169E1"), sg.Button("MS", tooltip="Save to Memory", expand_x=True, button_color="#4169E1")],
    [sg.Button("%", expand_x=True), sg.Button("CE", tooltip="Clear Last Entry", expand_x=True), sg.Button("C", tooltip="Clear", expand_x=True), sg.Button("\u2190", tooltip="Backspace", expand_x=True, button_color="gray")],
    [sg.Button("1/x", expand_x=True), sg.Button("x²", expand_x=True), sg.Button("√x", expand_x=True), sg.Button("/", expand_x=True)],
    [sg.Button("7", expand_x=True), sg.Button("8", expand_x=True), sg.Button("9", expand_x=True), sg.Button("*", expand_x=True)],
    [sg.Button("4", expand_x=True), sg.Button("5", expand_x=True), sg.Button("6", expand_x=True), sg.Button("-", expand_x=True)],
    [sg.Button("1", expand_x=True), sg.Button("2", expand_x=True), sg.Button("3", expand_x=True), sg.Button("+", expand_x=True)],
    [sg.Button("+/-", expand_x=True), sg.Button("0", expand_x=True), sg.Button(".", expand_x=True), sg.Button("=", expand_x=True, button_color="orange")]
    ]

window = sg.Window(title="Calculator", layout=layout, margins=(7, 7), element_padding=(1, 1), auto_size_buttons=True, grab_anywhere=True, auto_size_text=True, resizable=True, icon="calculator.ico")

# Helper functions
def update_input(in_value): # Updates input for numeric button presses
    if calc.in_operation:
        input.update(value=in_value)
        calc.in_operation = False
    else:
        if input.get() == "0":
            input.update(value=in_value)
        elif in_value == "." and dec_in_input():
            pass
        else:
            input.update(value=input.get() + in_value)

def delete_last(): # Deletes last character in input
    if len(input.get()) == 1:
        input.update(value="0")
    else:
        input.update(value=input.get()[:-1])

def add_to_mem(): # Adds current input to memory
    if dec_in_input():
        calc.store(float(input.get()))
    else:
        calc.store(int(input.get()))

def arithmetic(op): # Performs arithmetic operation
    if calc.in_operation:
        if calc.op != op:
            calc.op = op
        else:
            pass
    else:
        if op == "+":
            func = calc.add
        elif op == "-":
            func = calc.subtract
        elif op == "*":
            func = calc.multiply
        elif op == "/":
            func = calc.divide

        if calc.op is not None and calc.get_temp() is not None:
            if calc.op == "+":
                old_func = calc.add
            elif calc.op == "-":
                old_func = calc.subtract
            elif calc.op == "*":
                old_func = calc.multiply
            elif calc.op == "/":
                old_func = calc.divide

            if dec_in_input():
                calc.set_temp(old_func(calc.get_temp(), float(input.get())))
            else:
                calc.set_temp(old_func(calc.get_temp(), int(input.get())))
            input.update(value=str(calc.get_temp()))

        elif calc.op is None and calc.get_temp() is not None:
            if dec_in_input():
                input.update(str(func(calc.get_temp(), float(input.get()))))
            else:
                input.update(str(func(calc.get_temp(), int(input.get()))))

        else:
            if dec_in_input():
                calc.set_temp(float(input.get()))
            else:
                calc.set_temp(int(input.get()))

        calc.in_operation = True
        calc.op = op

def special_op(op): # Performs special operations
    if op == "1/x":
        func = calc.frac
    if op == "x²":
        func = calc.square
    if op == "√x":
        func = calc.root
    
    if dec_in_input():
        input.update(str(func(float(input.get()))))
    else:
        input.update(str(func(int(input.get()))))

def equals(): # Performs equals operation
    if calc.op == "+":
        func = calc.add
    if calc.op == "-":
        func = calc.subtract
    if calc.op == "*":
        func = calc.multiply
    if calc.op == "/":
        func = calc.divide
    
    if calc.get_temp() is not None:
        if type(calc.get_temp()) == float:
            input.update(str(func(calc.get_temp(), float(input.get()))))
        else:
            input.update(str(func(calc.get_temp(), int(input.get()))))
    else:
        if dec_in_input():
            calc.set_temp(float(input.get()))
        else:
            calc.set_temp(int(input.get()))

    calc.in_operation = False
    calc.set_temp(None)
    calc.op = None

def dec_in_input(): # Checks if decimal is in input
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
        calc.in_operation = False
        calc.op = None
        input.update(value="0")
        calc.set_temp(None)

    if event == "\u2190":
        delete_last()

    # Mathematic operators
    if event == "%":
        if dec_in_input() or "e" in input.get():
            input.update(str(calc.multiply(float(input.get()), 0.01)))    
        else:
            input.update(str(calc.multiply(int(input.get()), 0.01)))
    
    if event == "+/-":
        if dec_in_input():
            input.update(str(calc.multiply(float(input.get()), -1)))
        else:    
            input.update(str(calc.multiply(int(input.get()), -1)))

    if event == "1/x":
        special_op("1/x")

    if event == "x²":
        special_op("x²")

    if event == "√x":
        special_op("√x")

    if event == "/":
        arithmetic("/")

    if event == "-":
        arithmetic("-")

    if event == "*":
        arithmetic("*")

    if event == "+":
        arithmetic("+")

    if event == "=":
        equals()

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