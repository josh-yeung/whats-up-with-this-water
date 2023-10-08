
import geocoder
import requests
from bs4 import BeautifulSoup
from geopy.geocoders import Nominatim
from PIL import Image

im = Image.open("magnetic-reconnection\map2.png").convert('RGB')

def return_longlat():
    g = geocoder.ip('me')
    latitude, longitude = g.latlng
    print(f"Latitude: {latitude}, Longitude: {longitude}")
    return latitude, longitude

def longlat_to_city(lat, lon):
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.reverse(str(lat)+","+str(lon))
    print(location)

def weather(city): 
    # creating url and requests instance
    url = "https://www.google.com/search?q="+"weather"+city
    html = requests.get(url).content
    
    # getting raw data
    soup = BeautifulSoup(html, 'html.parser')
    temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text

    # printing all data
    print("Temperature is", temp)
    return temp

if im.getpixel((return_longlat()[0] + 100, return_longlat()[1] + 140)) == (74, 161, 112):
    print("Evergreen")
if im.getpixel((return_longlat()[0] + 100, return_longlat()[1] + 140)) == (240, 225, 117):
    print("Deciduous")
if im.getpixel((return_longlat()[0] + 100, return_longlat()[1] + 140)) == (228, 237, 251):
    print("Shrubland")
if im.getpixel((return_longlat()[0] + 100, return_longlat()[1] + 140)) == (192, 203, 149):
    print("grassland")
if im.getpixel((return_longlat()[0] + 100, return_longlat()[1] + 140)) == (205, 213, 230):
    print("Cropland")
if im.getpixel((return_longlat()[0] + 100, return_longlat()[1] + 140)) == (252, 252, 252):
    print("Built-up")