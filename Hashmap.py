class Hashmap:

    def __init__(self):
        # List to hold packages from csv
        package_hashmap = [None] * 10  # Create hashmap with space for 10 buckets (%10)


    # Hash the id to calculate the bucket
    def hash(key):

        hash = int(key) % 10
        return hash


    # Add new package to hashmap
    def add(self, key, value):

        key_hash = self.hash(key)
        key_value = [key, value]

### FIXME
        if self[key_hash] is None:  # If no hash already exists in bin
            self.insert  # Insert new package object into the hashmap

        else:  # Check for collisions
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self[key_hash].append(key_value)
            return True


    def get(self, key):
        key_hash = self.hash(key)
        if self[key_hash] is not None:
            for pair in self[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None


    def print(self):
        for item in self:
            if item is not None:
                print(str(item))