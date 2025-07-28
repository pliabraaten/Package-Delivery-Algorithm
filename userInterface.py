import datetime
import config
import fleetOperations


class CLI:

    def menu(self):

        print("\n----------------------------------------------------")
        print("This is the command-line interface")
        print("----------------------------------------------------")
        print("Enter 1 see total mileage of trucks after delivery")
        print("Enter 2 to query all packages after delivery")
        print("Enter 3 to lookup a package after delivery")
        print("Enter 4 to query packages at a specific time")
        print("Enter 0 to exit program")
        print("--")
        action = input("Enter your option: ")


        # Enter 1 see total mileage of trucks after delivery
        if action == "1":

            stop_time = None
            truck1, truck2 = fleetOperations.Fleet.run_package_delivery(stop_time)

            total_mileage = truck1.mileage + truck2.mileage #+ truck3.mileage

            print("\n----------------------------------------------------")
            print("RESULT:")
            print("Total Miles: " + str(round(total_mileage, 2)))
            print("Truck 1 mileage: " + str(round(truck1.mileage, 2)))
            print("Truck 2 mileage: " + str(round(truck2.mileage, 2)))
            # print("Truck 3 mileage: " + str(round(truck3.mileage, 2)))

            # Return to menu options
            self.menu()


        # Enter 2 to query all packages after delivery
        if action == "2":

            stop_time = None
            fleetOperations.Fleet.run_package_delivery(stop_time)

            print("\n----------------------------------------------------")
            print("RESULT:")
            config.package_hashmap.print_all()

            # Return to menu options
            self.menu()


        # Enter 3 to lookup a package after delivery
        if action == "3":

            stop_time = None
            fleetOperations.Fleet.run_package_delivery(stop_time)

            id = int(input("Enter package id: "))

            print("\n----------------------------------------------------")
            print("RESULT:")
            config.package_hashmap.print_package(id)

            # Return to menu options
            self.menu()


        # Enter 4 to query packages at a specific time
        if action == "4":

            # Obtain stop time from user
            input_time = input("Enter time in HHMM format: ")
            input_time = datetime.datetime.strptime(input_time, '%H%M').time()  # Format input into time
            stop_time = datetime.datetime.combine(datetime.datetime.today(), input_time)  # Add today's date

            # Run trucks until that time
            truck1, truck2 = fleetOperations.Fleet.run_package_delivery(stop_time)


            print("\n----------------------------------------------------")
            print("RESULT:")
            print("Truck 1 delivered " + str(truck1.counter) + " packages")
            print("Truck 2 delivered " + str(truck2.counter) + " packages")
            print("\n-- Packages by Truck --")
            print("------------------------")
            print("Truck 1:")
            print("Total packages delivered: " + str(truck1.delivered_count))
            print("--")
            config.package_hashmap.print_truck(truck1.original_package_list)
            print("------------------------\n")
            print("Truck 2:")
            print("Total packages delivered: " + str(truck2.delivered_count))
            print("--")
            config.package_hashmap.print_truck(truck2.original_package_list)
            print("------------------------\n")
            # print("Truck 3: ")
            # config.package_hashmap.print_truck(truck3.original_package_list)
            # print("--\n")

            # Return to menu options
            self.menu()

            return




        #Enter 0 to exit program
        if action == "0":
            return