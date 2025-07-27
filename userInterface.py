import datetime
import config
import fleetOperations


class CLI:

    def menu(self):

        print("This is the command-line interface")
        print("Enter 1 see total mileage of trucks")
        print("Enter 2 to query all packages after delivery")
        print("Enter 3 to lookup a package after delivery")
        print("Enter 4 to query delivery status at a specific time")
        action = input("Enter your option: ")


        # Enter 1 see total mileage of trucks
        if action == "1":

            stop_time = None
            truck1, truck2 = fleetOperations.Fleet.run_package_delivery(stop_time)

            total_mileage = truck1.mileage + truck2.mileage #+ truck3.mileage

            print("Total Miles: " + str(round(total_mileage, 2)))
            print("Truck 1 mileage: " + str(round(truck1.mileage, 2)))
            print("Truck 2 mileage: " + str(round(truck2.mileage, 2)))
            # print("Truck 3 mileage: " + str(round(truck3.mileage, 2)))


        # Enter 2 to query all packages after delivery
        if action == "2":

            stop_time = None
            fleetOperations.Fleet.run_package_delivery(stop_time)

            config.package_hashmap.print_all()


        # Enter 3 to see a lookup a package after delivery
        if action == "3":

            stop_time = None
            fleetOperations.Fleet.run_package_delivery(stop_time)

            id = int(input("Enter package id: "))
            config.package_hashmap.print_package(id)


        # Enter 4 to query delivery status at a specific time
        if action == "4":

            input_time = input("Enter time in HHMM format: ")
            input_time = datetime.datetime.strptime(input_time, '%H%M').time()  # Format input into time
            stop_time = datetime.datetime.combine(datetime.datetime.today(), input_time)  # Add today's date

            # print(stop_time)

            fleetOperations.Fleet.run_package_delivery(stop_time)

            return
