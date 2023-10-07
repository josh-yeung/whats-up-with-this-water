
import geocoder


def return_longlat():
    g = geocoder.ip('me')
    latitude, longitude = g.latlng
    print(f"Latitude: {latitude}, Longitude: {longitude}")
    return latitude, longitude

def get_longlog(name):
    print("test")

return_longlat()