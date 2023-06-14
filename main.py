# import datetime
# from hashtable import *
# from distance import *
# from route import *
# from truck import  *
# from csv_reader import *
# from package import *
# #from distance import create_distance_calc
# import re
# #####################################################################################
# #data = hashtable()

# # reusable print  functions :> O(1)
# def print_status(count):
#     print(

#         f'Package ID: {get_hash_table().search(str(count))[0]}', """    """
#                                                                  f'Truck load time: {get_hash_table().search(str(count))[9]}',
#         """    """
#         f'Deli1very status: {get_hash_table().search(str(count))[10]}'
#     )


# # reusable print  functions :> # O(1)
# def print_pk_detail(count):
#     print(
#         '-' * 30, 'package information', '-' * 49, '\n'
#                                                    f'Package ID: {get_hash_table().search(str(count))[0]}\n'
#                                                    f'Street address: {get_hash_table().search(str(count))[2]}, '
#                                                    f'{get_hash_table().search(str(count))[3]}, '
#                                                    f'{get_hash_table().search(str(count))[4]}, '
#                                                    f'{get_hash_table().search(str(count))[5]},\n'

#                                                    f'Delivery deadline : {get_hash_table().search(str(count))[6]}\n'
#                                                    f'Package weight: {get_hash_table().search(str(count))[7]} KG\n'
#                                                    f'Special note: {get_hash_table().search(str(count))[8]}\n',
#         '-' * 30, 'delivery status', '-' * 51,
#     )
# # class Truck:
# #     def __init__(self, id, packages, indices, total_time=0, total_mileage=0):
# #         self.id = id
#     # truck2.total_packages_not_delivered = 0
#     # truck3.total_packages_not_delivered = 0


# if __name__ == '__main__':
#     # create objects and load csv data
    
#     #distance = create_distance_calc()
#     truck1, truck2, truck3 = create_trucks()
#     #distance = Distance().create_distance()
#     #distance = create_distance_calc()
    
#     # Read CSV files
#     with open('c950/distance_data.csv') as csvfile_1:
#         distance_csv = list(csv.reader(csvfile_1, delimiter=','))
#     with open('c950/distance_name_data.csv') as csvfile_2:
#         distance_name_csv = list(csv.reader(csvfile_2, delimiter=','))

#     # User Interface
#     # Upon running the program, the below message will appear.
#     print("Western Governors University Parcel Service (WGUPS)")
#     print("The mileage for the route is:")
#    # print(truck1.mileage + truck2.mileage + truck3.mileage)  # Print total mileage for all trucks
#    # distance.display_data_from_time("TRUCK 1", optimized_truck_1, truck_timeline_1, "", td1)
#    # distance.display_data_from_time("TRUCK 2", optimized_truck_2, truck_timeline_2, "", td2)
#    # distance.display_data_from_time("TRUCK 3", optimized_truck_3, truck_timeline_3, "", td3)
#    # print('Total Distance = {} Miles\n'.format(total_distance))


#     # display today's date and time
#     now = datetime.datetime.now()
#     cur_time = now.strftime("%H:%M:%S\n")
#     cur_date = now.strftime("%Y-%m-%d\n")
#     print(""" #Today is          :""", cur_date, """#Current time      :""", cur_time)


#    # for package in data.get_all_values():
#    #     print(package)

#     # display package data
#     print("WGUPS Package Data")
#     print("------------------------------------------------------------------------------------------------------------------------")
#     print("Package ID | Address | City | State | Zip | Deadline | Weight | Status | Delivery Time | Notes")
#     print("------------------------------------------------------------------------------------------------------------------------")

#     print("------------------------------------------------------------------------------------------------------------------------")
#     print("Total Packages Delivered: ", len(truck1.packages) + len(truck2.packages) + len(truck3.packages))
#     print("Total Packages Not Delivered: ", truck1.total_packages_not_delivered + truck2.total_packages_not_delivered + truck3.total_packages_not_delivered)
#    # print("Total Packages: ", len(data.packages))
#     print("Total Distance: ",)# total_distance)
#     print("Total Time: ", truck1.total_time + truck2.total_time + truck3.total_time)
#     print("Total Mileage: ", truck1.total_mileage + truck2.total_mileage + truck3.total_mileage)
#     print("------------------------------------------------------------------------------------------------------------------------")
#     print("WGUPS Truck Data")
#     print("------------------------------------------------------------------------------------------------------------------------")
#     print("Truck ID | Total Packages | Total Distance | Total Time | Total Mileage")
#     print("------------------------------------------------------------------------------------------------------------------------")
#     print(truck1)
#     print(truck2)
#     print(truck3)
    
#         # initial user selection : report for  1 packet or all packets
#     user_input = int(input("""
#     TYPE 1 : To  lookup  ALL  package packages 
#     TYPE 2 : To  lookup  an individual package\n  
#     TYPE quit : To  quit\n"""))
#     if user_input > 2 or user_input < 1:
#         print("Invalid entry")
#         exit()

#     while user_input != 'quit':

#         # user input : Timeframe to retrieve report
#         input_time_raw = input('Enter a time to retrieve report (HH:MM:SS):\n')
#         print('-' * 100)
#         (hrs0, mins0, secs0) = input_time_raw.split(':')
#         input_time = datetime.timedelta(hours=int(hrs0), minutes=int(mins0), seconds=int(secs0))

#         # Case if user selects Option #1
#         # Get info for all packages at a particular time :> O(n)
#         # ---------------------------------------- CASE 1: ALL PACKET REPORT  -----------------------------------------
#         if user_input == 1:
#             try:
#                 for count in range(1, 41):
#                     package = get_hash_table().search(str(count))

#                     t1_temp = package[9]
#                     t2_temp = package[10]
                    
#                     (hrs1, mins1, secs1) = t1_temp.split(':')
#                     (hrs2, mins2, secs2) = t2_temp.split(':')

#                     T1 = datetime.timedelta(hours=int(hrs1), minutes=int(mins1), seconds=int(secs1))
#                     T2 = datetime.timedelta(hours=int(hrs2), minutes=int(mins2), seconds=int(secs2))
     
#                     # Determine which packages have left the hub
#                     if T1 >= input_time:
#                         package[10] = 'At Hub'
#                         package[9] = t1_temp
#                         print_status(count)  # Print package's current info

#                     # Determine which packages have left but have not been delivered
#                     elif T1 <= input_time:
#                         if input_time < T2:
#                             package[10] = 'In transit'
#                             package[9] = t1_temp
#                             print_status(count)  # Print package's current info

#                         # Determine which packages have already been delivered
#                         else:
#                             package[10] = 'Delivered at ' + t2_temp
#                             package[9] = t1_temp
#                             print_status(count)  # Print package's current info
#                 break

#             except IndexError:
#                 print(IndexError)
#                 exit()
#             except ValueError:
#                 print('Invalid entry!')
#                 exit()



#             # Case if user selects Option #2
#             # Get info for a single package at a particular time -> O(n)
#             # ------------------------------ CASE 2 : SINGLE PACKET REPORT ------------------------------------------------
#         elif user_input == 2:
#             try:
#                 # Time variables (T1 : start time, T2: delivery time )
#                 count = input('Enter a valid package ID: \n')
#                 package = get_hash_table().search(str(count))

#                 t1_temp = package[9]
#                 t2_temp = package[10]
                
#                 (hrs1, mins1, secs1) = t1_temp.split(':')
#                 (hrs2, mins2, secs2) = t2_temp.split(':')

#                 T1 = datetime.timedelta(hours=int(hrs1), minutes=int(mins1), seconds=int(secs1))
#                 T2 = datetime.timedelta(hours=int(hrs2), minutes=int(mins2), seconds=int(secs2))


#                 print_pk_detail(count)  # prints specified packet's info

#                     # Determine which packages have left the hub
#                 if T1 >= input_time:
#                     package[10] = 'At Hub'
#                     package[9] = t1_temp
#                     print_status(count)  # Print package's current delivery status

#                 # Determine which packages have left but have not been delivered
#                 elif T1 <= input_time:
#                     if input_time < T2:
#                         package[10] = 'In transit'
#                         package[9] = t1_temp
#                         print_status(count)  # Print package's current delivery status

#                         # Determine which packages have already been delivered
#                     else:
#                         package[10] = 'Delivered at ' + t2_temp
#                         package[9] = t1_temp
#                         print_status(count)  # Print package's current delivery status

#             except ValueError:
#                     print('Invalid entry')
#                     exit()

#         else:
#             print('Invalid entry!')
#             exit()
# ################################################################################################3
# #ideas---------------------------------------------------------------
# from HashTable import HashTable
# from Truck import Truck
# from datetime import datetime, timedelta
# from Package import Package
# import re

# # Create global variables
# receiveing = HashTable()
# global_time = datetime(2023,6,8,8,00)
# truck1 = Truck(receiveing.handload_truck_1(), datetime(2023,6,8,9,5), 1, receiveing)
# truck2 = Truck(receiveing.handload_truck_2(), datetime(2023,6,8,8,00), 2, receiveing)
# truck3 = Truck(receiveing.handload_truck_3(), datetime(2023,6,8,23,59), 3, receiveing)

# # The main function
# def main():
#     # TODO: Implement the main loop here. You will need to integrate the remaining 
#     # parts of your code into the main function here. This will involve calling the 
#     # relevant functions from the respective classes (Truck, HashTable, Package) at 
#     # the right times and in the right order.

#     # Main loop.  Prompts user for actions until exit is chosen. 
#     while True:
#         print(f''' 
#         Current time = {global_time.hour}:{global_time.minute:>02}

#         1) Set time of day
#         2) Print current package & truck status
#         3) Insert new package
#         4) Lookup package based on address
#         5) Lookup package based on city
#         6) Lookup package based on zip code
#         7) Lookup package based on weight
#         8) Lookup package based on deadline
#         9) Lookup package based on status
#         0) Exit program
#         ''')

#         selection = input('Please select an option: ').strip()

#         # 1) Set time of day
#         if selection == '1':
#             run_deliveries()

#         # 2) Print current package & truck status
#         elif selection == '2':
#             print_status()

#         # 3) Insert new package
#         elif selection == '3':
#             create_new_package()

#         # 4) Lookup package based on address
#         elif selection == '4':
#             address = input('Enter the address you would like to lookup: ')
#             receiveing.lookup('address', address)
            
#         # 5) Lookup package based on city
#         elif selection == '5':
#             city = input('Enter the city you would like to lookup: ')
#             receiveing.lookup('city', city)

#         # 6) Lookup package based on zip code
#         elif selection == '6':
#             zip_code = input('Enter the zip code you would like to lookup: ')
#             receiveing.lookup('zip_code', zip_code)

#         # 7) Lookup package based on weight
#         elif selection == '7':
#             weight = input('Enter the weight you would like to lookup: ')
#             receiveing.lookup('weight', weight)

#         # 8) Lookup package based on deadline
#         elif selection == '8':
#             deadline = input('Enter the deadline you would like to lookup: ')
#             receiveing.lookup('deadline', deadline)

#         # 9) Lookup package based on status
#         elif selection == '9':
#             status = input('Enter the status you would like to lookup: ')
#             receiveing.lookup('status', status)

#         # 0) Exit program
#         elif selection == '0':
#             print('Thank you for choosing WGUPS!\nGoodbye....')
#             exit()

#         # Invalid input
       
       
#from csv_reader import get_hash_table
# from package import total_distance
# import datetime
# from csv_reader import get_first_delivery, get_second_delivery, get_final_delivery
# from package import total_distance
# import distance
# from distance import Truck
# from distance import trucks
from hashtable import HashTable
from distance import Distance
from route import Route
from truck import Truck
import re
import datetime

class Main:
    # first_delivery = get_first_delivery()
    # second_delivery = get_second_delivery()
    # final_delivery = get_final_delivery()

    # for truck in trucks:
    #     if truck.truck_id == 1:
    #         truck.load_truck(first_delivery)
    #     elif truck.truck_id == 2:
    #         truck.load_truck(second_delivery)
    #     elif truck.truck_id == 3:
    #         truck.load_truck(final_delivery)

    # for truck in trucks:
    #     truck.display_info()
#     # This is the display message that is shown when the user runs the program. The interface is accessible from here
#     print('------------------------------')
#     print('WGUPS Routing Program!')
#     print('------------------------------\n')
#     print(f'Route was completed in {total_distance():.2f} miles.\n')
    # display today's date and time
    now = datetime.datetime.now()
    cur_time = now.strftime("%H:%M:%S\n")
    cur_date = now.strftime("%Y-%m-%d\n")
    print("#Today is: ", cur_date)
    print("#Current time: ", cur_time)
    data = HashTable()
    distance = Distance()
    route = Route(distance)
    ts = Truck()
    ts.sort_packages_into_priorities(data.packages)
    # optimize truck routes
    optimized_truck_1 = route.optimize_route(ts.truck1)
    optimized_truck_2 = route.optimize_route(ts.truck2)
    optimized_truck_3 = route.optimize_route(ts.truck3)
    truck_timeline_1 = distance.check_time(optimized_truck_1, 'truck1')
    truck_timeline_2 = distance.check_time(optimized_truck_2, 'truck2')
    truck_timeline_3 = distance.check_time(optimized_truck_3, 'truck3')
    # calc distance
    td1 = distance.get_total_distance_traveled(optimized_truck_1)
    td2 = distance.get_total_distance_traveled(optimized_truck_2)
    td3 = distance.get_total_distance_traveled(optimized_truck_3)
    total_distance = td1 + td2 + td3
    # for package in data.get_all_values():
    #     print(package)

    # display package data
    print("WGUPS Current Package Data")
    # print("------------------------------------------------------------------------------------------------------------------------")
    # print("Package ID | Address | City | State | Zip | Deadline | Weight | Status | Delivery Time | Notes")
    # print("------------------------------------------------------------------------------------------------------------------------")

    # for package in distance.first_truck_list() + distance.second_truck_list() + distance.third_truck_list():
    #     print(" | ".join(str(x) for x in package))
  #  total_packages_delivered = len(distance.first_truck_list()) + len(distance.second_truck_list()) + len(distance.third_truck_list())
  #  total_packages_not_delivered = len(get_first_delivery()) + len(get_second_delivery()) + len(get_final_delivery()) - total_packages_delivered
    # print("Total packages delivered: ", total_packages_delivered)
    # print("Total packages not delivered: ", total_packages_not_delivered)

    print("------------------------------------------------------------------------------------------------------------------------")
#    print("Total Packages Delivered: ", total_packages_delivered)
#    print("Total Packages Not Delivered: ", total_packages_not_delivered)
    # print("Total Packages: ", len(data.packages))
    print("Truck 1 Distance: ", td1)
    print("Truck 2 Distance: ", td2)
    print("Truck 3 Distance: ", td3)
    print("Total Distance:   ", total_distance)
    print("------------------------------------------------------------------------------------------------------------------------")
    print("WGUPS Truck Data")
    print("------------------------------------------------------------------------------------------------------------------------")
    print("Truck ID | Total Packages | Total Distance | Total Time | Total Mileage")
    print("------------------------------------------------------------------------------------------------------------------------")

    # for truck in trucks:
    #     truck.display_info()
 

    while True:
        user_input = input("""
    Please select an option below to begin or type 'quit' to quit:
        1. Get info for all packages at a particular time
        2. Get all packages current status
        3. Get info for a single package at a particular time
    """)
#if user input is quit or q, exit the program
        if user_input == 'quit':
            print('Thank you for using WGUPS!')
            break
        elif user_input == 'q':
            print('Thank you for using WGUPS!')
            break
        # Case if user selects Option #1
        # Get info for all packages at a particular time -> O(n)
        elif user_input == '1':
            try:
                input_time = input('Enter a time (HH:MM): ')
                hrs, mins = input_time.split(':')
                secs = 0  # default seconds to 0
                convert_user_time = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))


                # Complexity ->  O(n^2)
                for count in range(1,41):
                    try:
                        # first_time = get_hash_table().get_value(str(count))[9]
                        # second_time = get_hash_table().get_value(str(count))[10]
                        (hrs, mins, secs) = first_time.split(':')
                        convert_first_time = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))
                        (hrs, mins, secs) = second_time.split(':')
                        convert_second_time = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))
                    except ValueError:
                        pass
                    
                    # Determine which packages have left the hub
                    if convert_first_time >= convert_user_time:
                        # get_hash_table().get_value(str(count))[10] = 'At Hub'
                        # get_hash_table().get_value(str(count))[9] = 'Leaves at ' + first_time

                        # Print package's current info
                        print(
                            # f'Package ID: {get_hash_table().get_value(str(count))[0]}, '
                            # f'Delivery status: {get_hash_table().get_value(str(count))[10]}'
                        )

                    # Determine which packages have left but have not been delivered
                    elif convert_first_time <= convert_user_time:
                        if convert_user_time < convert_second_time:
                            # get_hash_table().get_value(str(count))[10] = 'In transit'
                            # get_hash_table().get_value(str(count))[9] = 'Left at ' + first_time

                            # Print package's current info
                            print(
                                # f'Package ID: {get_hash_table().get_value(str(count))[0]}, '
                                # f'Delivery status: {get_hash_table().get_value(str(count))[10]}'
                            )

                        # Determine which packages have already been delivered
                        else:
                            # get_hash_table().get_value(str(count))[10] = 'Delivered at ' + second_time
                            # get_hash_table().get_value(str(count))[9] = 'Left at ' + first_time

                            # Print package's current info
                            print(
                                # f'Package ID: {get_hash_table().get_value(str(count))[0]}, '
                                # f'Delivery status: {get_hash_table().get_value(str(count))[10]}'
                            )
            except IndexError:
                print(IndexError)
                exit()
            except ValueError:
                print('Invalid entry!')
                exit()
                
        elif user_input == '2':
            print("WGUPS Current Package Data")
            print("------------------------------------------------------------------------------------------------------------------------")
            print("Package ID | Address | City | State | Zip | Deadline | Weight | Status | Delivery Time | Notes")
            print("------------------------------------------------------------------------------------------------------------------------")

    #         for package in distance.first_truck_list() + distance.second_truck_list() + distance.third_truck_list():
    #             print(" | ".join(str(x) for x in package))
    #         total_packages_delivered = len(distance.first_truck_list()) + len(distance.second_truck_list()) + len(distance.third_truck_list())
    #         # total_packages_not_delivered = len(get_first_delivery()) + len(get_second_delivery()) + len(get_final_delivery()) - total_packages_delivered
    #         print("Total packages delivered: ", total_packages_delivered)
    #   #      print("Total packages not delivered: ", total_packages_not_delivered)
            
            
            distance.display_data_from_time("TRUCK 1", optimized_truck_1, truck_timeline_1, "", td1)
            distance.display_data_from_time("TRUCK 2", optimized_truck_2, truck_timeline_2, "", td2)
            distance.display_data_from_time("TRUCK 3", optimized_truck_3, truck_timeline_3, "", td3)
            print('Total Distance = {} Miles\n'.format(total_distance))
    
        # Case if user selects Option #2
        # Get info for a single package at a particular time -> O(n)
        elif user_input == '3':
            try:
                count = input('Enter a valid package ID: ')
                # first_time = get_hash_table().get_value(str(count))[9]
                # second_time = get_hash_table().get_value(str(count))[10]
                input_time = input('Enter a time (HH:MM): ')
                hrs, mins = input_time.split(':')
                secs = 0  # default seconds to 0
                convert_user_time = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))
                # hrs, mins, secs = first_time.split(':')
                # convert_first_time = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))
                # hrs, mins, secs = second_time.split(':')
                # convert_second_time = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))



                # Determine which packages have left the hub
                if convert_first_time >= convert_user_time:

                    # get_hash_table().get_value(str(count))[10] = 'At Hub'
                    # get_hash_table().get_value(str(count))[9] = 'Leaves at ' + first_time
                    
                    # # Print package's current info
                    print(
                        # f'Package ID: {get_hash_table().get_value(str(count))[0]}\n'
                        # f'Street address: {get_hash_table().get_value(str(count))[2]}\n'
                        # f'Required delivery time: {get_hash_table().get_value(str(count))[6]}\n'
                        # f'Package weight: {get_hash_table().get_value(str(count))[7]}\n'
                        # f'Truck status: {get_hash_table().get_value(str(count))[9]}\n'
                        # f'Delivery status: {get_hash_table().get_value(str(count))[10]}\n'
                    )

                # Determine which packages have left but have not been delivered
                elif convert_first_time <= convert_user_time:
                    if convert_user_time < convert_second_time:
                        # get_hash_table().get_value(str(count))[10] = 'In transit'
                        # get_hash_table().get_value(str(count))[9] = 'Left at ' + first_time

                        # Print package's current info
                        print(
                        #     f'Package ID: {get_hash_table().get_value(str(count))[0]}\n'
                        #     f'Street address: {get_hash_table().get_value(str(count))[2]}\n'
                        #     f'Required delivery time: {get_hash_table().get_value(str(count))[6]}\n'
                        #     f'Package weight: {get_hash_table().get_value(str(count))[7]}\n'
                        #     f'Truck status: {get_hash_table().get_value(str(count))[9]}\n'
                        #     f'Delivery status: {get_hash_table().get_value(str(count))[10]}\n'
                        )

                    # Determine which packages have already been delivered
                    else:
                        # get_hash_table().get_value(str(count))[10] = 'Delivered at ' + second_time
                        # get_hash_table().get_value(str(count))[9] = 'Left at ' + first_time

                        # Print package's current info
                        print(
                            # f'Package ID: {get_hash_table().get_value(str(count))[0]}\n'
                            # f'Street address: {get_hash_table().get_value(str(count))[2]}\n'
                            # f'Required delivery time: {get_hash_table().get_value(str(count))[6]}\n'
                            # f'Package weight: {get_hash_table().get_value(str(count))[7]}\n'
                            # f'Truck status: {get_hash_table().get_value(str(count))[9]}\n'
                            # f'Delivery status: {get_hash_table().get_value(str(count))[10]}\n'
                        )

            except ValueError:
                print('Invalid entry')
                exit()

        # # Case 'exit'
        # # This exits the program
        # elif user_input == 'quit':
        #     exit()

        # Case Error
        # Print Invalid Entry and quit the program
        else:
            print('print("Invalid input, please select an option from the menu or type quit to quit.")')
            ############################################################################################

#             from HashData import HashData
# from Distance import Distance
# from Route import Route
# from TruckSort import TruckSort
# import re

# if __name__ == '__main__':
#     # create objects and load csv data
#     data = HashData()
#     distance = Distance()
#     route = Route(distance)
#     ts = TruckSort()
#     ts.sort_packages_into_priorities(data.packages)
#     # optimize truck routes
#     optimized_truck_1 = route.optimize_route(ts.truck1)
#     optimized_truck_2 = route.optimize_route(ts.truck2)
#     optimized_truck_3 = route.optimize_route(ts.truck3)
#     truck_timeline_1 = distance.check_time(optimized_truck_1, 'truck1')
#     truck_timeline_2 = distance.check_time(optimized_truck_2, 'truck2')
#     truck_timeline_3 = distance.check_time(optimized_truck_3, 'truck3')
#     # calc distance
#     td1 = distance.get_total_distance_traveled(optimized_truck_1)
#     td2 = distance.get_total_distance_traveled(optimized_truck_2)
#     td3 = distance.get_total_distance_traveled(optimized_truck_3)
#     total_distance = td1 + td2 + td3


#     while(True):
#         print("Please Enter a command\n'Report'\n'Lookup'\n'Timestamp\n'Exit'\n")
#         print(total_distance)
#         start = input().lower()
#         print(start)
#         if start == 'exit':
#             exit(0)
#         elif start == 'report':
#             # display
#             distance.display_data_from_time("TRUCK 1", optimized_truck_1, truck_timeline_1, "", td1)
#             distance.display_data_from_time("TRUCK 2", optimized_truck_2, truck_timeline_2, "", td2)
#             distance.display_data_from_time("TRUCK 3", optimized_truck_3, truck_timeline_3, "", td3)
#             print('Total Distance = {} Miles\n'.format(total_distance))
#         elif start == 'lookup':
#             print('Please enter a package ID: \n')
#             ans = int(input())
#             search = ''
#             truck = []
#             truck_time = []
#             for t in optimized_truck_1:
#                 if t.get_package_id() == ans:
#                     p = t
#                     search = ans
#                     truck = optimized_truck_1
#                     truck_time = truck_timeline_1
#             for t in optimized_truck_2:
#                 if t.get_package_id() == ans:
#                     p = t
#                     search = ans
#                     truck = optimized_truck_2
#                     truck_time = truck_timeline_2
#             for t in optimized_truck_3:
#                 if t.get_package_id() == ans:
#                     p = t
#                     search = ans
#                     truck = optimized_truck_3
#                     truck_time = truck_timeline_3
#             if search != '':
#                 ed = distance.check_delivery_time(truck, truck_time, int(search))
#                 print('ID: {} - Address: {} {}, {} - Deadline: {} - Weight: {} - Status: {} - Expected Delivery: {}\n'.format(p.get_package_id(), p.get_address(), p.get_city(), p.get_zip(), p.get_deadline(), p.get_weight(), p.get_delivery_status(), ed))
#             else:
#                 print("Sorry we didnt find a package with that ID number.\n")
#         elif start == 'timestamp':
#             print('Please Enter a timestamp in the format of HH:MM:SS\n')
#             pattern = re.compile("^(?:(?:([01]?\d|2[0-3]):)?([0-5]?\d):)?([0-5]?\d)$")
#             ans = input()
#             if pattern.search(ans):
#                 distance.display_data_from_time("TRUCK 1", optimized_truck_1, truck_timeline_1, ans, td1)
#                 distance.display_data_from_time("TRUCK 2", optimized_truck_2, truck_timeline_2, ans, td2)
#                 distance.display_data_from_time("TRUCK 3", optimized_truck_3, truck_timeline_3, ans, td3)
#             else:
#                 print('Please enter timestamp info correctly matching the correct pattern')
#         else:
#             print('Please enter a valid command.\n')
#             pass
