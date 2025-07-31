import datetime
import config
import fleetOperations
import package_data


class CLI:

    def menu(self):

        while True:

            print("\n----------------------------------------------------")
            print("This is the command-line interface")
            print("----------------------------------------------------")
            print("Enter 1 see total mileage of trucks after delivery")
            print("Enter 2 to query all packages after delivery")
            print("Enter 3 to look up a package after delivery")
            print("Enter 4 to query all packages at a specific time")
            print("Enter 5 to look up package at a specific time")
            print("Enter 0 to exit program")
            print("--")
            action = input("Enter your option: ")


            # Enter 1 see total mileage of trucks after delivery
            if action == "1":

                stop_time = None
                package_data.load_packages(config.package_file)  # Reload the hashmap
                truck1, truck2, truck3 = fleetOperations.Fleet.run_package_delivery(stop_time)

                total_mileage = truck1.mileage + truck2.mileage #+ truck3.mileage

                print("\n----------------------------------------------------")
                print("RESULT:")
                print("Total Miles: " + str(round(total_mileage, 2)))
                print("Truck 1 mileage: " + str(round(truck1.mileage, 2)))
                print("Truck 2 mileage: " + str(round(truck2.mileage, 2)))
                print("Truck 3 mileage: " + str(round(truck3.mileage, 2)))

                # # TESTING FOR LATE PACKAGES
                # print("\n")
                # config.package_hashmap.print_late()


            # Enter 2 to query all packages after delivery
            elif action == "2":

                stop_time = None
                config.package_hashmap = package_data.load_packages(config.package_file)  # Reload the hashmap
                truck1, truck2, truck3 = fleetOperations.Fleet.run_package_delivery(stop_time)

                print("\n----------------------------------------------------")
                print("RESULT:")
                print("Total delivered packages: " + str(truck1.delivered_count + truck2.delivered_count + truck3.delivered_count))
                print("Truck 1 delivered " + str(truck1.delivered_count) + " packages")
                print("Truck 2 delivered " + str(truck2.delivered_count) + " packages")
                print("Truck 3 delivered " + str(truck3.delivered_count) + " packages")
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
                print("Truck 3: ")
                print("Total packages delivered: " + str(truck3.delivered_count))
                print("--")
                config.package_hashmap.print_truck(truck3.original_package_list)
                print("------------------------")


            # Enter 3 to look up a package after delivery
            elif action == "3":

                stop_time = None
                config.package_hashmap = package_data.load_packages(config.package_file)  # Reload the hashmap
                fleetOperations.Fleet.run_package_delivery(stop_time)

                id = int(input("Enter package id: "))

                print("\n----------------------------------------------------")
                print("RESULT:")
                print("Package id: " + str(id))
                if id in config.truck1_packages:
                    print("Truck 1")
                elif id in config.truck2_packages:
                    print("Truck 2")
                elif id in config.truck3_packages:
                    print("Truck 3")
                config.package_hashmap.print_package(id)


            # Enter 4 to query all packages at a specific time
            elif action == "4":

                # Obtain stop time from user
                while True:
                    input_time = input("Enter time in HHMM format: ")
                    try:
                        input_time = datetime.datetime.strptime(input_time, '%H%M').time()  # Format input into time
                    except ValueError:
                        print("Invalid input. Please enter time as HHMM (ex: 1330 for 1:30 PM)")
                        continue
                    stop_time = datetime.datetime.combine(datetime.datetime.today(), input_time)  # Add today's date
                    break

                # Run trucks until that time
                config.package_hashmap = package_data.load_packages(config.package_file)  # Reload the hashmap
                truck1, truck2, truck3 = fleetOperations.Fleet.run_package_delivery(stop_time)

                print("\n----------------------------------------------------")
                print("RESULT:")
                print("Time: " + str(stop_time))
                print("Total delivered packages: " + str(truck1.delivered_count + truck2.delivered_count + truck3.delivered_count))
                print("Truck 1 delivered " + str(truck1.delivered_count) + " packages")
                print("Truck 2 delivered " + str(truck2.delivered_count) + " packages")
                print("Truck 3 delivered " + str(truck3.delivered_count) + " packages")
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
                print("Truck 3: ")
                print("Total packages delivered: " + str(truck3.delivered_count))
                print("--")
                config.package_hashmap.print_truck(truck3.original_package_list)
                print("------------------------")

                # # TESTING FOR LATE PACKAGES
                # print("\n LATE PACKAGES")
                # config.package_hashmap.print_late()


            # Enter 5 to look up package at a specific time
            elif action == "5":

                id = int(input("Enter package id: "))

                # Obtain stop time from user
                while True:
                    input_time = input("Enter time in HHMM format: ")
                    try:
                        input_time = datetime.datetime.strptime(input_time, '%H%M').time()  # Format input into time
                    except ValueError:
                        print("Invalid input. Please enter time as HHMM (ex: 1330 for 1:30 PM)")
                        continue
                    stop_time = datetime.datetime.combine(datetime.datetime.today(), input_time)  # Add today's date
                    break

                # Run trucks until that time
                config.package_hashmap = package_data.load_packages(config.package_file)  # Reload the hashmap
                fleetOperations.Fleet.run_package_delivery(stop_time)

                print("\n----------------------------------------------------")
                print("RESULT:")
                print("Time: " + str(stop_time))
                print("Package id: " + str(id))
                if id in config.truck1_packages:
                    print("Truck 1")
                elif id in config.truck2_packages:
                    print("Truck 2")
                elif id in config.truck3_packages:
                    print("Truck 3")
                config.package_hashmap.print_package(id)


            #Enter 0 to exit program
            elif action == "0":
                print("Thanks!")
                break


            # If invalid input send back to menu
            else:
                print("Invalid input.")