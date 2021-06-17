# Dylan Thiemann
# Daily programming
# https://www.reddit.com/r/dailyprogrammer/comments/8i5zc3/20180509_challenge_360_intermediate_find_the/?utm_content=title&utm_medium=hot&utm_source=reddit&utm_name=dailyprogrammer

# Callsign index = 1
# Longitude index = 5
# latitude index = 6

import requests, json, math, sys

def main(longitude, latitude):
    openSkyApiUrl = "https://opensky-network.org/api/states/all"
    response = requests.get(openSkyApiUrl)
    flight_data = response.json()

    shortestDistance = sys.float_info.max
    closestFlight = ""

    startPoint = (latitude, longitude)
    for flight in flight_data["states"]:
        if (flight[5] == None or flight[6] == None):
            continue
        
        distance = euclideanDistance(startPoint, (flight[6], flight[5]))
        if (distance < shortestDistance):
            shortestDistance = distance
            closestFlight = flight

    print(closestFlight, shortestDistance)

# startPoint = (lat, long), endPoint = (lat, long)
def euclideanDistance(startPoint, endPoint):
    return math.sqrt((endPoint[0] - startPoint[0])**2 + (endPoint[1] - startPoint[1])**2)

main(-2.2945, 48.8584)