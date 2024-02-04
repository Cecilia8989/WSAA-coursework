import requests
import json
import locationtagger
from geopy.geocoders import Nominatim

# Specify my current town location coordinates
latitude = 51.903614
longitude = -8.468399

# Initialize the Nominatim geocoder
geoLoc = Nominatim(user_agent="GetLoc")

# Reverse geocode the coordinates
location = geoLoc.reverse(str(latitude) + "," + str(longitude))

# Extract the address data
address = location.raw['address']

# Get the city
city = address.get('city', '')

# Print the city
print('City:', city)

# Construct the URL for fetching weather data based on the provided latitude and longitude
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m&current=temperature_2m,wind_speed_10m"

# Make a request to the Open Meteo API and parse the JSON response
response = requests.get(url)
data = response.json()

with open ("current_weather.json", 'w') as fp:
    json.dump(data, fp)

# Define keys for temperature and wind speed in the API response
temp_value = "temperature_2m"
wind_value = "wind_speed_10m"

# Extract relevant data from the API response
currentvalue = data["current"]
currentunits = data["current_units"]
temp_2m = currentvalue[temp_value]
wind_direction_10m = currentvalue[wind_value]

# Print temperature and wind speed along with their respective units
# Utilize title() to capitalize the first letter of variable names for better formatting 
# https://www.geeksforgeeks.org/how-to-capitalize-first-character-of-string-in-python/

# define title to print
title_to_print = "-- Temperature and wind speed on Ork "


print(f'{temp_value.title()} : {temp_2m} {currentunits[temp_value]}')
print(f'{wind_value.title()} : {wind_direction_10m} {currentunits[wind_value]}')