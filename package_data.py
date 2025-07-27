import csv
from datetime import datetime

import hashmap
import package


# Function to load the package list
def load_packages(file_path):

    # Instantiate package hashmap
    package_hashmap = hashmap.Hashmap()  #Module.Class()

    # Read csv as list of rows
    with open(file_path, 'r', encoding='utf-8-sig') as csv_file:  # encoding removes the BOM artifacts from the file
            csv_reader = csv.reader(csv_file, delimiter=',')

            # Pull package row data into the package list
            for row in csv_reader:

                new_package = package.Package(*row) # Instantiate a new package object; *row unpacks all the values as arguments

                # If package has delivery deadline, convert it to datetime
                if new_package.deadline != 'EOD':
                    new_package.deadline = datetime.strptime(new_package.deadline, '%H:%M').today()

                # HASH and ADD NEW PACKAGE
                package_hashmap.put(new_package.id, new_package)

    return package_hashmap