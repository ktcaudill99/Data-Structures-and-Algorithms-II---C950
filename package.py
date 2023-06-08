class Package:
    def __init__(self, id, address, city, state, zipcode, deadline, weight, status=None, delivery_time=None, notes=None):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadline = deadline
        self.weight = weight
        self.status = status if status else "Not Delivered"
        self.delivery_time = delivery_time
        self.notes = notes

    def __str__(self):
        return "%s | %s | %s | %s | %s | %s | %s | %s | %s | %s" % (
            self.id, self.address, self.city, self.state, self.zipcode, self.deadline, self.weight, 
            self.status, self.delivery_time if self.delivery_time else 'N/A', self.notes if self.notes else 'N/A')
