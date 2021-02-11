import PySimpleGUI as sg

sg.theme("Reds")
layout = [[sg.Text("Gold: "), sg.Spin(values=[i for i in range(0, 1000)], initial_value=0, size=(4,1))]]

window = sg.Window("Gold", layout, keep_on_top=True)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
window.close()