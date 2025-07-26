import csv

import Hashmap
import Package


# Function to load the package list
def load_packages(file_path):

    # Read csv as list of rows
    with open(file_path, 'r', encoding='utf-8-sig') as csv_file:  # encoding removes the BOM artifacts from the file
            csv_reader = csv.reader(csv_file, delimiter=',')

            # Pull package row data into the package list
            for row in csv_reader:

                new_package = Package.Package(*row) # Instantiate a new package object; *row unpacks all the values as arguments

                # HASH and ADD NEW PACKAGE
                hashmap = HashMap  # Instantiate package hashmap
                hashmap.HashMap.add(hashmap, new_package.id, new_package)


    return