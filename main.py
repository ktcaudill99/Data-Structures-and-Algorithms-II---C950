from hashtable import HashTable
from distance import Distance
from route import Route
from truck import Truck
import re
import datetime
from package import Package

# Main class
# This is the main class that runs the program
# It is responsible for creating the hash table, distance, route, and truck objects
# It is also responsible for sorting the packages into their respective trucks
# It is also responsible for optimizing the routes for each truck
# It is also responsible for getting the timelines for each truck
# It is also responsible for calculating the total distance travelled by each truck
# It is also responsible for calculating the total distance travelled by all trucks
# It is also responsible for getting the package status of a given package at a given time
# It is also responsible for displaying the package data
# It is also responsible for displaying the distance travelled by each truck and total distance travelled by all trucks
# It is also responsible for displaying the menu and getting the user input
# It is also responsible for displaying the package data based on the user input


class Main:
    
    now = datetime.datetime.now()
    cur_time = now.strftime("%H:%M:%S")
    cur_date = now.strftime("%Y-%m-%d")
    print("\n#Today is: ", cur_date)
    print("\n#Current time: ", cur_time, "\n")
    
    # Create objects for hash table, distance, route, and truck
    data = HashTable()
    distance = Distance()
    route = Route(distance)
    ts = Truck()
    
    # Sorting the packages into their respective trucks
    ts.sort_packages_into_priorities(data.packages)

    # optimize truck routes
    optimized_truck_1 = route.optimize_route(ts.truck1)
    optimized_truck_2 = route.optimize_route(ts.truck2)
    optimized_truck_3 = route.optimize_route(ts.truck3)
    
    # Getting the timelines for each truck
    truck_timeline_1 = distance.check_time(optimized_truck_1, 'truck1')
    truck_timeline_2 = distance.check_time(optimized_truck_2, 'truck2')
    truck_timeline_3 = distance.check_time(optimized_truck_3, 'truck3')
    
    # Calculate the total distance travelled by each truck
    td1 = distance.get_total_distance_traveled(optimized_truck_1)
    td2 = distance.get_total_distance_traveled(optimized_truck_2)
    td3 = distance.get_total_distance_traveled(optimized_truck_3)
    
    # Calculate the total distance travelled by all trucks
    total_distance = td1 + td2 + td3
    
    # Define the get_package_status function outside of the Main class
    def get_package_status(package, truck1, truck2, truck3, current_time):
        if package.get_package_id() in [p.get_package_id() for p in truck1]:
            truck = truck1
        elif package.get_package_id() in [p.get_package_id() for p in truck2]:
            truck = truck2
        elif package.get_package_id() in [p.get_package_id() for p in truck3]:
            truck = truck3
        else:
            return "Package not found on any truck"
        
        for p in truck:
            if p.get_package_id() == package.get_package_id():
                if p.get_delivery_status() == "DELIVERED":
                    return "DELIVERED"
                elif p.get_delivery_status() == "EN ROUTE":
                    for i in range(len(truck)):
                        if truck[i].get_package_id() == package.get_package_id():
                            if truck[i].get_delivery_status() == "EN ROUTE":
                                if truck[i].get_delivery_time() <= current_time:
                                    return "AT HUB"
                                else:
                                    return "EN ROUTE"
                else:
                    return "AT HUB"

    # display package data
    print("WGUPS Current Truck Data")
 
     # Display distance travelled by each truck and total distance travelled by all trucks
    print("------------------------------------------------------------------------------------------------------------------------")
    print("Truck 1 Distance: ", td1)
    print("Truck 2 Distance: ", td2)
    print("Truck 3 Distance: ", td3)
    print("Total Distance:   ", total_distance)
    print("------------------------------------------------------------------------------------------------------------------------")

    while True:
        
        user_input = input("""
==========================================================================
        Western Governors University Parcel Service (WGUPS)
==========================================================================
    Please select an option below to begin or type 'quit' to quit:
         1. Get info for all packages at a particular time
         2. Get all packages current status
         3. Get info for a single package at a particular time
         4. Get all packages data
         5. Look up package data by ID
         6. Look up package data by address
         7. Look up package data by city
         8. Look up package data by zip code
         9. Look up package data by weight
        10. Look up package data by deadline
    """)
        
        #if user input is quit or q, exit the program
        if  user_input in ['quit', 'q']:
            print('Thank you for using WGUPS!')
            break
        
        # Case if user selects Option #1
        # Get info for all packages at a particular time -> O(n)
        elif user_input == '1':
            # Case if user selects Option #1
            # Get info for all packages at a particular time
            print('Please Enter a timestamp in the format of HH:MM\n')
            pattern = re.compile("^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$")
            ans = input()
            if pattern.search(ans):
                ans += ":00"
                distance.display_data_from_time("TRUCK 1", optimized_truck_1, truck_timeline_1, ans, td1)
                distance.display_data_from_time("TRUCK 2", optimized_truck_2, truck_timeline_2, ans, td2)
                distance.display_data_from_time("TRUCK 3", optimized_truck_3, truck_timeline_3, ans, td3)
            else:
                print('Please enter timestamp info correctly matching the correct pattern')
       
                
        elif user_input == '2':
            distance.display_data_from_time("TRUCK 1", optimized_truck_1, truck_timeline_1, "", td1)
            distance.display_data_from_time("TRUCK 2", optimized_truck_2, truck_timeline_2, "", td2)
            distance.display_data_from_time("TRUCK 3", optimized_truck_3, truck_timeline_3, "", td3)

            print('\n====================================================================================================')
            print('Total Distance = {} Miles\n'.format(total_distance))
        
        elif user_input == '3':
            print('Please enter a package ID: ')
            pattern = re.compile("^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$")  # Regular expression to validate the time format
            ans = int(input().strip())   # Read the package ID as an integer
            print('\nPlease enter a specific time in HH:MM format: ')
            specific_time = input().strip()
            if pattern.search(specific_time): # Check if the specific time matches the expected format
                    specific_time += ":00"  # Convert the specific time to HH:MM:SS format
                    search = ''
                    print()
                    truck = []
                    truck_time = []
                    truck_name = ''  # initialise the variable here

                    # Search for the package ID in each truck's packages
                    for t in optimized_truck_1:
                        if t.get_package_id() == ans:
                            p = t # Found the package in truck 1
                            search = ans
                            truck = optimized_truck_1
                            truck_time = truck_timeline_1
                            truck_name = 'TRUCK 1'  # set the truck_name here
                    for t in optimized_truck_2:
                        if t.get_package_id() == ans:
                            p = t # Found the package in truck 2
                            search = ans
                            truck = optimized_truck_2
                            truck_time = truck_timeline_2
                            truck_name = 'TRUCK 2'  # set the truck_name here
                    for t in optimized_truck_3:
                        if t.get_package_id() == ans:
                            p = t # Found the package in truck 3
                            search = ans
                            truck = optimized_truck_3
                            truck_time = truck_timeline_3
                            truck_name = 'TRUCK 3'  # set the truck_name here

                    if search != '':
                        ed = distance.check_delivery_time(truck, truck_time, int(search))
                        delivery_status = distance.check_delivery_status(specific_time, truck, truck_time, truck_name, int(search))
                        print('ID: {} - Address: {} {}, {} - Deadline: {} - Weight: {} - Status: {} - Expected Delivery: {}\n'.format(p.get_package_id(), p.get_address(), p.get_city(), p.get_zip(), p.get_deadline(), p.get_weight(), delivery_status, ed))
                    else:
                        print("Please neter in correct format.\n")
            else:
                print("Sorry we didnt find a package with that ID number.\n")

        elif user_input == '4':
        # Get all packages data
            print('============================================================================================================================================================================ \n')
            print('All Package Data')
            print('----------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
            print('{:<4s}{:<40s}{:<18s}{:<7s}{:<10s}{:<10s}{:<8s}{:<8s}{:<20s}'.format('ID', 'Address', 'City', 'State', 'Zip', 'Deadline', 'Weight', 'Status', 'Notes'))
            print('----------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
            
            # Iterate over all packages and display their information
            for p in data.packages:
                current_status = get_package_status(p, optimized_truck_1, optimized_truck_2, optimized_truck_3, cur_time) # Get the current status of the package
                print('{:<4s}{:<40s}{:<18s}{:<7s}{:<10s}{:<10s}{:<8s}{:<8s}{:<20s}'.format(
                    str(p.package_id), 
                    p.address, 
                    p.city, 
                    p.state,
                    p.zip,
                    p.deadline, 
                    str(p.weight), 
                    current_status,
                    p.notes if p.notes else ''
                ))
            
            print('============================================================================================================================================================================ \n')

        elif user_input == '5':
            # Look up package data by ID
            while True:
                try:
                    package_id = int(input("Please enter a package ID: ")) # Prompt the user to enter a package ID
                    break
                except ValueError:
                    print("Invalid input. Please enter a number for the package ID.")

            package = data.lookup_by_id(package_id) # Look up the package by ID
            if package:
                print('----------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
                print('{:<4s}{:<40s}{:<18s}{:<7s}{:<10s}{:<10s}{:<8s}{:<8s}{:<20s}'.format('ID', 'Address', 'City', 'State', 'Zip', 'Deadline', 'Weight', 'Status', 'Notes'))
                print('----------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
                print('{:<4s}{:<40s}{:<18s}{:<7s}{:<10s}{:<10s}{:<8s}{:<8s}{:<20s}'.format(
                    str(package.package_id), 
                    package.address, 
                    package.city, 
                    package.state,
                    package.zip,
                    package.deadline, 
                    str(package.weight), 
                    package.delivery_status,
                    package.notes if package.notes else ''
                ))
                print('============================================================================================================================================================================')
            else:
                print("Package not found.")


        elif user_input == '6':
            # Look up package data by address
            address = input("Please enter an address: ")  # Prompt the user to enter an address
            packages = data.lookup_by_address(address) # Look up the packages by address
            if packages:
                for package in packages:
                    print(package.__dict__) # Print the package information
            else:
                print("Package not found.")

        elif user_input == '7':
            # Look up package data by city
            city = input("Please enter a city: ")  # Prompt the user to enter a city
            packages = data.lookup_by_city(city) # Look up the packages by city
            if packages:
                print('============================================================================================================================================================================ \n')
                print('All Packages in {}:'.format(city))
                print('----------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
                print('{:<4s}{:<40s}{:<18s}{:<7s}{:<10s}{:<10s}{:<8s}{:<8s}{:<20s}'.format(
                    'ID', 'Address', 'City', 'State', 'Zip', 'Deadline', 'Weight', 'Status', 'Notes'
                ))
                print('----------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
                for package in packages:
                    print('{:<4s}{:<40s}{:<18s}{:<7s}{:<10s}{:<10s}{:<8s}{:<8s}{:<20s}'.format(
                        str(package.package_id), 
                        package.address, 
                        package.city, 
                        package.state,
                        package.zip,
                        package.deadline, 
                        str(package.weight), 
                        package.delivery_status,
                        package.notes if package.notes else ''
                    ))
                print('============================================================================================================================================================================')
            else:
                print("No packages found in {}.".format(city))


        elif user_input == '8':
        # Look up package data by zip code
            zip_code = input("Please enter a zip code: ")  # Prompt the user to enter a zip code
            packages = data.lookup_by_zip(zip_code) # Look up the packages by zip code
            if packages:
                print('============================================================================================================================================================================ \n')
                print('All Packages in Zip Code {}:'.format(zip_code))
                print('----------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
                print('{:<4s}{:<40s}{:<18s}{:<7s}{:<10s}{:<10s}{:<8s}{:<8s}{:<20s}'.format(
                    'ID', 'Address', 'City', 'State', 'Zip', 'Deadline', 'Weight', 'Status', 'Notes'
                ))
                print('----------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
                for package in packages:
                    print('{:<4s}{:<40s}{:<18s}{:<7s}{:<10s}{:<10s}{:<8s}{:<8s}{:<20s}'.format(
                        str(package.package_id), 
                        package.address, 
                        package.city, 
                        package.state,
                        package.zip,
                        package.deadline, 
                        str(package.weight), 
                        package.delivery_status,
                        package.notes if package.notes else ''
                    ))
                print('============================================================================================================================================================================')
            else:
                print("No packages found in Zip Code {}.".format(zip_code))


        elif user_input == '9':
             # Look up package data by weight
            while True:
                try:
                    weight = int(input("Please enter a weight (e.g., '10'): ")) # Prompt the user to enter a weight
                    break
                except ValueError:
                    print("Invalid input. Please enter a number for the weight.")
            
            packages = data.lookup_by_weight(weight) # Look up the packages by weight
            if isinstance(packages, list):  # Check if 'packages' is a list
                print('============================================================================================================================================================================ \n')
                print('All Packages with Weight {}:'.format(weight))
                print('----------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
                print('{:<4s}{:<40s}{:<18s}{:<7s}{:<10s}{:<10s}{:<8s}{:<8s}{:<20s}'.format(
                    'ID', 'Address', 'City', 'State', 'Zip', 'Deadline', 'Weight', 'Status', 'Notes'
                ))
                print('----------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
                for package in packages:
                    print('{:<4s}{:<40s}{:<18s}{:<7s}{:<10s}{:<10s}{:<8s}{:<8s}{:<20s}'.format(
                        str(package.package_id), 
                        package.address, 
                        package.city, 
                        package.state,
                        package.zip,
                        package.deadline, 
                        str(package.weight), 
                        package.delivery_status,
                        package.notes if package.notes else ''
                    ))
                print('============================================================================================================================================================================')
            else:
                print(packages)  # 'packages' is a string indicating no package was found with the given weight



        elif user_input == '10':
            # Look up package data by deadline
            deadline = input("Please enter a deadline (e.g., '9:00', '10:30' or 'EOD'): ") # Prompt the user to enter a deadline
            packages = data.lookup_by_deadline(deadline) # Look up the packages by deadline
            if packages:
                print('============================================================================================================================================================================ \n')
                print('All Packages with Deadline {}:'.format(deadline))
                print('----------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
                print('{:<4s}{:<40s}{:<18s}{:<7s}{:<10s}{:<10s}{:<8s}{:<8s}{:<20s}'.format(
                    'ID', 'Address', 'City', 'State', 'Zip', 'Deadline', 'Weight', 'Status', 'Notes'
                ))
                print('----------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
                for package in packages:
                    print('{:<4s}{:<40s}{:<18s}{:<7s}{:<10s}{:<10s}{:<8s}{:<8s}{:<20s}'.format(
                        str(package.package_id), 
                        package.address, 
                        package.city, 
                        package.state,
                        package.zip,
                        package.deadline, 
                        str(package.weight), 
                        package.delivery_status,
                        package.notes if package.notes else ''
                    ))
                print('============================================================================================================================================================================')
            else:
                print("No packages found with Deadline {}.".format(deadline))



        else:
            print("Invalid input, please select an option from the menu or type quit to quit.")
            pass