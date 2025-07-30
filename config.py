from datetime import datetime
import distance_data
import package_data


# CSV FILES
distance_file = 'Package Distance Table.csv'
package_file = 'Package Delivery Table.csv'

# LOAD ADDRESSES
address_dict, distance_list = distance_data.load_addresses(distance_file)

# START TIME
today = datetime.today()
start_time1 = datetime(today.year, today.month, today.day, 8, 0, 0)
start_time2 = datetime(today.year, today.month, today.day, 9, 10, 0)

# DELAYED PACKAGES
delayed_packages = [28, 6, 32, 25]
delayed_time = datetime(today.year, today.month, today.day, 9, 5, 0)

# LOAD PACKAGES INTO HASHMAP
package_hashmap = package_data.load_packages(package_file)

# START LOCATION
start_address = '4001 South 700 East'



