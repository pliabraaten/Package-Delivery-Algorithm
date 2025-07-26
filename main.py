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

#
# Truck with list of packages
truck1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # package ids
# NearestNeighbor.NearestNeighbor.calculate_next(truck1, package_hashmap, address_dict, distance_list)

# print(address_dict)
# print(distance_list)
#
# print(address_dict['195 W Oakland Ave'])
# print(distance_list[5][2])


# address1 = '195 W Oakland Ave'  #5
# address2 = '2300 Parkway Blvd'  #7
#
# distance = DistanceData.get_distance(address1, address2, address_dict, distance_list)

# print(distance)

package_hashmap.print_all()