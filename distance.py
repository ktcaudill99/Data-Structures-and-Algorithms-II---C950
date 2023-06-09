import csv
import datetime
from turtle import distance
#from turtle import distance


class DistanceCalc:
    # Initialize the class
    def __init__(self):
        # load distance name data
        with open('c950/distance_name_data.csv') as distance_name_file:
            self.name_reader = list(csv.reader(distance_name_file, delimiter=','))

        # load distance data
        with open('c950/distance_data.csv') as distance_file:
            self.distance_reader = list(csv.reader(distance_file, delimiter=','))

    # check distance from current location to another location
    def check_distance(self, current_location, from_location):
        row = int(current_location)
        col = int(from_location)
        distance = self.distance_reader[row][col]
        if distance is None or distance == '':
            distance = self.distance_reader[col][row]
        return distance

    # get number from location address
    def check_location_num_from_address(self, location):
        for name in self.name_reader:
            if location == name[2]:
                return name[0]

    # get simulated truck time
    def check_time(self, truck, name):
        truck_timeline = []
        if name == 'truck1':
            truck_time = ['8:00:00']
        elif name == 'truck2':
            truck_time = ['9:05:00']
        elif name == 'truck3':
            truck_time = ['10:00:00']
        for t in truck:
            if truck[0] == t:
                pl = 0
            address = t.get_address()
            cl = self.check_location_num_from_address(address)
            d = self.check_distance(cl, pl)
            pl = cl
            time = float(d) / 18
            time_format = '{0:02.0f}:{1:02.0f}:00'.format(*divmod(time * 60, 60))
            truck_time.append(time_format)
        total_time = datetime.timedelta()
        for t in truck_time:
            total_time += self.get_delta_time(t)
            truck_timeline.append(total_time)
        return truck_timeline

    # convert string to time delta
    def get_delta_time(self, s):
        try:
            (h, m, s) = s.split(':')
            dt = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            return dt
        except:
            print("Error converting to Time Delta")

    # get specific time
    def check_delivery_time(self, truck, truck_time, id):
        for i in truck:
            if i.get_package_id() == id:
                index = truck.index(i)
        return truck_time[index+1]

    # Check delivery status and any given time
    def check_delivery_status(self, t, truck, t_time, name, id):
        delivery_time = self.check_delivery_time(truck, t_time, id)
        timestamp = self.get_delta_time(t)
        truck_time = {'TRUCK 1': self.get_delta_time('8:00:00'),
                      'TRUCK 2': self.get_delta_time('9:05:00'),
                      'TRUCK 3': self.get_delta_time('10:00:00')}.get(name, None)
        if timestamp > delivery_time:
            return 'DELIVERED'
        elif timestamp <= delivery_time and timestamp >= truck_time:
            return 'ON_TRUCK'
        else:
            return 'AT_HUB'

       # calc the total distance traveled by the trucks
    def get_total_distance_traveled(self, truck):
        total_miles = 0
        for t in truck:
            if truck[0] == t:
                previous_location = 0
            current_location = self.check_location_num_from_address(t.get_address())
            distance = self.check_distance(current_location, previous_location)
            total_miles += float(distance)
            previous_location = current_location
        return total_miles

    # # calc the total distance traveled by the trucks
    # def get_total_distance_traveled(self, truck):
    #     total_miles = 0
    #     for t in truck:
    #         if truck[0] == t:
    #             pl = 0
    #         cl = self.check_location_num_from_address(t.get_address())
    #         d = self.check_distance(cl, pl)
    #         pl = cl
    #         total_miles += float(d)
    #     # calc trip back to main hub
    #     d = self.check_distance(cl, 0)
    #     total_miles += float(d)
    #     return round(total_miles, 2)

    # display data based off time input
    def display_data_from_time(self, name, truck, truck_timeline, time, distance):
        print('\n{} || # of packages: {} || Total Distance: {} miles\n'.format(name, len(truck), distance))
        if time == '':
            timestamp = '23:00:00'
        else:
            timestamp = time
        for t in truck:
            i = truck.index(t)
            id = t.get_package_id()
            ds = self.check_delivery_status(timestamp, truck, truck_timeline, name, id)
            s = 'ID: {:>2} -- Deadline: {:>6} -- Status: {:>6} -- Expected Delivery: {}'
            formatted_string = s.format(id, t.get_deadline(), ds, truck_timeline[i + 1])
            print(formatted_string)
            
def create_distance_calc():
    return DistanceCalc()  # Create an instance of DistanceCalc class

            

