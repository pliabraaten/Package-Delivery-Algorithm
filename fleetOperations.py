import datetime
import config
import truck


class Fleet:

    @staticmethod
    def run_package_delivery(stop_time):

        # LOAD TRUCKS
        truck1, truck2 = Fleet.load_trucks(config.start_address, config.start_time1, config.start_time2)

        # RUN TRUCKS
        t1_time_returned = Fleet.run_trucks(truck1, truck2, config.package_hashmap, config.address_dict, config.distance_list, config.start_address, stop_time)

        # LOAD AND RUN 3RD TRUCK
        truck3 = Fleet.run_3rd_truck(t1_time_returned, stop_time)

        return truck1, truck2, truck3


    @staticmethod
    def load_trucks(start_address, start_time1, start_time2):

        # Load truck with packages
        truck1_packages = config.truck1_packages
        truck2_packages = config.truck2_packages

        # Instantiate a truck packages
        truck1 = truck.Truck(truck1_packages, start_address, start_time1, name="truck1")
        truck2 = truck.Truck(truck2_packages, start_address, start_time2, name="truck2")

        return truck1, truck2


    @staticmethod
    def run_trucks(truck1, truck2, package_hashmap, address_dict, distance_list, start_address, stop_time):

        # If user didn't enter a specific time to check, set stop time to the last sec of the day
        if stop_time is None:
            day_end = datetime.datetime.strptime('235959', '%H%M%S').time()
            stop_time = datetime.datetime.combine(datetime.datetime.today(), day_end)

        # DELIVER PACKAGES
        truck1.delivered_count = truck1.deliver_packages(package_hashmap, address_dict, distance_list, stop_time)
        truck2.delivered_count = truck2.deliver_packages(package_hashmap, address_dict, distance_list, stop_time)

        # TRUCK 1 RETURNS
        t1_time_returned = truck1.return_truck(address_dict, distance_list, start_address, stop_time)

        return t1_time_returned


    @staticmethod
    def run_3rd_truck(t1_time_returned, stop_time):

        # LOAD
        truck3_packages = config.truck3_packages

        # INSTANTIATE and SET TRUCK 3'S START TIME TO TRUCK 1'S ENDTIME
        truck3 = truck.Truck(truck3_packages, config.start_address, t1_time_returned, name="truck3")

        # If user didn't enter a specific time to check, set stop time to the last sec of the day
        if stop_time is None:
            day_end = datetime.datetime.strptime('235959', '%H%M%S').time()
            stop_time = datetime.datetime.combine(datetime.datetime.today(), day_end)

        # UPDATE PACKAGE WITH INCORRECT ADDRESS
        if stop_time > config.time_corrected:
            for id in config.packages_wrongAddress:
                package = config.package_hashmap.get(id)
                package.address = config.corrected_address
                package.city = config.corrected_city
                package.state = config.corrected_state
                package.zip = config.corrected_zip

        # If Truck 1 didn't return, END
        if t1_time_returned is None:
            return truck3

        # DELIVER PACKAGES
        if stop_time > t1_time_returned:  # Only if truck 1 has returned
            truck3.delivered_count = truck3.deliver_packages(config.package_hashmap, config.address_dict, config.distance_list, stop_time)

        return truck3