class Package:
    def __init__(self, id, address, city, state, zipcode, deadline, weight):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadline = deadline
        self.weight = weight

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s" % (self.id, self.address, self.city, self.state, self.zipcode, self.deadline, self.weight)

