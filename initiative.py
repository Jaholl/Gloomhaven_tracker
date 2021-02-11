import PySimpleGUI as sg

layout = [[sg.Input("")],[sg.Input("")],[sg.Input("")],[sg.Input("")],[sg.Input("")],[sg.Input("")],[sg.Input("")],[sg.Input("")],[sg.Input("")]]

window = sg.Window("HP", layout, keep_on_top=True)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
window.close()