# Web Service and Application
# Author: Cecilia Pastore 


# Import necessary libraries
import requests
from geopy.geocoders import Nominatim

# Specify my current town location coordinates
# References: https://www.countrycoordinate.com/city-cork-ireland/
latitude = 51.896892
longitude = -8.486316

# Get the city and the country from the latitude and longitude
# Reference: https://www.geeksforgeeks.org/get-the-city-state-and-country-names-from-latitude-and-longitude-using-python/

# Initialize Nominatim API for reverse geocoding
geolocator = Nominatim(user_agent="geoapiExercises")
# Reverse geocode the coordinates to obtain the address details
location = geolocator.reverse(f"{latitude},{longitude}")
# Extract the address data
address = location.raw['address']
# Get the city and country from the address
city = address.get('city', '')
country = address.get('country', '')

# Construct the URL for fetching weather data based on the provided latitude and longitude
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_direction_10m"

# Make a request to the Open Meteo API and parse the JSON response
response = requests.get(url)
data = response.json()

# Define keys for temperature and wind speed in the API response
temp_value = "temperature_2m"
wind_value = "wind_direction_10m"

# Extract relevant data from the API response
currentvalue = data["current"]
currentunits = data["current_units"]
temp_2m = currentvalue[temp_value]
wind_direction_10m = currentvalue[wind_value]

# Print temperature and wind speed along with their respective units
# Reference: https://www.geeksforgeeks.org/how-to-capitalize-first-character-of-string-in-python/

# Print temperature and wind speed along with their respective units
print("\n-- Temperature and Wind Direction --")
print(f'   City: {city} ({country})')
print(f'   {temp_value.title()}: {temp_2m} {currentunits[temp_value]}')
print(f'   {wind_value.title()}: {wind_direction_10m} {currentunits[wind_value]}')