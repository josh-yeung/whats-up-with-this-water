# import geocoder
# import requests
# from bs4 import BeautifulSoup
# from geopy.geocoders import Nominatim

# def return_longlat():
#     g = geocoder.ip('me')
#     latitude, longitude = g.latlng
#     print(f"Latitude: {latitude}, Longitude: {longitude}")
#     return latitude, longitude

# def longlat_to_city(lat, lon):
#     geolocator = Nominatim(user_agent="geoapiExercises")
#     location = geolocator.reverse(str(lat)+","+str(lon))
#     print(location)

# def weather(city): 
#     # creating url and requests instance
#     url = "https://www.google.com/search?q="+"weather"+city
#     html = requests.get(url).content
    
#     # getting raw data
#     soup = BeautifulSoup(html, 'html.parser')
#     temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text

#     # printing all data
#     print("Temperature is", temp)
#     return temp

import geocoder
import math
import openpyxl 

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


def findClosestLake(): 
    latitude, longitude = return_longlat()
    # print("latitude: ", latitude)
    # print("longitude: ", longitude)
    referencePoint = {'latitude': latitude, 'longitude': longitude}
    locations = []
    wb = openpyxl.load_workbook('magnetic-reconnection\station.xlsx')
    ws = wb.active
    lofname = []
    loftype = []
    loflongitude = []
    loflatitude = []
    for i in range(2, ws.max_row+1):
        data = ws.cell(i,column=4).value
        lofname.append(data)
    for i in range(2, ws.max_row+1):
        data = ws.cell(i,column=5).value
        loftype.append(data)
    for i in range(2, ws.max_row+1):
        data = ws.cell(i,column=13).value
        loflongitude.append(data)
    for i in range(2, ws.max_row+1):
        data = ws.cell(i,column=12).value
        loflatitude.append(data)
    
    


findClosestLake()




    




