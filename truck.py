class Truck:
    truck1 = []
    truck2 = []
    truck3 = []

    # sort the packages onto the trucks - semi random
    def sort_packages_into_priorities(self, packages):
        priority_truck_1 = []
        np_truck_1 = []
        priority_truck_2 = []
        np_truck_2 = []
        non_priority = []
        for p in packages:
            notes = p.get_notes()
            deadline = p.get_deadline()
            address = p.get_address()

            if id == 13 or id == 15 or id == 19:
                priority_truck_1.append(p)
            elif 'Can only be on' in notes or 'Delayed on flight' in notes:
                priority_truck_2.append(p)
            elif 'Wrong address listed' in notes:
                p.set_address('410 S State St')
                p.set_zip('84111')
                non_priority.append(p)
            elif 'Must be delivered' in notes and deadline != 'EOD':
                priority_truck_1.append(p)
            elif deadline != 'EOD':
                ft_address = []
                for t in priority_truck_1:
                    ft_address.append(t.get_address())
                if address in ft_address:
                    np_truck_1.append(p)
                else:
                    np_truck_2.append(p)
            elif '10:30' not in deadline:
                non_priority.append(p)
            else:
                non_priority.append(p)

        for t in priority_truck_1:
            if len(self.truck1) < 16:
                self.truck1.append(t)
        for t in np_truck_1:
            if len(self.truck1) < 16:
                self.truck1.append(t)
        for t in priority_truck_2:
            if len(self.truck2) < 16:
                self.truck2.append(t)
        for t in np_truck_2:
            if len(self.truck1) < 16:
                self.truck1.append(t)
            elif len(self.truck2) < 16:
                self.truck2.append(t)
            else:
                self.truck3.append(t)
        for t in non_priority:
            if len(self.truck3) < 16:
                self.truck3.append(t)
            elif len(self.truck2) < 16:
                self.truck2.append(t)
            elif len(self.truck1) < 16:
                self.truck1.append(t)
            else:
                print('Not enough room on trucks')
# import csv
# import datetime

# # Read CSV files
# with open('c950/distance_data.csv') as csvfile_1:
#     distance_csv = list(csv.reader(csvfile_1, delimiter=','))
# with open('c950/distance_name_data.csv') as csvfile_2:
#     distance_name_csv = list(csv.reader(csvfile_2, delimiter=','))

# class Truck:
#     def __init__(self, id, packages, indices, total_time=0, total_mileage=0):
#         self.id = id
#         self.packages = packages
#         self.indices = indices
#         self.total_time = total_time
#         self.total_mileage = total_mileage
#         self.total_packages_delivered = 0  
#         self.total_packages_not_delivered = len(packages)

#     def __str__(self):
#         return "Truck ID: %s | Total Packages: %s | Total Distance: %s | Total Time: %s | Total Mileage: %s" % (
#             self.id, len(self.packages), self.calculate_total_distance(), self.total_time, self.total_mileage)

#     def deliver_package(self, package):
#         # Here you should put the code that changes the package's status to delivered
#         # and remove the package from the truck's packages.
#         # For the sake of example, I'm just going to assume that package is the id of the package.
#         for i in range(len(self.packages)):
#             if self.packages[i].id == package:
#                 # Update T1 and T2
#                 self.packages[i].T1 = datetime.datetime.now()
#                 self.packages[i].T2 = self.packages[i].T1 + datetime.timedelta(hours=self.packages[i].deadline)
#                 self.packages.pop(i)
#                 self.total_packages_delivered += 1
#                 self.total_packages_not_delivered -= 1
#                 break

#     def calculate_total_distance(self):
#         total_distance = 0
#         for i in range(1, len(self.indices)):
#             total_distance += get_current_distance(self.indices[i-1], self.indices[i])
#         return total_distance

# # Get package address data -> O(n)
# def get_address():
#     return distance_name_csv

# # Calculate the total distance from row/column values -> O(1)
# def get_distance(row, col, total):
#     distance = distance_csv[row][col]
#     if distance == '':
#         distance = distance_csv[col][row]
#     return total + float(distance)

# # Calculate the current distance from row/column values -> O(1)
# def get_current_distance(row, col):
#     distance = distance_csv[row][col]
#     if distance == '':
#         distance = distance_csv[col][row]
#     return float(distance)

# # Calculate total distance for a given truck -> O(n)
# def get_time(distance, truck_list):
#     new_time = distance / 18
#     distance_in_minutes = '{0:02.0f}:{1:02.0f}'.format(
#         *divmod(new_time * 60, 60))
#     final_time = distance_in_minutes + ':00'
#     truck_list.append(final_time)
#     total = datetime.timedelta()
#     for i in truck_list:
#         (hrs, mins, secs) = i.split(':')
#         total += datetime.timedelta(hours=int(hrs),
#                                     minutes=int(mins), seconds=int(secs))
#     return total

# # these lists represent the sorted trucks that are put in order of efficiency in the function below
# first_truck = []
# first_truck_indices = []
# second_truck = []
# second_truck_indices = []
# third_truck = []
# third_truck_indices = []

# def get_shortest_route(_list, num, curr_location):
#     if not len(_list):
#         return _list

#     lowest_value = 50.0
#     location = 0

#     for i in _list:
#         value = int(i[1])
#         if get_current_distance(curr_location, value) <= lowest_value:
#             lowest_value = get_current_distance(
#                 curr_location, value)
#             location = value

#     for i in _list:
#         if get_current_distance(curr_location, int(i[1])) == lowest_value:
#             if num == 1:
#                 first_truck.append(i)
#                 first_truck_indices.append(i[1])
#                 _list.pop(_list.index(i))
#                 curr_location = location
#                 get_shortest_route(_list, 1, curr_location)
#             elif num == 2:
#                 second_truck.append(i)
#                 second_truck_indices.append(i[1])
#                 _list.pop(_list.index(i))
#                 curr_location = location
#                 get_shortest_route(_list, 2, curr_location)
#             elif num == 3:
#                 third_truck.append(i)
#                 third_truck_indices.append(i[1])
#                 _list.pop(_list.index(i))
#                 curr_location = location
#                 get_shortest_route(_list, 3, curr_location)

# # Insert 0 for the first index of each index list
# def create_trucks():
#     # Insert 0 for the first index of each index list
#     first_truck_indices.insert(0, '0')
#     second_truck_indices.insert(0, '0')
#     third_truck_indices.insert(0, '0')

#     truck1 = Truck(1, first_truck, first_truck_indices)
#     truck2 = Truck(2, second_truck, second_truck_indices)
#     truck3 = Truck(3, third_truck, third_truck_indices)
    
#     print(truck1)
#     print(truck2)
    
    
#     return truck1, truck2, truck3

# if __name__=="__main__":
#     print(create_trucks())
##################################################################################
# import csv
# import datetime

# class Truck:

#     def __init__(self):
#         self.truck = []
#         self.truck_indices = []

#     def get_shortest_route(self, _list, curr_location):
#         if not len(_list):
#             return _list

#         lowest_value = 50.0
#         location = 0

#         for i in _list:
#             value = int(i[1])
#             if self.get_current_distance(curr_location, value) <= lowest_value:
#                 lowest_value = self.get_current_distance(curr_location, value)
#                 location = value

#         for i in _list:
#             if self.get_current_distance(curr_location, int(i[1])) == lowest_value:
#                 self.truck.append(i)
#                 self.truck_indices.append(i[1])
#                 _list.pop(_list.index(i))
#                 curr_location = location
#                 self.get_shortest_route(_list, curr_location)

#     def get_truck_indices(self):
#         return self.truck_indices

#     def get_truck_list(self):
#         return self.truck

#     # ... other functions (like get_current_distance, get_address, etc.) ...

# # read CSV files
# def read_csv():
#     with open('./c950/distance_data.csv') as csvfile_1:
#         distance_csv = list(csv.reader(csvfile_1, delimiter=','))
#     with open('./c950/distance_name_data.csv') as csvfile_2:
#         distance_name_csv = list(csv.reader(csvfile_2, delimiter=','))
#     return distance_csv, distance_name_csv