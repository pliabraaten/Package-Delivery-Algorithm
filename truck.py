from datetime import timedelta

import algorithms
import distance_data


class Truck:

    def __init__(self, truck_packages, start_address, start_time):
        self.original_package_list = truck_packages.copy()
        self.packages = truck_packages.copy()
        self.current_address = start_address
        self.time = start_time
        self.mileage = 0.0  # Miles by specific truck
        self.delivered_count = 0  # Count of packages delivered


    def status_en_route(self, package_hashmap):

        # Loop through all package ids in the truck
        for id in self.packages:
            package = package_hashmap.get(id)  # Retrieve package object
            package.delivery_status = "En route"  # Update delivery_status

        return True


    def deliver_packages(self, package_hashmap, address_dict, distance_list, stop_time):

        counter = 0  # Track number of packages delivered

        #  Stop truck deliveries at a specific time if one was entered OR when truck is empty
        while self.time < stop_time and len(self.packages) > 0:

            # DETERMINE NEXT PACKAGE
            next_package, distance, drive_time = self.pick_package(package_hashmap, address_dict, distance_list)

            # print("Next package: ")
            # print(next_package)

            # MOVE TRUCK
            self.move_truck(next_package, distance, drive_time)

            # DELIVER PACKAGE
            self.drop_package(next_package, distance)

            # print("Delivery: ")
            # print("Current time: " + str(self.time))
            # print("Current location: " + self.current_address)
            # print("Truck's milelage: " + str(self.mileage))
            # print("Packages still on truck: ")
            # print(self.packages)

            counter += 1

        # print("Counter: " + str(counter))

        return counter


    def pick_package(self, package_hashmap, address_dict, distance_list):

        # Determine next package to deliver; return that package object and the distance to its delivery address
        next_package, distance = algorithms.NearestNeighbor.calculate_next(self, self.current_address, package_hashmap,
                                                                           address_dict, distance_list)

        # Calculate the time to the next package
        drive_time = algorithms.NearestNeighbor.calculate_time(distance)

        return next_package, distance, drive_time


    def move_truck(self, next_package, distance, drive_time):

        # Update time after driving to the next package address
        self.time += timedelta(0, 0,0,0, drive_time, 0)

        # Update current location
        self.current_address = next_package.address

        # Update truck's mileage
        self.mileage += distance


    def drop_package(self, next_package, distance):

        # Timestamp package as delivered
        next_package.delivery_status = "Delivered"
        next_package.delivery_time = self.time

        # Remove package from the truck
        self.packages.remove(next_package.id)

        # Increment count of delivered packages
        self.delivered_count += 1


    def return_truck(self, address_dict, distance_list, start_address):

        # print("Miles before returning: " + str(self.mileage))

        # Calculate distance from last package location back to HUB
        distance = distance_data.get_distance(self.current_address, start_address, address_dict, distance_list)

        # Calculate time back to HUB
        return_time = algorithms.NearestNeighbor.calculate_time(distance)

        # Update time after driving to the next package address
        self.time += timedelta(0, 0,0,0, return_time, 0)

        # Update current location
        self.current_address = start_address

        # Update truck's mileage
        self.mileage += distance

        # print("------------------------------------------------------------------------")
        # print("Distance to return: " + str(distance))
        # print("Miles after returning: " + str(self.mileage))
        # print("Ending time: " + str(self.time))

        return self.time

