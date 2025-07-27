from datetime import timedelta

import algorithms


class Truck:

    def __init__(self, truck1_packages, start_address, start_time):
        self.packages = truck1_packages
        self.current_address = start_address
        self.time = start_time
        self.mileage = 0.0  # Miles by specific truck


    def deliver_packages(self, package_hashmap, address_dict, distance_list):

        counter = 0  # Track number of packages delivered

        while len(self.packages) > 0:  # While there are still packages in the truck

            print("Before: ")
            print(self.time)
            print(self.current_address)
            print(self.mileage)
            print(self.packages)

            # DETERMINE NEXT PACKAGE
            next_package, distance = self.pick_package(package_hashmap, address_dict, distance_list)

            print("next package: ")
            print(next_package)

            # MOVE TRUCK
            self.move_truck(next_package, distance)

            # DELIVER PACKAGE
            self.deliver_package(next_package, distance)

            print("After: ")
            print(self.time)
            print(self.current_address)
            print(self.mileage)
            print(self.packages)

            counter += 1

        print("Counter: " + str(counter))


    def pick_package(self, package_hashmap, address_dict, distance_list):

        # Determine next package to deliver; return that package object and the distance to its delivery address
        next_package, distance = algorithms.NearestNeighbor.calculate_next(self, self.current_address, package_hashmap,
                                                                           address_dict, distance_list)

        # Update the next package object's loading time
        next_package.loading_time = algorithms.NearestNeighbor.calculate_time(distance)

        return next_package, distance


    def move_truck(self, next_package, distance):

        # Update time after driving to the next package address
        self.time += timedelta(0, next_package.loading_time, 0)

        # Update current location
        self.current_address = next_package.address

        # Update truck's mileage
        self.mileage += distance


    def deliver_package(self, next_package, distance):

        # Timestamp package as delivered
        next_package.delivery_time = self.time

        # Remove package from the truck
        self.packages.remove(next_package.id)


