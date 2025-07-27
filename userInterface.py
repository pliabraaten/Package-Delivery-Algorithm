

class CLI:

    def menu(self, truck1, truck2, truck3, package_hashmap):


        print("This is the command-line interface")
        print("Enter 1 see total mileage of trucks")
        print("Enter 2 to see all packages after delivery")
        print("Enter 3 to deliver all trucks and see a single package")
        print("Enter 4 to see the status of all packages after a certain time")
        action = input("Enter your value: ")


        total_mileage = truck1.mileage + truck2.mileage + truck3.mileage


        # Enter 1 see total mileage of trucks
        if action == "1":
            print("Total Miles: " + str(round(total_mileage, 2)))
            print("Truck 1 mileage: " + str(round(truck1.mileage, 2)))
            print("Truck 2 mileage: " + str(round(truck2.mileage, 2)))
            print("Truck 3 mileage: " + str(round(truck3.mileage, 2)))


        # Enter 2 to see all packages after delivery
        if action == "2":
            package_hashmap.print_all()