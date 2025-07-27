from datetime import datetime, timedelta
import package_list
import distance_data
import hashmap
import algorithms
import package_data


# CSV FILES
distance_file = 'Package Distance Table.csv'
package_file = 'Package Delivery Table.csv'

# LOAD ADDRESSES
address_dict, distance_list = distance_data.load_addresses(distance_file)

# LOAD PACKAGES INTO HASHMAP
package_hashmap = package_data.load_packages(package_file)

# print(address_dict)
# print(distance_list)
# package_hashmap.print_all()


##########
# Truck with list of packages
truck1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # package ids

# Current Location
current_address = 'HUB'  # FIXME

print("Start address: " + current_address)

# Start Time
today = datetime.today()
time = datetime(today.year, today.month, today.day, 8, 0, 0)

# Determine next package to deliver; return that package object and the distance to its delivery address
next_package = algorithms.NearestNeighbor.calculate_next(truck1, current_address, package_hashmap, address_dict, distance_list)

print("Next Package: ")
print(next_package)

# MOVE TRUCK
# Update time to the next package address
time += timedelta(0,next_package.loading_time,0)

# Update current location
current_address = next_package.address

# Timestamp package as delivered
next_package.delivery_time = time

print("Next address: " + current_address)
print(next_package.loading_time)
print(next_package.delivery_time)
print(time)
print(current_address)

# Remove package from the truck
truck1.remove(next_package.id)

print(truck1)



