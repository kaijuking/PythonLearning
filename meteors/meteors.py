import requests
from geopy.distance import geodesic
from geopy.units import miles


def meteors():
    #print("meteors")

    # Irvine, CA (latitude, longitude)
    destination = (33.669445, -117.823059)
    data = get_data()
    process_data(data.json(), destination)



def get_data():
    #print("data")
    meteor_data = requests.get('https://data.nasa.gov/resource/gh4g-9sfh.json')
    return meteor_data


def process_data(data_to_parse, destination):
    
    # temp variable
    unsorted_data = []
    top_ten_locations = []

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