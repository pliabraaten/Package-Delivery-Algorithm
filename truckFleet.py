import config
import truck



class Fleet:

    @staticmethod
    def run_package_delivery(self, stop_time):

        # LOAD TRUCKS
        truck1, truck2 = Fleet.load_trucks(config.start_address, config.start_time)

        # RUN TRUCKS
        Fleet.run_trucks(truck1, truck2, config.package_hashmap, config.address_dict, config.distance_list,
                         config.start_address, stop_time)

        return truck1, truck2


    @staticmethod
    def load_trucks(self, start_address, start_time):

        # Load truck with packages
        truck1_packages = [1, 2, 4, 13, 14, 15, 16, 19, 20, 21, 27, 33, 34, 35, 39, 40]  # package ids
        truck2_packages = [3, 5, 7, 8, 9, 10, 11, 12, 18, 23, 24, 29, 30, 36, 37, 38]
        # Instantiate a truck packages
        truck1 = truck.Truck(truck1_packages, start_address, start_time)
        truck2 = truck.Truck(truck2_packages, start_address, start_time)

        return truck1, truck2


    def run_trucks(self, truck1, truck2, package_hashmap, address_dict, distance_list, start_address, stop_time):

        while truck1.time < stop_time:
            # Update delivery status for packages to en route
            truck.Truck.status_en_route(truck1, package_hashmap)

            # DELIVER PACKAGES
            truck1.deliver_packages(package_hashmap, address_dict, distance_list)

        while truck2.time < stop_time:
            # Update delivery status for packages to en route
            truck.Truck.status_en_route(truck2, package_hashmap)

            # DELIVER PACKAGES
            truck2.deliver_packages(package_hashmap, address_dict, distance_list)


        # TRUCK RETURNS
        returned_time = truck1.return_truck(address_dict, distance_list, start_address)