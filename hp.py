import PySimpleGUI as sg

sg.theme("DarkRed2")
layout = [[sg.Text("HP: "), sg.Spin(values=[i for i in range(0, 1000)], initial_value=13, size=(4,1))]]

window = sg.Window("HP", layout, keep_on_top=True)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
window.close()