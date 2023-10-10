import PySimpleGUI as sg
import time
import backend as back
import word as word

def main():
    sg.theme('Dark Amber')

    # # Loading Screen
    # loading = [[sg.Text('Fun Fact')], [sg.Button('Start')]]
    # loadingWindow = sg.Window('Loading', loading, size=(500,500), element_justification='c')
            
    # #Loading Screen
    # loadingEvent, loadingValues = loadingWindow.read()
    # if (loadingEvent==sg.WIN_CLOSED or loadingEvent=="Start"):
    #     loadingWindow.close()
    main_menu()

def subwindow_handler(subwindow, window):
    long, lat = back.return_longlat()
    drainage, name = back.drainageToLake(long, lat)
    if(drainage=="Unknown Amount"):
        safety_message = f"Safety Levels are Unknown. Proceed at own risk."
    elif(float(drainage)<=7366.0):
        safety_message = f"Safety Levels lower than average. Relatively Safe."
    else:
        safety_message = f"Safety Levels higher than average. Do not Swim"
    water = [[sg.Text('Water Safety', font=("Helvetica", 11, "bold"))], [sg.Text(f'Drainage in {name}: {drainage}')], [sg.Text(f'{safety_message}\n')],
            [sg.Text('Natural Hydrology', font=("Helvetica", 11, "bold"))], 
            [sg.Text('In natural ecosystems, bodies of water often have natural drainage patterns, \n' 
                    'and these patterns play a crucial role in maintaining the health of \n'
                    'the ecosystem. High drainage can disrupt these natural patterns and \n' 
                    'may lead to negative consequences such as erosion, habitat loss, \n'
                    'and changes in water quality, which can be detrimental to the ecosystem.')],
            [sg.Text('\n')], [sg.Image('waterquality.png')], [sg.Button("Back")]]

    nearby_animal = back.find_closest_animals(long,lat)
    facts, image = back.return_animal_facts(nearby_animal)
    animal = [[sg.Image(image)], [sg.Text('\n')],
             [sg.Text(f'Animal Species: {nearby_animal}', font=("bold"))], [sg.Text('\n')], [sg.Text(facts)], [sg.Button("Ocean Wordle!")], [sg.Button("Back")]]
    if(subwindow=="water"):
        SecondWindow = sg.Window('Water Health', water, size=(500,500), element_justification='c')
    else:
        SecondWindow = sg.Window('Endangered Species Nearby', animal, size=(500,500), element_justification='c')
    subevent, subvalues = SecondWindow.read()
    if(subevent==sg.WIN_CLOSED):
        SecondWindow.close()
        window.close()
    if(subevent=="Ocean Wordle!"):
        word.main()
        SecondWindow.close()
    if(subevent=="Back"):
        SecondWindow.close()


def main_menu():
    #Home
    long, lat = back.return_longlat()
    city, province = back.findClosestCity(long, lat)

    back.redownload_lakes_excel()
    layout = [  [sg.Text('Water You Up To?', font=("Helvetica", 20, "bold"))],
                [sg.Image('canadamap.png')],
                [sg.Button('Refresh'),],
                [sg.Text(f'Weather: {back.weather(city, province)}', font=("Helvetica", 11))],
                [sg.Text(f'Location: {back.findClosestCity(long, lat)}', font=("Helvetica", 11))],
                [sg.Text(f'Closest Body of Water: {back.findClosestLake(long, lat)}', font=("Helvetica", 11))],
                [sg.Text(f'Type of Water: {back.typeOfWater(long, lat)}', font=("Helvetica", 11))],
                [sg.Button('Water Safety Level'), sg.Button('Species Nearby')] ]

    window = sg.Window('Prokaryote', layout, size=(500,500), element_justification='c')


    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            window.close()
            break
        if event == 'Water Safety Level':
            subwindow_handler("water", window)
        if event == 'Species Nearby':
            subwindow_handler("animal", window)
        if event == "Refresh":
            window.close()
            main_menu()
            break

main()
