"""
"""

from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="Get NMI get location")


def get_lat_long(addr):
    location = geolocator.geocode(addr)
    try:
        return location.latitude, location.longitude
    except AttributeError as e:
        if 'NoneType' in str(e):
            return 0, 0
        raise (e)
