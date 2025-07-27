# Parker LiaBraaten
# Student ID: 012461945


from datetime import datetime
import distance_data
import package_data
import userInterface

# CSV FILES
distance_file = 'Package Distance Table.csv'
package_file = 'Package Delivery Table.csv'

# LOAD ADDRESSES
address_dict, distance_list = distance_data.load_addresses(distance_file)

# LOAD PACKAGES INTO HASHMAP
package_hashmap = package_data.load_packages(package_file)

# START LOCATION
start_address = '4001 South 700 East'

# START TIME
today = datetime.today()
start_time = datetime(today.year, today.month, today.day, 8, 0, 0)

## TODO: keep?
# OVERALL MILEAGE TRACKER
total_mileage = 0

## TODO: keep?
# OVERALL PACKAGES DELIVERED
delivered_count = 0



# CLI
UI = userInterface.CLI()  # Instantiate the UI
userInterface.CLI.menu(UI, package_hashmap)  # Run the UI








## FIXME
# # TRUCK 3
# # Load truck 3
# truck3_packages = [6, 17, 22, 25, 26, 28, 31, 32]
# #Instantiate truck 3
# truck3 = truck.Truck(truck3_packages, start_address, returned_time)
# # Update delivery status for packages to en route
# truck.Truck.status_en_route(truck3, package_hashmap)
#
# # START TRUCK 3 AFTER ANOTHER TRUCK RETURNS
# truck3.deliver_packages(package_hashmap, address_dict, distance_list)












# Print total mileage
delivered_count = truck1.delivered_count + truck2.delivered_count + truck3.delivered_count
total_mileage = round(truck1.mileage + truck2.mileage + truck3.mileage, 2)




# print("Delivered packages: " + str(delivered_count))
#

#
# package_hashmap.print_all()
# package_hashmap.print_late()
#
# package_hashmap.print_package(34)