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
        if "." in input.get():
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

def arithmetic_operation(operator, a):
    equals = False
    # Infinite loop problem
    while equals == False:
        if event == "0":
            update_input("0", True)
        if event == "1":
            update_input("1", True)
        if event == "2":
            update_input("2", True)
        if event == "3":
            update_input("3", True)
        if event == "4":
            update_input("4", True)
        if event == "5":
            update_input("5", True)
        if event == "6":
            update_input("6", True)
        if event == "7":
            update_input("7", True)
        if event == "8":
            update_input("8", True)
        if event == "9":
            update_input("9", True)
        if event == "+":
            update_input("+", True)
        if event == "-":
            update_input("-", True)
        if event == "*":
            update_input("*", True)
        if event == "/":
            update_input("/", True)
        if event == ".":
            update_input(".", True)
        if event == "equals":
            equals = True

    b = float(input.get())

    if operator == "+":
        return calc.add(a, b)
    if operator == "-":
        return calc.subtract(a, b)
    if operator == "*":
        return calc.multiply(a, b)
    if operator == "/":
        return calc.divide(a, b)

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
        calc.recall()
    if event == "M+":
        calc.store(input.get())
    if event == "M-":
        calc.delete()
    if event == "MS":
        calc.store(input.get())
    if event == "CE":
        delete_last()
    if event == "C":
        input.update(value="0")
    if event == "\u2190":
        delete_last()

    # Mathematic operators
    if event == "%":
        input.update(str(calc.multiply(float(input.get()), 0.01)))
    if event == "1/x":
        input.update(str(calc.frac(float(input.get()))))
    if event == "x²":
        input.update(str(calc.square(float(input.get()))))
    if event == "√x":
        input.update(str(calc.root(float(input.get()))))
    if event == "/":
        pass #calc.divide(calc.read(), calc.read())
    if event == "-":
        pass #calc.subtract(calc.read(), calc.read())
    if event == "*":
        pass #calc.multiply(calc.read(), calc.read())
    if event == "+":
        input.update(str(arithmetic_operation("+", float(input.get()))))
    if event == "+/-":
        input.update(str(calc.multiply(float(input.get()), -1)))
    if event == ".":
        update_input(".")

    # in_valuebers
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