from os import stat
import PySimpleGUI as sg

read = open("template.txt", "r")
lines = []
for l in read.readlines():
    lines.append((l.strip().split(":")))
read.close()

#Add items to list that will be tracked
statsToTrack = ["Damage done", "Healing done", "Damage taken", "Blocked damage", "Shielded damage", 'Curse added', "Poison added"]

def createColumn(title, attribute, color='grey'):
    return [
    [sg.Text(title, text_color='black', background_color=color)], 
    [sg.Spin(values=[i for i in range(0, 1000)], initial_value=lines[0][attribute], size=(6,1), key=(title + '0'))], 
    [sg.Spin(values=[i for i in range(0, 1000)], initial_value=lines[1][attribute], size=(6,1), key=(title + '1'))], 
    [sg.Spin(values=[i for i in range(0, 1000)], initial_value=lines[2][attribute], size=(6,1), key=(title + '2'))], 
    [sg.Spin(values=[i for i in range(0, 1000)], initial_value=lines[3][attribute], size=(6,1), key=(title + '3'))]]

sg.theme('DarkAmber')
nameColumn = [
    [sg.Text("Name"), ], 
    [sg.Text(lines[0][0] + ": ", key='P0')], 
    [sg.Text(lines[1][0] + ": ", key='P1')], 
    [sg.Text(lines[2][0] + ": ", key='P2')], 
    [sg.Text(lines[3][0] + ": ", key='P3')]]

#Add column if stat track is added
layout = [[
    sg.Column(nameColumn), 
    sg.Column(createColumn("Damage done", 1, color="#cc2c1b"), background_color='#cc2c1b'), 
    sg.Column(createColumn("Healing done", 2, color="#2aab16"), background_color='#2aab16'), 
    sg.Column(createColumn("Damage taken", 3, color="#cc2c1b"), background_color='#cc2c1b'),
    sg.Column(createColumn("Blocked damage", 4, color="grey"), background_color='grey'),
    sg.Column(createColumn("Shielded damage", 5, color="#c9c9b7"), background_color='#c9c9b7'),
    sg.Column(createColumn("Curse added", 7, color="purple"), background_color='purple'),
    sg.Column(createColumn("Poison added", 7, color="#2aab16"), background_color='#2aab16')],
    [sg.Button('Reset')]]

# Create the window
window = sg.Window("Gloomtracker", layout, keep_on_top=True)

# Create an event loop
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        write = open("stats.txt", "w")
        backup = open("backup.txt", "a")
        for i in range(4):
            write.write(lines[i][0]+":")
            backup.write(lines[i][0]+":")
            for j in range(len(statsToTrack)):
                write.write(str(window.Element(statsToTrack[j]+str(i)).Get()) + ":")
                backup.write(str(window.Element(statsToTrack[j]+str(i)).Get()) + ":")
            write.write("\n")
            backup.write("\n")
        write.close()
        backup.close()
        break
    if event == 'Reset':
        for item in statsToTrack:
            for i in range(4):
                window[item+str(i)].update(0)

window.close()