# There is a direct connection between every location
import distance_data
import hashmap


class NearestNeighbor:

    @staticmethod  # Method belongs to class rather than an instance of the class
    def calculate_next(truck, package_hashmap, address_dict, distance_list):

        # Track the shortest distance
        shortest_dist = None
        # Track package with the shortest distance
        next_package = None

        for package in truck:  # Loop through the list of packages on truck

            package_object = package_hashmap.get(package)  # Get package object from hashmap

            current_address = '300 State St'  # FIXME
            address2 = package_object.address  # Grab package address

            # Calculate distance between the current address and each package destination
            distance = distance_data.get_distance(current_address, address2, address_dict, distance_list)

            if shortest_dist is None:  # For first package, set its distance to shortest for comparing
                shortest_dist = distance
                next_package = package_object
            else:
                if distance < shortest_dist:  # If shortest distance is found, track and set that as next package
                    shortest_dist = distance
                    next_package = package_object

        # After looping, return the package_object with the shortest distance
        return next_package




    # MOVE TRUCK
    # calculate time based on distance moved
    # add time to current datetime object
    # change the truck's current location variable

    # Deliver the package
    # timestamp the packagea
    # pop the package id off the list


