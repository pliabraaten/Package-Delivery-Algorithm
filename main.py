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
start_address = 'HUB'

# START TIME
today = datetime.today()
start_time = datetime(today.year, today.month, today.day, 8, 0, 0)

# OVERALL MILEAGE TRACKER
total_mileage = 0

# START TRUCKS
# Load truck with packages
truck1_packages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # package ids  ##FIXME
# Instantiate a truck packages
truck1 = truck.Truck(truck1_packages, start_address, start_time)

# START TRUCKS
# Deliver Packages for Truck1
truck1.deliver_packages(package_hashmap, address_dict, distance_list)



# Print total mileage
total_mileage = truck1.mileage
print("Total Miles: " + str(total_mileage))



