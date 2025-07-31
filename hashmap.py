

class Hashmap:

    def __init__(self):  # Contructor for Hashmap object
        # Hashmap to hold packages from csv for quick lookup
        self.package_hashmap = [None] * 10  # Create hashmap with space for 10 buckets (%10)

    def __str__(self):
        return f'Package({self.package_hashmap})'

    def __repr__(self):
        return f'Package({self.package_hashmap})'


    # Add new package to hashmap
    def put(self, key, value):  # key = new_package.id, value = new_package object

        hash_bin = self.calculate_hash(key)  # Run calculate_hash method to return the correct bin for this package
        key_value = [key, value]  # Save the id and object in a list: [id, <Package object>]

        if self.package_hashmap[hash_bin] is None:  # Check if anything is in the new package's bin
            self.package_hashmap[hash_bin] = [key_value]  # Assign list with id and object to the correct bin

        else:  # If bin already has packages
            for pair in self.package_hashmap[hash_bin]:  # Loop through each id/object list already in this bin
                if pair[0] == key:  # If an existing id equals the new_package.id
                    pair[1] = value  # Update the package object for that id
                    return True
            self.package_hashmap[hash_bin].append(key_value)  # If the id doesn't already exist, add it to the bin
            return True


    # Helper function to hash the id to calculate the bucket for each package based on its ID
    def calculate_hash(self, package_id):

        hash_bin = int(package_id) % 10  # Hash function
        return hash_bin  # Return the correct bin for this package


    # Function to retrieve the value from the key
    def get(self, key):

        hash_bin = self.calculate_hash(key)  # Run calculate_hash method to return the correct bin for this package

        if self.package_hashmap[hash_bin] is not None:  # If values exist in this bin
            for pair in self.package_hashmap[hash_bin]:  # Loop through each [id, object] pair in this bin
                if pair[0] == key:  # If the id matches the key being checked
                    return pair[1]  # Return the package object
        return None


    # Print one package object
    def print_package(self, key):

        package = self.get(key)
        print(package)


    # Print entire hashmap
    def print_all(self):
        for bin in self.package_hashmap:  # Loop through the bins
            if bin is not None:  # Skip if bin is empty
                for key, value in bin:  # For each key_value pair in the bin
                    print(value)  # Print the package object


    # Print original list of packages on truck and their status
    def print_truck(self, original_package_list):

        packages_list = []  # Create list for holding package objects
        for id in original_package_list:  # Loop through the truck's initial package load
            package = self.get(id)
            if package is not None:
                packages_list.append(package)  # Add packages to this list

        # Sort list by delivery_time
        packages_list.sort(key=lambda x: (x.delivery_time is None, x.delivery_time))  # Put None values (packages en route) at the end

        # Print each package one at a time:
        for package in packages_list:
            print(package)


    def print_late(self):
        for bin in self.package_hashmap:  # Loop through the bins
            if bin is not None:  # Skip if bin is empty
                for id, package in bin:  # For each key_value pair in the bin (id, <package>)
                    if package.deadline != 'EOD' and package.delivery_time is not None:  # Only print if package has a deadline
                        if package.deadline < package.delivery_time:
                            print(package)