import datetime
import config
import truck



class Fleet:

    @staticmethod
    def run_package_delivery(stop_time):

        # LOAD TRUCKS
        truck1, truck2 = Fleet.load_trucks(config.start_address, config.start_time)

        # RUN TRUCKS
        t1_time_returned = Fleet.run_trucks(truck1, truck2, config.package_hashmap, config.address_dict, config.distance_list, config.start_address, stop_time)

        # LOAD AND RUN 3RD TRUCK
        truck3 = Fleet.run_3rd_truck(t1_time_returned, stop_time)

        return truck1, truck2, truck3


    @staticmethod
    def load_trucks(start_address, start_time):

        # Load truck with packages
        truck1_packages = [1, 2, 4, 13, 14, 15, 16, 19, 20, 21, 27, 33, 34, 35, 39, 40]  # package ids
        truck2_packages = [3, 5, 7, 8, 9, 10, 11, 12, 18, 23, 24, 29, 30, 36, 37, 38]

        # Instantiate a truck packages
        truck1 = truck.Truck(truck1_packages, start_address, start_time)
        truck2 = truck.Truck(truck2_packages, start_address, start_time)

        return truck1, truck2


    @staticmethod
    def run_trucks(truck1, truck2, package_hashmap, address_dict, distance_list, start_address, stop_time):

        # Update delivery status for packages to en route
        truck.Truck.status_en_route(truck1, package_hashmap)
        truck.Truck.status_en_route(truck2, package_hashmap)

        # If user didn't enter a specific time to check, set stop time to the last sec of the day
        if stop_time is None:
            day_end = datetime.datetime.strptime('235959', '%H%M%S').time()
            stop_time = datetime.datetime.combine(datetime.datetime.today(), day_end)

        # DELIVER PACKAGES
        truck1.counter = truck1.deliver_packages(package_hashmap, address_dict, distance_list, stop_time)
        truck2.counter = truck2.deliver_packages(package_hashmap, address_dict, distance_list, stop_time)

        # TRUCK 1 RETURNS
        t1_time_returned = truck1.return_truck(address_dict, distance_list, start_address)

        return t1_time_returned


    @staticmethod
    def run_3rd_truck(t1_time_returned, stop_time):

        # LOAD
        truck3_packages = [6, 17, 22, 25, 26, 28, 31, 32]

        # INSTANTIATE and SET TRUCK 3'S START TIME TO TRUCK 1'S ENDTIME
        truck3 = truck.Truck(truck3_packages, config.start_address, t1_time_returned)

        # UPDATE PACKAGE STATUS
        truck.Truck.status_en_route(truck3, config.package_hashmap)

        # If user didn't enter a specific time to check, set stop time to the last sec of the day
        if stop_time is None:
            day_end = datetime.datetime.strptime('235959', '%H%M%S').time()
            stop_time = datetime.datetime.combine(datetime.datetime.today(), day_end)

        # DELIVER PACKAGES
        truck3.counter = truck3.deliver_packages(config.package_hashmap, config.address_dict, config.distance_list, stop_time)

        return truck3