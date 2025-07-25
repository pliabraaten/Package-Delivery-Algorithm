import csv
from operator import index

file_path = 'Package Distance Table.csv'

# Tracks address and their index from the package distance table
# Ex: 195 W Oakland: 5 -> indexed fifth in the distance_list[5]
address_dict = {}

# List of list that contains the distances
# Ex: distance_list[5][2] pulls the 3rd value for 195 W Oakland
distance_list = []

# Index counter for addresses
index = 0

# Read csv as list of rows
with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        # Create address index dictionary and list of list for distances
        for row in csv_reader:
                address = row.pop(0)  # Pop address from the beginning of each row
                row = [float(val) if val else 0.0 for val in row]  # Convert distance strings to floats
                address_dict[address] = index  # Key is the address, value is its index in the distance list
                distance_list.append(row)  # Add distance values in list of list
                index += 1  # Move to next index for this address

print(address_dict)
print(distance_list)

print(address_dict['195 W Oakland Ave'])
print(distance_list[5][2])