import csv
import Package




# Function to load the package list
def load_packages(file_path):

    # List to hold packages from csv
    package_list = []

    index = 0

    # Read csv as list of rows
    with open(file_path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')

            # Hash each package into hash map
            for row in csv_reader:

                    package = row.pop(0)  # Pop package from the beginning of each row

                    #package_list.append(Package(package))  # Add distance values in list of list

    return package_list