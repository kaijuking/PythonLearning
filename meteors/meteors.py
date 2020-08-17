import requests
from geopy.distance import geodesic
from geopy.units import miles

# Notes
# Geopy found from pypi.org - https://pypi.org/project/geopy/
# Exercise part of Cloud Guru video (Python for Beginners - Deprecated Aug 2020), lesson Chapter 2.12


def meteors():
    # Irvine, CA (latitude, longitude)
    destination = (33.669445, -117.823059)
    data = get_data()
    process_data(data.json(), destination)


def get_data():
    
    # Make a GET request to Nasa to get the data
    meteor_data = requests.get('https://data.nasa.gov/resource/gh4g-9sfh.json')
    if  meteor_data.status_code == 200:
        return meteor_data
    else:
        print("Expected Response = 200. Actual Response = {0}. Please try again.".format(meteor_data.status_code))


def process_data(data_to_parse, destination):
    
    # temp variable
    unsorted_data = []

    # process data    
    print("Processing The Data")
    for location in data_to_parse:
        if "geolocation" in location:

            # parse the current latitude and longitude values from the JSON
            current_location = (float(location["geolocation"]["latitude"]), float(location["geolocation"]["longitude"]))

            # use geopy to calculate the distance bewtween the two locations
            distance = geodesic(current_location, destination).miles

            # append the distance (in miles) to JSON
            unsorted_data.append((distance, location["name"]))
            #location["total_distance"] = distance

        else:
            print('Skipping because no geolocation data was provided')
        
    # sort data
    print("Sorting The Data")
    sorted_data = sorted(unsorted_data)

    # return the top ten closest meteors
    print("Top ten meteor names closest to Irvine, CA (MILES, METEOR NAME)")
    for i in range(10):
        print(sorted_data[i])


if __name__ == "__main__":
    meteors()