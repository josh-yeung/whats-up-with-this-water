import PySimpleGUI as sg

sg.theme('LightBlue7')

# Loading Screen

loading = [[sg.Text('Fun Fact')], [sg.Button('Start')]]
loadingWindow = sg.Window('Loading', loading)
        

# Home Screen

layout = [  [sg.Button('Refresh')],
            [sg.Text('Weather:')],
            [sg.Text('Location:')],
            [sg.Button('Water Saftey Level'), sg.Button('Species Nearby')] ]


window = sg.Window('Prokaryote', layout)


while True:
    loadingEvent, loadingValues = loadingWindow.read()
    event, values = window.read()
    if loadingEvent == sg.WIN_CLOSED:
        loadingWindow.close()
        break
    if loadingEvent == 'Start':
        loadingWindow.close()
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            window.close()
        if event == 'Water Saftey Level':
            print('hi')
        if event == 'Species Nearby':
            print('hello')


    
