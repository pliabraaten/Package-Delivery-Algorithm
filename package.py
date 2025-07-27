from datetime import datetime


class Package:
    # constructor
    def __init__(self, id, address, city, state, zip, deadline, weight, notes):
        self.id = int(id)
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.delivery_status = "At the HUB"
        self.delivery_time = None


    def __str__(self):
        return f'Package({self.id},{self.address},{self.city},{self.state},{self.zip},{self.deadline},{self.weight},{self.notes},{self.delivery_status},{self.delivery_time})'

    def __repr__(self):
        return f'Package({self.id},{self.address},{self.city},{self.state},{self.zip},{self.deadline},{self.weight},{self.notes},{self.delivery_status},{self.delivery_time})'