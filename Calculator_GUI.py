# Calculator GUI
import PySimpleGUI as sg
import Calculations

sg.set_options(font="Arial 12")

layout = [
    [sg.In(size=(25, 4), enable_events=True, key="-INPUT-", readonly=True, default_text="0", pad=(0, 5), justification="right")],
    [sg.Button("MC", tooltip="Clear All Memory", expand_x=True), sg.Button("MR", tooltip="Memory Recall", expand_x=True), sg.Button("M+", tooltip="Add to Memory", expand_x=True), sg.Button("M-", tooltip="Subtract from Memory", expand_x=True), sg.Button("MS", tooltip="Save to Memory", expand_x=True)],
    [sg.Button("%", expand_x=True), sg.Button("CE", tooltip="Clear Last Entry", expand_x=True), sg.Button("C", tooltip="Clear", expand_x=True), sg.Button("\u2190", tooltip="Backspace", expand_x=True)],
    [sg.Button("1/x", expand_x=True), sg.Button("x²", expand_x=True), sg.Button("√x", expand_x=True), sg.Button("/", expand_x=True)],
    [sg.Button("7", expand_x=True), sg.Button("8", expand_x=True), sg.Button("9", expand_x=True), sg.Button("*", expand_x=True)],
    [sg.Button("4", expand_x=True), sg.Button("5", expand_x=True), sg.Button("6", expand_x=True), sg.Button("-", expand_x=True)],
    [sg.Button("1", expand_x=True), sg.Button("2", expand_x=True), sg.Button("3", expand_x=True), sg.Button("+", expand_x=True)],
    [sg.Button("+/-", expand_x=True), sg.Button("0", expand_x=True), sg.Button(".", expand_x=True), sg.Button("=", expand_x=True)],
    ]
window = sg.Window(title="Calculator", layout=layout, margins=(7, 7), element_padding=(1, 1))

while True:
    event, values = window.read()
    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close()