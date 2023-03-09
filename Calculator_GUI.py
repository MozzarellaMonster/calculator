# Calculator GUI
import PySimpleGUI as sg
import Calculations

layout = [[sg.In(size=(25, 1), enable_events=True, key="-INPUT-")], [sg.Button("OK")]]
window = sg.Window(title="Calculator", layout=layout, margins=(100, 50))

while True:
    event, values = window.read()
    if event == "OK" or even == sg.WIN_CLOSED:
        break

window.close()