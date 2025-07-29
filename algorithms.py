import itertools
from itertools import combinations

import distance_data


class NearestNeighbor:

    @staticmethod  # Method belongs to class rather than an instance of the class
    def calculate_next(truck, current_address, package_hashmap, address_dict, distance_list):

        # Track the shortest distance
        shortest_dist = None
        # Track package with the shortest distance
        next_package = None

        for package in truck.packages:  # Loop through the list of packages on truck

            package_object = package_hashmap.get(package)  # Get package object from hashmap

            package_address = package_object.address  # Grab package address

            # Calculate distance between the current address and each package destination
            distance = distance_data.get_distance(current_address, package_address, address_dict, distance_list)

            if shortest_dist is None:  # For first package, set its distance to shortest for comparing
                shortest_dist = distance
                next_package = package_object
            else:
                if distance < shortest_dist:  # If shortest distance is found, track and set that as next package
                    shortest_dist = distance
                    next_package = package_object

        # After looping, return the package_object with the shortest distance
        return next_package, shortest_dist


    @staticmethod
    def calculate_time(distance):

        speed = 18  # Trucks have average speed of 18 miles per hour
        drive_time = distance / speed * 60  # Minutes

        return drive_time


    @staticmethod
    def calculate_combinations(iterable, r):

        combinations = itertools.combinations(iterable, r)

        return combinations

    #https://docs.python.org/3/library/itertools.html#itertools.combinations