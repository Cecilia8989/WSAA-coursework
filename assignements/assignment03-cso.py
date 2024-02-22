# Web Service and Application
# assignement 3
# Author: Cecilia Pastore 

# Original url of the json dataset on cso:
# https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en

import requests
import json 

# Base URL components for the CSO API
url_beginning = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/"
url_end = "/JSON-stat/2.0/en"

# Function to fetch all data for a given dataset
def get_all_data(dataset):
    url = url_beginning + dataset + url_end
    response = requests.get(url)
    return response.json()
    
# Function to save fetched data as a JSON file
def get_all_as_json_file(dataset):
    # Opening a file in write mode to save the JSON data
    with open("output-files\cso.json", "wt") as fp:
        # Writing the fetched data to the file with indentation for readability
        json.dump(get_all_data(dataset), fp, indent=4)
        
if __name__ == "__main__":
    # Executing the function to fetch and save data for the "FIQ02" dataset
    get_all_as_json_file("FIQ02")