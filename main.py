import package_list

import DistanceData
import PackageData


distance_file = 'Package Distance Table.csv'
package_file = 'Package Delivery Table.csv'


address_dict, distance_list = DistanceData.load_addresses(distance_file)

package_list = PackageData.load_packages(package_file)


print(address_dict)
print(distance_list)

print(address_dict['195 W Oakland Ave'])
print(distance_list[5][2])




address1 = '195 W Oakland Ave'  #5
address2 = '2300 Parkway Blvd'  #7

distance = DistanceData.get_distance(address1, address2, address_dict, distance_list)

print(distance)



for p in package_list:
    print(p)
