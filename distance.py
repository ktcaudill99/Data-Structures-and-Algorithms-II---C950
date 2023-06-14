import csv
import datetime


class Distance:
    # get distance name data
    with open('distance_name_data.csv') as distance_name_file:
        name_reader = list(csv.reader(distance_name_file, delimiter=','))

    # get distance data
    with open('distance_data.csv') as distance_file:
        distance_reader = list(csv.reader(distance_file, delimiter=','))

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
        if name == 'truck2':
            truck_time = ['9:05:00']
        if name == 'truck3':
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
        if name == 'TRUCK 1':
            truck_time = self.get_delta_time('8:00:00')
        if name == 'TRUCK 2':
            truck_time = self.get_delta_time('9:05:00')
        if name == 'TRUCK 3':
            truck_time = self.get_delta_time('10:00:00')
        if timestamp > delivery_time:
            return 'DELIVERED'
        if timestamp <= delivery_time:
            if timestamp < truck_time:
                return 'AT_HUB'
            else:
                return 'ON_TRUCK'

    # calc the total distance traveled by the trucks
    def get_total_distance_traveled(self, truck):
        total_miles = 0
        for t in truck:
            if truck[0] == t:
                pl = 0
            cl = self.check_location_num_from_address(t.get_address())
            d = self.check_distance(cl, pl)
            pl = cl
            total_miles += float(d)
        # calc trip back to main hub
        d = self.check_distance(cl, 0)
        total_miles += float(d)
        return round(total_miles, 2)

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











# from package import total_distance_1, total_distance_2, total_distance_3
# import csv
# import datetime
# from importlib.resources import Package

# # Read CSV files
# with open('./distance_data.csv') as csvfile_1:
#     distance_csv = list(csv.reader(csvfile_1, delimiter=','))
# with open('./distance_name_data.csv') as csvfile_2:
#     distance_name_csv = list(csv.reader(csvfile_2, delimiter=','))


#     # Get package address data -> O(n)
#     def get_address():
#         return distance_name_csv

#     # Calculate the total distance from row/column values -> O(1)
#     def get_distance(row, col, total):
#         distance = distance_csv[row][col]
#         if distance == '':
#             distance = distance_csv[col][row]

#         return total + float(distance)

#     # Calculate the current distance from row/column values -> O(1)
#     def get_current_distance(row, col):
#         distance = distance_csv[row][col]
#         if distance == '':
#             distance = distance_csv[col][row]

#         return float(distance)

#     # Calculate total distance for a given truck -> O(n)
#     def get_time(distance, truck_list):
#         new_time = distance / 18
#         distance_in_minutes = '{0:02.0f}:{1:02.0f}'.format(
#             *divmod(new_time * 60, 60))
#         final_time = distance_in_minutes + ':00'
#         truck_list.append(final_time)
#         total = datetime.timedelta()
#         for i in truck_list:
#             (hrs, mins, secs) = i.split(':')
#             total += datetime.timedelta(hours=int(hrs),
#                                         minutes=int(mins), seconds=int(secs))
#         return total

#     # these lists represent the sorted trucks that are put in order of efficiency in the function below
#     first_truck = []
#     first_truck_indices = []
#     second_truck = []
#     second_truck_indices = []
#     third_truck = []
#     third_truck_indices = []

#     def get_shortest_route(_list, num, curr_location):
#         if not len(_list):
#             return _list

#         lowest_value = 50.0
#         location = 0

#         for i in _list:
#             value = int(i[1])
#             if get_current_distance(curr_location, value) <= lowest_value:
#                 lowest_value = get_current_distance(
#                     curr_location, value)
#                 location = value

#         for i in _list:
#             if get_current_distance(curr_location, int(i[1])) == lowest_value:
#                 if num == 1:
#                     first_truck.append(i)
#                     first_truck_indices.append(i[1])
#                     _list.pop(_list.index(i))
#                     curr_location = location
#                     get_shortest_route(_list, 1, curr_location)
#                 elif num == 2:
#                     second_truck.append(i)
#                     second_truck_indices.append(i[1])
#                     _list.pop(_list.index(i))
#                     curr_location = location
#                     get_shortest_route(_list, 2, curr_location)
#                 elif num == 3:
#                     third_truck.append(i)
#                     third_truck_indices.append(i[1])
#                     _list.pop(_list.index(i))
#                     curr_location = location
#                     get_shortest_route(_list, 3, curr_location)

#     # Insert 0 for the first index of each index list
#     first_truck_indices.insert(0, '0')
#     second_truck_indices.insert(0, '0')
#     third_truck_indices.insert(0, '0')

#     # The following are all helper functions to return a desired value -> O(1)
#     def first_truck_index():
#         return first_truck_indices

#     def first_truck_list():
#         return first_truck

#     def second_truck_index():
#         return second_truck_indices

#     def second_truck_list():
#         return second_truck

#     def third_truck_index():
#         return third_truck_indices

#     def third_truck_list():
#         return third_truck

# class Truck:
#     def __init__(self, truck_id, leave_time):
#         self.truck_id = truck_id
#         self.packages = []
#         self.total_distance = 0
#         self.total_time = leave_time
#         self.total_mileage = 0
#         self.current_weight = 0
#         self.weight_limit = 100  # weight limit for each truck
        
        
#         def load_truck(self):
#              # sort packages based on weight in ascending order
#             package.sort(key=lambda x: x['weight'])

#             for package in package:
#                 if self.current_weight + package['weight'] <= self.weight_limit:
#                     self.packages.append(package)
#                     self.current_weight += package['weight']
#                 else:
#                     # Break the loop if the truck has reached its weight limit
#                     break

#             # remove the packages that have been loaded onto the truck
#             for package in self.package:
#                 package.remove(package)

#     def add_package(self, package):
#         self.packages.append(package)
#         self.total_distance += package.distance  # assuming package has a distance attribute
#         self.total_time += package.time  # assuming package has a time attribute
#         self.total_mileage += package.mileage  # assuming package has a mileage attribute

    
#     def update_total_distance(self, distance):
#         self.total_distance += distance
    
#     def update_package_status(self, distance, delivery_time):
#         # assuming the distance class has these methods and they do what's expected
#         self.total_distance += distance
#         self.total_time += delivery_time
#         for package in self.packages:
#             package[10] = str(self.total_time)  # assuming package has a delivery time at index 10

#     def display_info(self):
#         print(f"Truck ID: {self.truck_id}")
#         print(f"Total Packages: {len(self.packages)}")
#         print(f"Total Distance: {self.total_distance}")
#         print(f"Total Time: {self.total_time}")
#         print(f"Total Mileage: {self.total_mileage}")
#         print("--------------------------------------------------")
#     def display_total_distance(self):
#             print(f"Total distance for truck {self.truck_id}: {self.total_distance}")

# # Create a list of trucks
# trucks = [
#     Truck(1, '8:00:00'),
#     Truck(2, '9:10:00'),
#     Truck(3, '11:00:00')
# ]

# for truck in trucks:
#   #  truck.display_info()
#     truck.display_total_distance()
# # # Create a list of trucks
# # trucks = [
# #     Truck(1, '8:00:00'),
# #     Truck(2, '9:10:00'),
# #     Truck(3, third_truck_indices)
# # ]

# # for truck in trucks:
# #     truck.display_info()

# ###########################################################################






# import csv
# import datetime
# from turtle import distance
#  #from turtle import distance


# class distance:
#     # Initialize the class
#     def __init__(self):
#         # load distance name data
#         with open('./c950/distance_name_data.csv') as distance_name_file:
#             self.name_reader = list(csv.reader(distance_name_file, delimiter=','))

#         # load distance data
#         with open('./c950/distance_data.csv') as distance_file:
#             self.distance_reader = list(csv.reader(distance_file, delimiter=','))

#     # Get package address data -> O(n)
#     def get_address(self):
#         return self.name_reader
    
#      # check distance from current location to another location
#     def check_distance(self, current_location, from_location):
#         row = int(current_location)
#         col = int(from_location)
#         distance = self.distance_reader[row][col]
#         if distance is None or distance == '':
#             distance = self.distance_reader[col][row]
#         return distance

# #     # get number from location address
#     def check_location_num_from_address(self, location):
#         for name in self.name_reader:
#             if location == name[2]:
#                 return name[0]

# #     # get simulated truck time
#     def check_time(self, truck, name):
#         truck_timeline = []
#         if name == 'truck1':
#             truck_time = ['8:00:00']
#         elif name == 'truck2':
#             truck_time = ['9:05:00']
#         elif name == 'truck3':
#             truck_time = ['10:00:00']
#         for t in truck:
#             if truck[0] == t:
#                 pl = 0
#             address = t.get_address()
#             cl = self.check_location_num_from_address(address)
#             d = self.check_distance(cl, pl)
#             pl = cl
#             time = float(d) / 18
#             time_format = '{0:02.0f}:{1:02.0f}:00'.format(*divmod(time * 60, 60))
#             truck_time.append(time_format)
#         total_time = datetime.timedelta()
#         for t in truck_time:
#             total_time += self.get_delta_time(t)
#             truck_timeline.append(total_time)
#         return truck_timeline

# #     # convert string to time delta
#     def get_delta_time(self, s):
#         try:
#             (h, m, s) = s.split(':')
#             dt = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
#             return dt
#         except:
#             print("Error converting to Time Delta")

# #     # get specific time
#     def check_delivery_time(self, truck, truck_time, id):
#         for i in truck:
#             if i.get_package_id() == id:
#                 index = truck.index(i)
#         return truck_time[index+1]
    
    

# #     # Check delivery status and any given time
#     def check_delivery_status(self, t, truck, t_time, name, id):
#         delivery_time = self.check_delivery_time(truck, t_time, id)
#         timestamp = self.get_delta_time(t)
#         truck_time = {'TRUCK 1': self.get_delta_time('8:00:00'),
#                       'TRUCK 2': self.get_delta_time('9:05:00'),
#                       'TRUCK 3': self.get_delta_time('10:00:00')}.get(name, None)
#         if timestamp > delivery_time:
#             return 'DELIVERED'
#         elif timestamp <= delivery_time and timestamp >= truck_time:
#             return 'ON_TRUCK'
#         else:
#             return 'AT_HUB'

#         # calc the total distance traveled by the trucks
#     def get_total_distance_traveled(self, truck):
#         total_miles = 0
#         for t in truck:
#             if truck[0] == t:
#                 previous_location = 0
#             current_location = self.check_location_num_from_address(t.get_address())
#             distance = self.check_distance(current_location, previous_location)
#             total_miles += float(distance)
#             previous_location = current_location
#         return total_miles
    
    
    #################################################3

#     # # calc the total distance traveled by the trucks
#     # def get_total_distance_traveled(self, truck):
#     #     total_miles = 0
#     #     for t in truck:
#     #         if truck[0] == t:
#     #             pl = 0
#     #         cl = self.check_location_num_from_address(t.get_address())
#     #         d = self.check_distance(cl, pl)
#     #         pl = cl
#     #         total_miles += float(d)
#     #     # calc trip back to main hub
#     #     d = self.check_distance(cl, 0)
#     #     total_miles += float(d)
#     #     return round(total_miles, 2)

#     # display data based off time input
#     def display_data_from_time(self, name, truck, truck_timeline, time, distance):
#         print('\n{} || # of packages: {} || Total Distance: {} miles\n'.format(name, len(truck), distance))
#         if time == '':
#             timestamp = '23:00:00'
#         else:
#             timestamp = time
#         for t in truck:
#             i = truck.index(t)
#             id = t.get_package_id()
#             ds = self.check_delivery_status(timestamp, truck, truck_timeline, name, id)
#             s = 'ID: {:>2} -- Deadline: {:>6} -- Status: {:>6} -- Expected Delivery: {}'
#             formatted_string = s.format(id, t.get_deadline(), ds, truck_timeline[i + 1])
#             print(formatted_string)
            
        
#     def create_distance_calc():
#             return distance()  # Create an instance of distance class

#     # these lists represent the sorted trucks that are put in order of efficiency in the function below
#     first_truck = []
#     first_truck_indices = []
#     second_truck = []
#     second_truck_indices = []
#     third_truck = []
#     third_truck_indices = []
    
#     def get_shortest_route(_list, num, curr_location):
            
            
#                 if not len(_list):
#                     return _list

#                 lowest_value = 50.0
#                 location = 0

#                 for i in _list:
#                     value = int(i[1])
#                     if self.check_distance(curr_location, value) <= lowest_value:
#                         lowest_value = self.check_distance(
#                             curr_location, value)
#                         location = value

#                 for i in _list:
#                     if check_distance(curr_location, int(i[1])) == lowest_value:
#                         if num == 1:
#                             self.first_truck.append(i)
#                             first_truck_indices.append(i[1])
#                             _list.pop(_list.index(i))
#                             curr_location = location
#                             get_shortest_route(_list, 1, curr_location)
#                         elif num == 2:
#                             second_truck.append(i)
#                             second_truck_indices.append(i[1])
#                             _list.pop(_list.index(i))
#                             curr_location = location
#                             get_shortest_route(_list, 2, curr_location)
#                         elif num == 3:
#                             third_truck.append(i)
#                             third_truck_indices.append(i[1])
#                             _list.pop(_list.index(i))
#                             curr_location = location
#                             get_shortest_route(_list, 3, curr_location)    
#                             # Insert 0 for the first index of each index list
#                 first_truck_indices.insert(0, '0')
#                 second_truck_indices.insert(0, '0')
#                 third_truck_indices.insert(0, '0')

#                 # The following are all helper functions to return a desired value -> O(1)
#                 def first_truck_index():
#                     return first_truck_indices

#                 def first_truck_list():
#                     return first_truck

#                 def second_truck_index():
#                     return second_truck_indices

#                 def second_truck_list():
#                     return second_truck

#                 def third_truck_index():
#                     return third_truck_indices

#                 def third_truck_list():
#                     return third_truck        
##################################################################################################################################################
# import csv
# import datetime

# class distance:
#     def __init__(self):
#         with open('./c950/distance_name_data.csv') as distance_name_file:
#             self.name_reader = list(csv.reader(distance_name_file, delimiter=','))

#         with open('./c950/distance_data.csv') as distance_file:
#             self.distance_reader = list(csv.reader(distance_file, delimiter=','))

#         self.first_truck = []
#         self.first_truck_indices = []
#         self.second_truck = []
#         self.second_truck_indices = []
#         self.third_truck = []
#         self.third_truck_indices = []

#     def get_address(self):
#         return self.name_reader

#     def check_distance(self, current_location, from_location):
#         row = int(current_location)
#         col = int(from_location)
#         distance = self.distance_reader[row][col]
#         if distance is None or distance == '':
#             distance = self.distance_reader[col][row]
#         return float(distance)

#      # gets the total distance from given row/column value:> O(1)
#     def total_distance(self, current_location, from_location, total):
#         row = int(current_location)
#         col = int(from_location)
#         distance = self.distance_reader[row][col]
#         if distance is None or distance == '':
#             distance = self.distance_reader[col][row]
#         return total + float(distance)
    
#     def check_location_num_from_address(self, location):
#         for name in self.name_reader:
#             if location == name[2]:
#                 return name[0]
            
#     def get_shortest_route(self, _list, num, curr_location):
#             if not len(_list):
#                 return _list

#             lowest_value = 50.0
#             location = 0

#             for i in _list:
#                 value = int(i[1])
#                 if float(self.check_distance(curr_location, value)) <= lowest_value:
#                     lowest_value = self.check_distance(curr_location, value)
#                     location = value

#             for i in _list:
#                 if self.check_distance(curr_location, int(i[1])) == lowest_value:
#                     if num == 1:
#                         self.first_truck.append(i)
#                         self.first_truck_indices.append(i[1])
#                         _list.pop(_list.index(i))
#                         curr_location = location
#                         self.get_shortest_route(_list, 1, curr_location)
#                     elif num == 2:
#                         self.second_truck.append(i)
#                         self.second_truck_indices.append(i[1])
#                         _list.pop(_list.index(i))
#                         curr_location = location
#                         self.get_shortest_route(_list, 2, curr_location)
#                     elif num == 3:
#                         self.third_truck.append(i)
#                         self.third_truck_indices.append(i[1])
#                         _list.pop(_list.index(i))
#                         curr_location = location
#                         self.get_shortest_route(_list, 3, curr_location)

#             self.first_truck_indices.insert(0, '0')
#             self.second_truck_indices.insert(0, '0')
#             self.third_truck_indices.insert(0, '0')       
    

#     def check_time(self, truck, name):
#         truck_timeline = []
#         if name == 'truck1':
#             truck_time = ['8:00:00']
#         elif name == 'truck2':
#             truck_time = ['9:05:00']
#         elif name == 'truck3':
#             truck_time = ['10:00:00']
#         for t in truck:
#             if truck[0] == t:
#                 pl = 0
#             address = t.get_address()
#             cl = self.check_location_num_from_address(address)
#             d = self.check_distance(cl, pl)
#             pl = cl
#             time = float(d) / 18
#             time_format = '{0:02.0f}:{1:02.0f}:00'.format(*divmod(time * 60, 60))
#             truck_time.append(time_format)
#         total_time = datetime.timedelta()
#         for t in truck_time:
#             total_time += self.get_delta_time(t)
#             truck_timeline.append(total_time)
#         return truck_timeline

#     def get_delta_time(self, s):
#         try:
#             (h, m, s) = s.split(':')
#             dt = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
#             return dt
#         except:
#             print("Error converting to Time Delta")

#     # def check_delivery_time(self, truck, truck_time, id):
#     #     for i in truck:
#     #         if i.get_package_id() == id:
#     #             index = truck.index(i)
#     #     return truck_time[index+1]
    
#     def calculate_delivery_time(self, distance, start_time):
#         time = float(distance) / 18
#         time_format = '{0:02.0f}:{1:02.0f}:00'.format(*divmod(time * 60, 60))
#         delivery_time = self.add_times(start_time, time_format)
#         return delivery_time

#     def add_times(self, start, duration):
#         start_datetime = datetime.datetime.strptime(start, '%H:%M:%S')
#         duration_timedelta = self.get_delta_time(duration)
#         end_datetime = start_datetime + duration_timedelta
#         return end_datetime.strftime('%H:%M:%S')


#     def check_delivery_status(self, t, truck, t_time, name, id):
#         delivery_time = self.check_delivery_time(truck, t_time, id)
#         timestamp = self.get_delta_time(t)
#         truck_time = {'TRUCK 1': self.get_delta_time('8:00:00'),
#                       'TRUCK 2': self.get_delta_time('9:05:00'),
#                       'TRUCK 3': self.get_delta_time('10:00:00')}.get(name, None)
#         if timestamp > delivery_time:
#             return 'DELIVERED'
#         elif timestamp <= delivery_time and timestamp >= truck_time:
#             return 'ON_TRUCK'
#         else:
#             return 'AT_HUB'

#     def get_total_distance_traveled(self, truck):
#         total_miles = 0
#         for t in truck:
#             if truck[0] == t:
#                 previous_location = 0
#             current_location = self.check_location_num_from