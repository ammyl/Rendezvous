# city as a string to a longitude, latitude equivalence 

from geopy.geocoders import Nominatim

# user inputs the location; return the weather info

geolocator = Nominatim()
city = geolocator.geocode("Cleveland Ohio")
print(city.latitude)
