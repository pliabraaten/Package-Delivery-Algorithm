

class Package:
    # constructor
    def __init__(self, id, address, city, state, zip, deadline, weight, notes):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.notes = notes

        self.loading_time = None
        self.delivery_time = None

    def __str__(self):
        return f'Package({self.id},{self.address},{self.city},{self.state},{self.zip},{self.deadline},{self.weight},{self.notes},{self.loading_time},{self.delivery_time})'

    def __repr__(self):
        return f'Package({self.id},{self.address},{self.city},{self.state},{self.zip},{self.deadline},{self.weight},{self.notes},{self.loading_time},{self.delivery_time})'