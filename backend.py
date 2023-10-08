import geocoder
import requests
from bs4 import BeautifulSoup
from geopy.geocoders import Nominatim
from PIL import Image
import wget
import zipfile
import os
im = Image.open("map2.png").convert('RGB')
import math
import openpyxl
from pyexcel.cookbook import merge_all_to_a_book
import glob

def return_longlat():
    g = geocoder.ip('me')
    latitude, longitude = g.latlng
    return latitude, longitude

def longlat_to_city(lat, lon):
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.reverse(str(lat)+","+str(lon))
    print(location)

def weather(city, province): 
    # creating url and requests instance
    url = "https://www.google.com/search?q="+"weather"+city+province
    html = requests.get(url).content
    
    # getting raw data
    soup = BeautifulSoup(html, 'html.parser')
    temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text

    # printing all data
    return temp


def haversine_distance(lat1, lon1, lat2, lon2):
    R = 6371  # Earth's radius in kilometers
    
    # Convert coordinates to radians
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)
    
    # Calculate differences in coordinates
    delta_lat = lat2_rad - lat1_rad
    delta_lon = lon2_rad - lon1_rad
    
    # Apply Haversine formula
    a = math.sin(delta_lat/2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(delta_lon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance = R * c
    
    return distance

def find_nearest_location(reference_point, locations):
    min_distance = float('inf')
    nearest_location = None
    
    for location in locations:
        if (location['latitude'] != None and location['longitude'] != None):
            distance = haversine_distance(reference_point['latitude'], reference_point['longitude'], location['latitude'], location['longitude'])
        
        if distance < min_distance:
            min_distance = distance
            nearest_location = location
    
    return nearest_location

# # Example usage
# reference_point = {'latitude': 37.7749, 'longitude': -122.4194}
# locations = [
#     {'latitude': 37.7749, 'longitude': -122.4194},
#     {'latitude': 34.0522, 'longitude': -118.2437},
#     {'latitude': 40.7128, 'longitude': -74.0060},
# ]

# nearest_location = find_nearest_location(reference_point, locations)
# print(nearest_location)


def return_longlat():
    g = geocoder.ip('me')
    latitude, longitude = g.latlng
    # print(f"Latitude: {latitude}, Longitude: {longitude}")
    return latitude, longitude


def findClosestLake(latitude, longitude): 
    referencePoint = {'latitude': latitude, 'longitude': longitude}
    locations = []
    lakeCoords = []
    wb = openpyxl.load_workbook('station.xlsx')
    ws = wb.active
    lofname = []
    loflongitude = []
    loflatitude = []
    for i in range(2, ws.max_row+1):
        data = ws.cell(i,column=4).value
        lofname.append(data)
    for i in range(2, ws.max_row+1):
        data = ws.cell(i,column=13).value
        loflongitude.append(data)
    for i in range(2, ws.max_row+1):
        data = ws.cell(i,column=12).value
        loflatitude.append(data)
    
    for i in range(0, len(loflongitude)):
        x = {'latitude': loflatitude[i], 'longitude': loflongitude[i]}
        locations.append(x)
    
    for i in range(0, len(lofname)):
        key = str(loflatitude[i]) + ',' + str(loflongitude[i])
        x = {key: lofname[i]}
        lakeCoords.append(x)
        
    nearest_location = find_nearest_location(referencePoint, locations)
    # print(nearest_location)
    x = nearest_location['latitude']
    y = nearest_location['longitude']
    key = str(x) + ',' + str(y)
    for i in range(0, len(lakeCoords)):
        if key in lakeCoords[i]:
            name = (lakeCoords[i])[key]
            break
    return name


def findClosestCity(latitude, longitude): 
    referencePoint = {'latitude': latitude, 'longitude': longitude}
    locations = []
    cityCoords = []
    wb = openpyxl.load_workbook('canadacities.xlsx')
    ws = wb.active
    lofname = []
    loftype = []
    loflongitude = []
    loflatitude = []
    for i in range(2, ws.max_row+1):
        data = ws.cell(i,column=2).value
        lofname.append(data)
    for i in range(2, ws.max_row+1):
        data = ws.cell(i,column=3).value
        loftype.append(data)
    for i in range(2, ws.max_row+1):
        data = ws.cell(i,column=6).value
        loflongitude.append(data)
    for i in range(2, ws.max_row+1):
        data = ws.cell(i,column=5).value
        loflatitude.append(data)
    
    for i in range(0, len(loflongitude)):
        x = {'latitude': loflatitude[i], 'longitude': loflongitude[i]}
        locations.append(x)
    
    for i in range(0, len(lofname)):
        key = str(loflatitude[i]) + ',' + str(loflongitude[i])
        x = {key: lofname[i]}
        cityCoords.append(x)
        
    nearest_location = find_nearest_location(referencePoint, locations)
    # print(nearest_location)
    x = nearest_location['latitude']
    y = nearest_location['longitude']
    key = str(x) + ',' + str(y)
    for i in range(0, len(cityCoords)):
        if key in cityCoords[i]:
            name = (cityCoords[i])[key]
            prov = (cityCoords[i])[key]
            break
    for j in range(2, ws.max_row+1):
        data = ws.cell(j,column=2).value
        if(data==name):
            prov = ws.cell(j,column=3).value
    return name, prov



def drainageToLake(latitude, longitude): 
    name = findClosestLake(latitude, longitude)
    wb = openpyxl.load_workbook('station.xlsx')
    ws = wb.active
    lofname = []
    lofdrainage= []
    list = []
    for i in range(2, ws.max_row+1):
        data = ws.cell(i,column=4).value
        lofname.append(data)
    for i in range(2, ws.max_row+1):
        data = ws.cell(i,column=8).value
        lofdrainage.append(data)
    for i in range(0, len(lofdrainage)):
        x = {str(lofname[i]): lofdrainage[i]}
        list.append(x)
    for i in range(0, len(list)):
        if name in list[i]:
            if (list[i])[name] != None:
                drainage = str((list[i])[name]) + " sq mi"
                break
            else:
                drainage = "Unknown Amount"
    return drainage, name


def typeOfWater(latitude, longitude): 
    name = findClosestLake(latitude, longitude)
    wb = openpyxl.load_workbook('station.xlsx')
    ws = wb.active
    lofname = []
    loftype= []
    list = []
    for i in range(2, ws.max_row+1):
        data = ws.cell(i,column=4).value
        lofname.append(data)
    for i in range(2, ws.max_row+1):
        data = ws.cell(i,column=5).value
        loftype.append(data)
    for i in range(0, len(loftype)):
        x = {str(lofname[i]): loftype[i]}
        list.append(x)
    for i in range(0, len(list)):
        if name in list[i]:
            if (list[i])[name] != None:
                type = str((list[i])[name])
                break
            else:
                type = "Unknown Water Source"
    return type

def redownload_lakes_excel():
    wget.download("https://www.waterqualitydata.us/data/Station/search?countrycode=CA&mimeType=csv&zip=yes&providers=NWIS&providers=STEWARDS&providers=STORET")
    with zipfile.ZipFile("station.zip", "r") as zip_ref:
        zip_ref.extractall()
    os.remove("station.zip")
    merge_all_to_a_book(glob.glob("station.csv"), "station.xlsx")
    os.remove("station.csv")

def return_ecosystem(return_longlat):
    if im.getpixel((return_longlat()[0] + 100, return_longlat()[1] + 140)) == (74, 161, 112):
        eco_system = "Evergreen ecosystem"
    if im.getpixel((return_longlat()[0] + 100, return_longlat()[1] + 140)) == (240, 225, 117):
        eco_system = "Deciduous ecosystem"
    if im.getpixel((return_longlat()[0] + 100, return_longlat()[1] + 140)) == (228, 237, 251):
        eco_system = "Shrubland"
    if im.getpixel((return_longlat()[0] + 100, return_longlat()[1] + 140)) == (192, 203, 149):
        eco_system = "grassland"
    if im.getpixel((return_longlat()[0] + 100, return_longlat()[1] + 140)) == (205, 213, 230):
        eco_system = "Cropland"
    if im.getpixel((return_longlat()[0] + 100, return_longlat()[1] + 140)) == (252, 252, 252):
        eco_system = "Cropland"
    if im.getpixel((return_longlat()[0] + 100, return_longlat()[1] + 140)) == (74, 161, 112):
        eco_system = "Built-in"
    print(eco_system)
    return eco_system


def find_closest_animals(latitude, longitude):
    referencePoint = {'latitude': latitude, 'longitude': longitude}
    locations = []
    cityCoords = []

    wb = openpyxl.load_workbook('animals.xlsx')
    ws = wb.active
    lofname = []
    loflongitude = []
    loflatitude = []
    for i in range(2, ws.max_row+1):
        data = ws.cell(i,column=1).value
        lofname.append(data)
    for i in range(2, ws.max_row+1):
        data = ws.cell(i,column=2).value
        loflongitude.append(data)
    for i in range(2, ws.max_row+1):
        data = ws.cell(i,column=3).value
        loflatitude.append(data)
    
    for i in range(0, len(loflongitude)):
        x = {'latitude': loflatitude[i], 'longitude': loflongitude[i]}
        locations.append(x)
    
    for i in range(0, len(lofname)):
        key = str(loflatitude[i]) + ',' + str(loflongitude[i])
        x = {key: lofname[i]}
        cityCoords.append(x)
        
    nearest_location = find_nearest_location(referencePoint, locations)
    # print(nearest_location)
    x = nearest_location['latitude']
    y = nearest_location['longitude']
    key = str(x) + ',' + str(y)
    for i in range(0, len(cityCoords)):
        if key in cityCoords[i]:
            name = (cityCoords[i])[key]
            break
    return name

def return_animal_facts(name):
    if(name == "Sea otters"):
        return ("")
    if(name == "Blue whale"):
        return ("")
    if(name == "Basking shark"):
        return ("")
    if(name == "Humpback whale"):
        return ("")
    if(name == "Leatherback turtle"):
        return ("")
    if(name == "Shortnose sturgeon"):
        return ("")
    if(name == "Atlantic salmon"):
        return ("")
    if(name == "Lake sturgeon"):
        return ("")
    if(name == "White sturgeon"):
        return ("")
    if(name == "Eastern Sand darter"):
        print("")
    if(name == "Vancouver lamprey"):
        return ("")
    if(name == "Nooksack Dace"):
        x = ("Location: Nooksack dace inhabit streams and rivers in British Columbia \nand some parts of the western United States.")
        x += ("\n\nDiet: They primarily feed on aquatic invertebrates.")
        x += ("\n\nWhy They're Endangered: Habitat loss and degradation caused by urban \ndevelopment, agriculture, and water diversion have led to the decline of Nooksack \ndace populations. These factors have limited their suitable habitat.\n\n\n")
        return x