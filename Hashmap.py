class Hashmap:

    def __init__(self):
        # List to hold packages from csv
        self.package_hashmap = [None] * 10  # Create hashmap with space for 10 buckets (%10)


    # Hash the id to calculate the bucket
    def hash(self, key):

        hash = int(key) % 10
        return hash


    # Add new package to hashmap
    def add(self, key, value):

        key_hash = self.hash(key)
        key_value = [key, value]

### FIXME
        if self.package_hashmap[key_hash] is None:  # If no hash already exists in bin
            self.package_hashmap[key_hash] = [key_value]  # Create a new list and assign key-pair to bucket
                                                                # Can't Insert into None
        else:  # Check for collisions
            for pair in self.package_hashmap[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.package_hashmap[key_hash].append(key_value)
            return True


    def get(self, key):
        key_hash = self.hash(key)
        if self[key_hash] is not None:
            for pair in self[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None


    def print(self):
        for item in self.package_hashmap:
            if item is not None:
                print(str(item))