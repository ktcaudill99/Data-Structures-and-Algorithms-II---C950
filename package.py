import datetime
import datetime
from distance import *
import csv_reader

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



# Create an instance of distance
distance_calc = distance()

# Empty lists created
first_delivery = []
second_delivery = []
third_delivery = []
first_truck_distance = []
second_truck_distance = []
third_truck_distance = []

# # Times the trucks leave the hub
# first_leave_times = ['8:00:00']
# second_leave_times = ['9:10:00']
# third_leave_times = ['11:00:00']

# # Set delivery_start to first_leave_time for all truck one packages -> O(n)
# for index, value in enumerate(csv_reader.get_first_delivery()):
#     csv_reader.get_first_delivery()[index][9] = first_leave_times[0]
#     first_delivery.append(csv_reader.get_first_delivery()[index])
    
# # Compare truck one addresses to address list -> O(n^2)
# for index, outer in enumerate(first_delivery):
#     for inner in distance_calc.get_address():
#         if outer[2] == inner[2]:
#             first_truck_distance.append(outer[0])
#             first_delivery[index][1] = inner[0]

# # Call algorithm to sort packages for first truck
# distance_calc.get_shortest_route(first_delivery, 1, 0)
# total_distance_1 = 0

# # Calculate total distance of the first truck and distance of each package -> O(n)
# for index in range(len(distance_calc.first_truck_indices)):
#     try:
#         total_distance_1 = distance_calc.check_distance(int(distance_calc.first_truck_indices()[index]), int(distance_calc.first_truck_indices()[index + 1]), total_distance_1)
        
#         deliver_package = distance_calc.get_time(distance_calc.get_current_distance(int(distance_calc.first_truck_indices()[index]), int(distance_calc.first_truck_indices()[index + 1])), first_leave_times)
#         distance_calc.first_truck_list()[index][10] = (str(deliver_package))
#         csv_reader.get_hash_map().update(int(distance_calc.first_truck_list()[index][0]), first_delivery)
#     except IndexError:
#         pass

# # Set delivery_start to second_leave_time for all truck two packages -> O(n)
# for index, value in enumerate(csv_reader.get_second_delivery()):
#     csv_reader.get_second_delivery()[index][9] = second_leave_times[0]
#     second_delivery.append(csv_reader.get_second_delivery()[index])

# # Compare truck two addresses to address list -> O(n^2)
# for index, outer in enumerate(second_delivery):
#     for inner in distance_calc.get_address():
#         if outer[2] == inner[2]:
#             second_truck_distance.append(outer[0])
#             second_delivery[index][1] = inner[0]

# # Call algorithm to sort packages for second truck
# distance_calc.get_shortest_route(second_delivery, 2, 0)
# total_distance_2 = 0

# # Calculate total distance of the second truck and distance of each package -> O(n)
# for index in range(len(distance_calc.second_truck_indices)):
#     try:
#         total_distance_2 = distance_calc.check_distance(int(distance_calc.second_truck_indices()[index]), int(distance_calc.second_truck_indices()[index + 1]), total_distance_2)
#         deliver_package = distance_calc.get_time(distance_calc.get_current_distance(int(distance_calc.second_truck_indices()[index]), int(distance_calc.second_truck_indices()[index + 1])), second_leave_times)
#         distance_calc.second_truck_list()[index][10] = (str(deliver_package))
#         csv_reader.get_hash_map().update(int(distance_calc.second_truck_list()[index][0]), second_delivery)
#     except IndexError:
#         pass

# # Set delivery_start to third_leave_time for all truck three packages -> O(n)
# for index, value in enumerate(csv_reader.get_final_delivery()):
#     csv_reader.get_final_delivery()[index][9] = third_leave_times[0]
#     third_delivery.append(csv_reader.get_final_delivery()[index])

# # Compare truck three addresses to address list -> O(n^2)
# for index, outer in enumerate(third_delivery):
#     for inner in distance_calc.get_address():
#         if outer[2] == inner[2]:
#             third_truck_distance.append(outer[0])
#             third_delivery[index][1] = inner[0]

# # Call algorithm to sort packages for third truck
# distance_calc.get_shortest_route(third_delivery, 3, 0)
# total_distance_3 = 0

# # Calculate total distance of the third truck and distance of each package -> O(n)
# for index in range(len(distance_calc.third_truck_indices)):
#     try:
#         total_distance_3 = distance_calc.check_distance(int(distance_calc.third_truck_indices()[index]), int(distance_calc.third_truck_indices()[index + 1]), total_distance_3)
        
#         deliver_package = distance_calc.get_time(distance_calc.get_current_distance(int(distance_calc.third_truck_indices()[index]), int(distance_calc.third_truck_indices()[index + 1])), third_leave_times)
#         distance_calc.third_truck_list()[index][10] = (str(deliver_package))
#         csv_reader.get_hash_map().update(int(distance_calc.third_truck_list()[index][0]), third_delivery)
#     except IndexError:
#         pass

# # Get distance of all packages -> O(1)
# def total_distance():
#     return total_distance_1 + total_distance_2 + total_distance_3
#------------------------------------------------------------------------------------
# import csv_reader

# # Empty lists created
# first_tr_pk_list = []
# second_tr_pk_list = []
# third_tr_pk_list = []

# first_tr_distance = []
# second_tr_distance = []
# third_tr_distance = []

# # initial leave time for trucks
# first_tr_start_time = ['8:00:00']
# second_tr_start_time = ['9:10:00']
# third_tr_start_time = ['11:00:00']

# # ================================================= first truck ======================================================

# distance_instance = distance()  # Creating an instance of the 'distance' class
# addresses = distance_instance.get_address()  # Calling the 'get_address' method on the instance



# # set delivery start time to packets of truck 1   :> O(n)
# for index, value in enumerate(csv_reader.get_first_delivery()):
#     csv_reader.get_first_delivery()[index][9] = first_tr_start_time[0]
#     first_tr_pk_list.append(csv_reader.get_first_delivery()[index])

# # Compare first truck addresses to full address list :> O(n^2)
# for index, outer in enumerate(first_tr_pk_list):
#     for inner in distance_instance.get_address():
#         if outer[2] == inner[2]:
#             first_tr_distance.append(outer[0])
#             first_tr_pk_list[index][1] = inner[0]

# # Call greedy  algorithm to sort packages for first truck
# distance_instance.get_shortest_route(first_tr_pk_list, 1, 0)
# total_DistanceClac_tr1 = 0

# # Calculate :> O(n)
# # 1.Total distance of the First truck
# # 2.distance of each packages
# for index in range(len(distance_instance.first_truck_indices[index])):
#     try:
#         total_DistanceClac_tr1 = distance_instance.total_distance(
#             int(distance_instance.first_truck_indices[index]),
#             int(distance_instance.first_truck_indices[index + 1]),
#             total_DistanceClac_tr1
#         )
#         deliver_package = distance_instance.check_distance(int(distance_instance.first_truck_indices[index]),
#                                                    int(distance_instance.first_truck_indices[index + 1]))

#         distance_instance.first_truck[index][10] = (str(deliver_package))
#         csv_reader.get_hash_table().update(int(distance_instance.first_truck[index][0]), first_tr_pk_list)
#     except IndexError:
#         pass

# # ================================================= Second truck ======================================================

# # set delivery start time to packets of truck 1   :> O(n)
# for index, value in enumerate(csv_reader.get_second_delivery()):
#     csv_reader.get_second_delivery()[index][9] = second_tr_start_time[0]
#     second_tr_pk_list.append(csv_reader.get_second_delivery()[index])

# # Compare Second truck addresses to full address list :> O(n^2)
# for index, outer in enumerate(second_tr_pk_list):
#     for inner in distance_instance.get_address():
#         if outer[2] == inner[2]:
#             second_tr_distance.append(outer[0])
#             second_tr_pk_list[index][1] = inner[0]

# # Call greedy  algorithm to sort packages for Second truck
# distance_instance.get_shortest_route(second_tr_pk_list, 2, 0)
# total_distance_tr2 = 0


# # Calculate :> O(n)
# # 1.Total distance of the Second truck
# # 2.distance of each package
# for index in range(len(distance_instance.second_truck_indices)):
#     try:
#         total_distance_tr2 = distance_instance.total_distance(int(distance_instance.second_truck_indices[index]),
#                                                     int(distance_instance.second_truck_indices[index + 1]),
#                                                     total_distance_tr2)

#         package_distance = distance_instance.check_distance(int(distance_instance.second_truck_indices[index]),
#                                            int(distance_instance.second_truck_indices[index + 1]))
#         deliver_package = distance_instance.calculate_delivery_time(package_distance, second_tr_start_time[0])
        
#         distance_instance.second_truck[index][10] = (str(deliver_package))
#         csv_reader.get_hash_table().update(int(distance_instance.second_truck[index][0]), second_tr_pk_list)
#     except IndexError:
#         pass

# # ================================================= Third truck ======================================================

# # set delivery start time to packets of truck 3   :> O(n)
# for index, value in enumerate(csv_reader.get_final_delivery()):
#     csv_reader.get_final_delivery()[index][9] = third_tr_start_time[0]
#     third_tr_pk_list.append(csv_reader.get_final_delivery()[index])

# # Compare Third truck addresses to full address list :> O(n^2
# for index, outer in enumerate(third_tr_pk_list):
#     for inner in distance_instance.get_address():
#         if outer[2] == inner[2]:
#             third_tr_distance.append(outer[0])
#             third_tr_pk_list[index][1] = inner[0]

# # Call greedy  algorithm to sort packages for Third truck
# distance_instance.get_shortest_route(third_tr_pk_list, 3, 0)
# total_distance_tr3 = 0

# # Calculate :> O(n)
# # 1.Total distance of the Third truck
# # 2.distance of each package
# for index in range(len(distance_instance.third_truck_indices[index])):
#     try:
#         total_distance_tr3 = distance_instance.total_distance(int(distance_instance.third_truck_indices[index]),
#                                                     int(distance_instance.third_truck_indices[index + 1]),
#                                                     total_distance_tr3)

#         deliver_package = distance_instance.check_time(
#            distance_instance.check_distance(int(distance_instance.third_truck_indices[index]),
#                                            int(distance_instance.third_truck_indices[index + 1])),
#             third_tr_start_time)
#         distance_instance.third_truck[index][10] = (str(deliver_package))
#         csv_reader.get_hash_table().update(int(distance_instance.third_truck[index][0]), third_tr_pk_list)
#     except IndexError:
#         pass

# """
# for testing only 
# -------------------------------------
# #check each truck's total distance
# print(total_distance_tr1)
# print(total_distance_tr2)
# print(total_distance_tr3)
# """


# # Get the total distance of all 40 packages :> O(1)
# def total_distance_all_tr():
#     return total_distance_tr1 + total_distance_tr2 + total_distance_tr3