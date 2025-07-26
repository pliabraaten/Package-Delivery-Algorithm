# There is a direct connection between every location
import DistanceData
import Hashmap


class NearestNeighbor:

    # create delivery function that will take a list of packages on a truck and the start time
    # find the package in the list that has the address closest to the truck's current location
    # "move" the truck to that location
    # "deliver" the package




    @staticmethod
    def calculate_next(truck1, package_hashmap, address_dict, distance_list):
        # Track the shortest distance
        shortest_dist = None

        # loop through the list of packages
        for package in truck1:
            package_object = package_hashmap.get(package)
            if shortest_dist is None:
                shortest_dist = DistanceData.get_distance(package_object.address)

        return shortest_dist

    # get the distance for each package and current location
    # track shortest distance as it loops through all of them

    # get packakage id, query hashmap to get whole package object, get address string out
    # query distance dictionary for distance, calculate total distance


    # MOVE TRUCK
    # calculate time based on distance moved
    # add time to current datetime object
    # change the truck's current location variable

    # Deliver the package
    # timestamp the packagea
    # pop the package id off the list


