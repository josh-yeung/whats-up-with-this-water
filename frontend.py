import PySimpleGUI as sg
import time
import backend as back
        
def main():
    # sg.theme('LightBlue7')

    # # Loading Screen
    # loading = [[sg.Text('Fun Fact')], [sg.Button('Start')]]
    # loadingWindow = sg.Window('Loading', loading, size=(500,500), element_justification='c')
            
    # #Loading Screen
    # loadingEvent, loadingValues = loadingWindow.read()
    # if (loadingEvent==sg.WIN_CLOSED or loadingEvent=="Start"):
    #     loadingWindow.close()
    main_menu()

def subwindow_handler(subwindow):
    long, lat = back.return_longlat()
    water = [[sg.Text('Water Safety')], [sg.Text(f'Drainage: {back.drainageToLake(long, lat)}')]]
    animal = [[sg.Text('Animal Species')], [sg.Text("-Animal Fact")]]
    if(subwindow=="water"):
        SecondWindow = sg.Window('Water Health', water, size=(500,500), element_justification='c')
    else:
        SecondWindow = sg.Window('Endangered Species Nearby', animal, size=(500,500), element_justification='c')
    subevent, subvalues = SecondWindow.read()
    if(subevent==sg.WIN_CLOSED):
        SecondWindow.close()


def main_menu():
    #Home
    long, lat = back.return_longlat()
    city, province = back.findClosestCity(long, lat)
    
    back.redownload_lakes_excel()
    layout = [  [sg.Image('canadamap.png')],
                [sg.Button('Refresh')],
                [sg.Text(f'Weather: {back.weather(city, province)}')],
                [sg.Text(f'Location: {back.findClosestCity(long, lat)}')],
                [sg.Text(f'Closest Body of Water: {back.findClosestLake(long, lat)}')],
                [sg.Text(f'Type of Water: {back.typeOfWater(long, lat)}')],
                [sg.Button('Water Safety Level'), sg.Button('Species Nearby')] ]

    window = sg.Window('Prokaryote', layout, size=(500,500), element_justification='c')



    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            window.close()
            break
        if event == 'Water Safety Level':
            subwindow_handler("water")
        if event == 'Species Nearby':
            subwindow_handler("animal")
        if event == "Refresh":
            window.close()
            main_menu()
            break


main()
