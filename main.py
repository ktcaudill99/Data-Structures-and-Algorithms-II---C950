import datetime
from hashtable import HashTable
#from Distance import Distance
#from Route import Route
#from truck import TruckSort
from csv_reader import get_hash_table
from package import get_total_distance
import re

# reusable print  functions :> O(1)
def print_status(count):
    print(

        f'Package ID: {get_hash_table().search(str(count))[0]}', """    """
                                                                 f'Truck load time: {get_hash_table().search(str(count))[9]}',
        """    """
        f'Deli1very status: {get_hash_table().search(str(count))[10]}'
    )


# reusable print  functions :> # O(1)
def print_pk_detail(count):
    print(
        '-' * 30, 'package information', '-' * 49, '\n'
                                                   f'Package ID: {get_hash_table().search(str(count))[0]}\n'
                                                   f'Street address: {get_hash_table().search(str(count))[2]}, '
                                                   f'{get_hash_table().search(str(count))[3]}, '
                                                   f'{get_hash_table().search(str(count))[4]}, '
                                                   f'{get_hash_table().search(str(count))[5]},\n'

                                                   f'Delivery deadline : {get_hash_table().search(str(count))[6]}\n'
                                                   f'Package weight: {get_hash_table().search(str(count))[7]} KG\n'
                                                   f'Special note: {get_hash_table().search(str(count))[8]}\n',
        '-' * 30, 'delivery status', '-' * 51,
    )



if __name__ == '__main__':
    # create objects and load csv data
    data = HashTable()
    data.load_csv('packages_data.csv')
    # create distance and route objects
    # distance = Distance()
    # route = Route(distance)
    # ts = TruckSort()
    # ts.sort_packages_into_priorities(data.packages)
    # # optimize truck routes
    # optimized_truck_1 = route.optimize_route(ts.truck1)
    # optimized_truck_2 = route.optimize_route(ts.truck2)
    # optimized_truck_3 = route.optimize_route(ts.truck3)
    # truck_timeline_1 = distance.check_time(optimized_truck_1, 'truck1')
    # truck_timeline_2 = distance.check_time(optimized_truck_2, 'truck2')
    # truck_timeline_3 = distance.check_time(optimized_truck_3, 'truck3')
    # # calc distance
    # td1 = distance.get_total_distance_traveled(optimized_truck_1)
    # td2 = distance.get_total_distance_traveled(optimized_truck_2)
    # td3 = distance.get_total_distance_traveled(optimized_truck_3)
    # total_distance = td1 + td2 + td3

    # # create truck objects
    # truck1 = ts.truck1
    # truck2 = ts.truck2
    # truck3 = ts.truck3

    # # set truck mileage
    # truck1.mileage = td1
    # truck2.mileage = td2
    # truck3.mileage = td3

    # # set truck timeline
    # truck1.timeline = truck_timeline_1
    # truck2.timeline = truck_timeline_2
    # truck3.timeline = truck_timeline_3

    # # set truck distance
    # truck1.distance = td1
    # truck2.distance = td2
    # truck3.distance = td3

    # # set truck packages
    # truck1.packages = optimized_truck_1
    # truck2.packages = optimized_truck_2
    # truck3.packages = optimized_truck_3

    # # set truck total distance
    # truck1.total_distance = td1
    # truck2.total_distance = td2
    # truck3.total_distance = td3

    # # set truck total packages
    # truck1.total_packages = len(optimized_truck_1)
    # truck2.total_packages = len(optimized_truck_2)
    # truck3.total_packages = len(optimized_truck_3)

    # # set truck total time
    # truck1.total_time = truck_timeline_1
    # truck2.total_time = truck_timeline_2
    # truck3.total_time = truck_timeline_3

    # # set truck total mileage
    # truck1.total_mileage = td1
    # truck2.total_mileage = td2
    # truck3.total_mileage = td3

    # # set truck total packages delivered
    # truck1.total_packages_delivered = len(optimized_truck_1)
    # truck2.total_packages_delivered = len(optimized_truck_2)
    # truck3.total_packages_delivered = len(optimized_truck_3)

    # # set truck total packages not delivered
    # truck1.total_packages_not_delivered = 0
    # truck2.total_packages_not_delivered = 0
    # truck3.total_packages_not_delivered = 0

    # User Interface
    # Upon running the program, the below message will appear.
    print("Western Governors University Parcel Service (WGUPS)")
    print("The mileage for the route is:")
   # print(truck1.mileage + truck2.mileage + truck3.mileage)  # Print total mileage for all trucks
   # distance.display_data_from_time("TRUCK 1", optimized_truck_1, truck_timeline_1, "", td1)
   # distance.display_data_from_time("TRUCK 2", optimized_truck_2, truck_timeline_2, "", td2)
   # distance.display_data_from_time("TRUCK 3", optimized_truck_3, truck_timeline_3, "", td3)
   # print('Total Distance = {} Miles\n'.format(total_distance))


    # display today's date and time
    now = datetime.datetime.now()
    cur_time = now.strftime("%H:%M:%S\n")
    cur_date = now.strftime("%Y-%m-%d\n")
    print(""" #Today is          :""", cur_date, """#Current time      :""", cur_time)

    # display package data
    print("WGUPS Package Data")
    print("------------------------------------------------------------------------------------------------------------------------")
    print("Package ID | Address | City | State | Zip | Deadline | Weight | Status | Delivery Time | Notes")
    print("------------------------------------------------------------------------------------------------------------------------")
    for package in data.packages:
        print(package)
    print("------------------------------------------------------------------------------------------------------------------------")
    print("Total Packages Delivered: ", truck1.total_packages_delivered + truck2.total_packages_delivered + truck3.total_packages_delivered)
    print("Total Packages Not Delivered: ", truck1.total_packages_not_delivered + truck2.total_packages_not_delivered + truck3.total_packages_not_delivered)
    print("Total Packages: ", len(data.packages))
    print("Total Distance: ", total_distance)
    print("Total Time: ", truck1.total_time + truck2.total_time + truck3.total_time)
    print("Total Mileage: ", truck1.total_mileage + truck2.total_mileage + truck3.total_mileage)
    print("------------------------------------------------------------------------------------------------------------------------")
    print("WGUPS Truck Data")
    print("------------------------------------------------------------------------------------------------------------------------")
    print("Truck ID | Total Packages | Total Distance | Total Time | Total Mileage")
    print("------------------------------------------------------------------------------------------------------------------------")
    print(truck1)
    print(truck2)
    print(truck3)
    
        # initial user selection : report for  1 packet or all packets
    user_input = int(input("""
    TYPE 1 : To  lookup  ALL  package packages 
    TYPE 2 : To  lookup  an individual package\n  
    TYPE quit : To  quit\n"""))
    if user_input > 2 or user_input < 1:
        print("Invalid entry")
        exit()

    while user_input != 'quit':

        # user input : Timeframe to retrieve report
        input_time_raw = input('Enter a time to retrieve report (HH:MM:SS):\n')
        print('-' * 100)
        (hrs0, mins0, secs0) = input_time_raw.split(':')
        input_time = datetime.timedelta(hours=int(hrs0), minutes=int(mins0), seconds=int(secs0))

        # Case if user selects Option #1
        # Get info for all packages at a particular time :> O(n)
        # ---------------------------------------- CASE 1: ALL PACKET REPORT  -----------------------------------------
        if user_input == 1:
            try:
                for count in range(1, 41):

                    try:
                        # Time variables (T1 : start time, T2: delivery time )
                        t1_temp = get_hash_table().search(str(count))[9]
                        t2_temp = get_hash_table().search(str(count))[10]

                        (hrs1, mins1, secs1) = t1_temp.split(':')
                        (hrs2, mins2, secs2) = t2_temp.split(':')

                        T1 = datetime.timedelta(hours=int(hrs1), minutes=int(mins1), seconds=int(secs1))
                        T2 = datetime.timedelta(hours=int(hrs2), minutes=int(mins2), seconds=int(secs2))

                    except ValueError:
                        pass

                    # Determine which packages have left the hub
                    if T1 >= input_time:
                        get_hash_table().search(str(count))[10] = 'At Hub'
                        get_hash_table().search(str(count))[9] = t1_temp
                        print_status(count)  # Print package's current info


                    # Determine which packages have left but have not been delivered
                    elif T1 <= input_time:
                        if input_time < T2:
                            get_hash_table().search(str(count))[10] = 'In transit'
                            get_hash_table().search(str(count))[9] = t1_temp
                            print_status(count)  # Print package's current info

                        # Determine which packages have already been delivered
                        else:
                            get_hash_table().search(str(count))[10] = 'Delivered at ' + t2_temp
                            get_hash_table().search(str(count))[9] = t1_temp
                            print_status(count)  # Print package's current info
                break


            except IndexError:
                print(IndexError)
                exit()
            except ValueError:
                print('Invalid entry!')
                exit()



        # Case if user selects Option #2
        # Get info for a single package at a particular time -> O(n)
        # ------------------------------ CASE 2 : SINGLE PACKET REPORT ------------------------------------------------
        elif user_input == 2:
            try:
                # Time variables (T1 : start time, T2: delivery time )
                count = input('Enter a valid package ID: \n')
                t1_temp = get_hash_table().search(str(count))[9]
                t2_temp = get_hash_table().search(str(count))[10]

                (hrs, mins, secs) = t1_temp.split(':')
                (hrs, mins, secs) = t2_temp.split(':')

                T1 = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))
                T2 = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))

                print_pk_detail(count)  # prints specified packet's info

                # Determine which packages have left the hub
                if T1 >= input_time:

                    get_hash_table().search(str(count))[10] = 'At Hub'
                    get_hash_table().search(str(count))[9] = t1_temp

                    print_status(count)  # Print package's current delivery status

                # Determine which packages have left but have not been delivered
                elif T1 <= input_time:

                    if input_time < T2:
                        get_hash_table().search(str(count))[10] = 'In transit'
                        get_hash_table().search(str(count))[9] = t1_temp

                        print_status(count)  # Print package's current delivery status

                    # Determine which packages have already been delivered
                    else:
                        get_hash_table().search(str(count))[10] = 'Delivered at ' + t2_temp
                        get_hash_table().search(str(count))[9] = t1_temp

                        print_status(count)  # Print package's current delivery status

            except ValueError:
                print('Invalid entry')
                exit()


        # Case Error
        # Print Invalid Entry and quit the program
        else:
            print('Invalid entry!')
            exit()


