from datetime import timedelta

import algorithms
import config
import distance_data
from config import start_time1, delayed_time


class Truck:

    def __init__(self, truck_packages, start_address, start_time, name):
        self.name = name
        self.original_package_list = truck_packages.copy()
        self.packages = truck_packages.copy()
        self.current_address = start_address
        self.time = start_time
        self.mileage = 0.0  # Miles by specific truck
        self.delivered_count = 0  # Count of packages delivered


    def check_delayed(self, package_hashmap):

        # Loop through all package ids in the truck
        for id in self.packages:
            package = package_hashmap.get(id)  # Retrieve package object
            if id in config.delayed_packages:  # If package is delayed, update status
                package.delivery_status = "Delayed"
        return


    def update_status(self, package_hashmap, stop_time):

        ## fixme: currently at 8 = en route, 905 = en route, 915 = at the hub
        ## should be 8 = delayed, 905 = at the hub, 915 = enroute
        # After delayed packages arrive at hug, update their status
        if stop_time <= delayed_time: # IF TIME IS BEFORE PACKAGE ARRIVES
            for id in config.delayed_packages:  # Loop through delayed packages
                package = package_hashmap.get(id)
                package.delivery_status = "Delayed"
        if config.delayed_time <= stop_time <= config.start_time2: # IF TIME IS AFTER PACKAGE ARRIVES BUT BEFORE TRUCK LEAVES
            for id in config.delayed_packages:  # Loop through delayed packages
                package = package_hashmap.get(id)
                package.delivery_status = "At the HUB"
        if config.start_time2 <= stop_time:  # IF TIME IS AFTER TRUCK LEAVES
            for id in self.packages:  # Loop through ALL package ids in the truck
                package = package_hashmap.get(id)
                package.delivery_status = "En route"

        return True


    def deliver_packages(self, package_hashmap, address_dict, distance_list, stop_time):

        counter = 0  # Track number of packages delivered

        # Update package status based on timing
        self.update_status(package_hashmap, stop_time)

        # if stop is before delayed time -> delayed


        # if stop time is after delayed time but before start time -> at hub
        # if stop is after start time -> enroute

        # # Update delivery status for packages to en route
        # if start_time1
        # truck.Truck.status_en_route(truck1, package_hashmap)
        # truck.Truck.status_en_route(truck2, package_hashmap)

        # # UPDATE STATUS FOR TRUCK 3 PACKAGES
        # if self.name == "truck3":
        #     self.status_en_route(package_hashmap)

        #  Deliver packages until truck is empty or until stop time is reached
        while True:

            # END if no more packages are in truck
            if len(self.packages) == 0:
                break

            # DETERMINE NEXT PACKAGE
            next_package, distance, drive_time = self.pick_package(package_hashmap, address_dict, distance_list)

            # END if move would take longer than stop_time
            if self.time + timedelta(minutes=drive_time) > stop_time:
                break

            # MOVE TRUCK
            self.move_truck(next_package, distance, drive_time)

            # DELIVER PACKAGE
            self.drop_package(next_package, distance)

            counter += 1

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
        self.time += timedelta(minutes=drive_time)

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

        return self.time

