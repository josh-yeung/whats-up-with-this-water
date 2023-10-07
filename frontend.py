import PySimpleGUI as sg

sg.theme('DarkBlue17')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Weather:')],
            [sg.Text('Location:')],
            [sg.Button('Water Saftey Level'), sg.Button('Species Nearby')] ]

# Create the Window
window = sg.Window('Prokaryote', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
        break
    
window.close()