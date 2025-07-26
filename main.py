import DistanceData





print(DistanceData.address_dict)
print(DistanceData.distance_list)

print(DistanceData.address_dict['195 W Oakland Ave'])
print(DistanceData.distance_list[5][2])



address1 = '195 W Oakland Ave'  #5
address2 = '2300 Parkway Blvd'  #7

distance = DistanceData.get_distance(address1, address2)

print(distance)