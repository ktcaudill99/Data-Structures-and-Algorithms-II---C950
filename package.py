import datetime

class Package:
    def __init__(self, id, address, city, state, zip, deadline, weight, status, delivery_time, notes):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.status = status
        self.delivery_time = delivery_time
        self.notes = notes
        self.T1 = datetime.timedelta(hours=int(delivery_time.split(':')[0]), 
                                      minutes=int(delivery_time.split(':')[1]), 
                                      seconds=int(delivery_time.split(':')[2]))
        self.T2 = self.T1 + datetime.timedelta(hours=int(deadline.split(':')[0]), 
                                                minutes=int(deadline.split(':')[1]), 
                                                seconds=int(deadline.split(':')[2]))

    def __str__(self):
        return self.id + '|' + self.address + '|' + self.city + '|' + self.state + '|' + self.zip + '|' + self.deadline + '|' + self.weight + '|' + self.status + '|' + self.delivery_time + '|' + self.notes
