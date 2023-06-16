#Katherine Caudill
#Student #: 005252042
#WGU: Data Structures and Algorithms II - C950

# class Package is a class that represents a package. It has a constructor that takes in the following parameters:
#     package_id: the package's ID number (int) 
#     address: the package's address (str)
#     city: the package's city (str)
#     state: the package's state (str)
#     zip: the package's zip code (str)
#     deadline: the package's deadline (str)
#     weight: the package's weight (str)
#     status: the package's delivery status (str)
#     notes: the package's notes (str)

class Package:
    def __init__(self, package_id, address, city, state, zip, deadline, weight, status, notes):
        self.package_id = int(package_id)
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.delivery_status = status
        self.notes = notes

    def get_package_id(self):
        return self.package_id

    def get_address(self):
        return self.address

    def get_city(self):
        return self.city

    def get_state(self):
        return self.state

    def get_zip(self):
        return self.zip

    def get_deadline(self):
        return self.deadline

    def get_weight(self):
        return self.weight

    def get_delivery_status(self):
        return self.delivery_status

    def get_notes(self):
        return self.notes

    def set_delivery_status(self, status):
        self.delivery_status = status

    def set_address(self, address):
        self.address = address

    def set_city(self, set_city):
        set_city

    def set_zip(self, zip):
        self.zip = zip

    def set_deadline(self, deadline):
        self.deadline = deadline    
