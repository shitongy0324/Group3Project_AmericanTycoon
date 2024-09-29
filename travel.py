# Functions about travelling

import geopy.distance

def get_distance(coordinate1, coordinate2):
    return geopy.distance.distance(coordinate1, coordinate2).km

## Calculate the travelling time: 1 hour per 500 km






