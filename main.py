from datetime import datetime, timedelta
import package_list
import distance_data
import hashmap
import algorithms
import package_data
import truck

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

# OVERALL MILEAGE TRACKER
total_mileage = 0

# OVERALL PACKAGES DELIVERED
delivered_count = 0

# START TRUCKS
# Load truck with packages
truck1_packages = [1, 2, 4, 13, 14, 15, 16, 19, 20, 21, 27, 33, 34, 35, 39, 40]  # package ids
truck2_packages = [3, 5, 7, 8, 9, 10, 11, 12, 18, 23, 24, 29, 30, 36, 37, 38]

# Instantiate a truck packages
truck1 = truck.Truck(truck1_packages, start_address, start_time)
truck2 = truck.Truck(truck2_packages, start_address, start_time)

# START TRUCKS AND DELIVER PACKAGES
truck1.deliver_packages(package_hashmap, address_dict, distance_list)
truck2.deliver_packages(package_hashmap, address_dict, distance_list)

# TRUCK RETURNS
returned_time = truck1.return_truck(address_dict, distance_list, start_address)

# TRUCK 3
# Load truck 3
truck3_packages = [6, 17, 22, 25, 26, 28, 31, 32]

#Instantiate truck 3
truck3 = truck.Truck(truck3_packages, start_address, returned_time)

# START TRUCK 3 AFTER ANOTHER TRUCK RETURNS
truck3.deliver_packages(package_hashmap, address_dict, distance_list)


truck1.mileage = round(truck1.mileage, 2)
truck2.mileage = round(truck2.mileage, 2)
truck3.mileage = round(truck3.mileage, 2)

# Print total mileage
delivered_count = truck1.delivered_count + truck2.delivered_count + truck3.delivered_count
total_mileage = round(truck1.mileage + truck2.mileage + truck3.mileage, 2)

print("Delivered packages: " + str(delivered_count))
print("Total Miles: " + str(total_mileage))
print("Truck 1 mileage: " + str(truck1.mileage))
print("Truck 2 mileage: " + str(truck2.mileage))
print("Truck 3 mileage: " + str(truck3.mileage))

print(package_hashmap)



