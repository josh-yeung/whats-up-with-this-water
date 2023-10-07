
import geocoder
import requests
from bs4 import BeautifulSoup
from geopy.geocoders import Nominatim

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


lon, lat = return_longlat()
longlat_to_city(lon, lat)