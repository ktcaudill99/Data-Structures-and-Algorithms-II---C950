# import csv
# from hashtable import *

# # Read CSV files
# with open('./c950/Package_File.csv') as csvfile:
#     read_csv = list(csv.reader(csvfile, delimiter=','))
    
# #with open('./c950/distance_name_data.csv') as distance_name_file:
# #        self.name_reader = list(csv.reader(distance_name_file, delimiter=','))

#     hashtable = hashtable()  # Create an instance of hashtable class
#     first_delivery = []  # first truck delivery
#     second_delivery = [] # second truck delivery
#     final_delivery = [] # final truck delivery

#     # Insert values from csv file into key/value pairs of the hash table -> O(n)
#     for row in read_csv:
#         id = row[0]
#         address = row[1]
#         city = row[2]
#         state = row[3]
#         zip = row[4]
#         delivery = row[5]
#         size = row[6]
#         note = row[7]
#         delivery_start = ''
#         address_location = ''
#         delivery_status = 'At hub'

#         value = [id, address_location, address, city, state, zip, delivery, size, 
#             note, delivery_start, delivery_status]

#         # Conditional statements to determine which truck a package should be located and 
#         # put these packages into a nested list for quick indexing

#         # Correct incorrect package details
#         if '84104' in value[5] and '10:30' not in value[6]:
#             final_delivery.append(value)

#         # First truck's first delivery
#         if value[6] != 'EOD':
#             if 'Must' in value[8] or 'None' in value[8]:
#                 first_delivery.append(value)

#         # Second truck's delivery
#         if 'Can only be' in value[8] or 'Delayed' in value[8]:
#             second_delivery.append(value)
        
#         # Check remaining packages
#         if value not in first_delivery and value not in second_delivery and value not in final_delivery:
#             second_delivery.append(value) if len(second_delivery) < len(final_delivery) else final_delivery.append(value)

#         # Insert value into the hash table
#         hashtable.insert(id, value)

#     # Get packages on the first delivery -> O(1)
#     def get_first_delivery():
#         return first_delivery

#     # Get packages on the second delivery -> O(1)
#     def get_second_delivery():
#         return second_delivery

#     # Get packages on the final delivery -> O(1)
#     def get_final_delivery():
#         return final_delivery

#     # Get full list of packages -> O(1)
#     def get_hash_table():
#         return hashtable
    
# if __name__=="__main__":
#     print(get_hash_table())
#    # print(get_first_delivery())
import csv
from hashtable import *

hashtable = hashtable()  # Create an instance of hashtable class
first_delivery = []  # first truck delivery
second_delivery = [] # second truck delivery
final_delivery = [] # final truck delivery

    
# Insert values from csv file into key/value pairs of the hash table -> O(n)
# for i in range(hashtable.total_packages):
#     package = hashtable.packages[i]
#     value = [package.get_package_id(), package.get_address_location(), package.get_address(), 
#              package.get_city(), package.get_state(), package.get_zip(), 
#              package.get_deadline(), package.get_weight(), 
#              package.get_notes(), package.get_delivery_status()]
#package.get_delivery_start()
  # Insert values from csv file into key/value pairs of the hash table -> O(n)
with open('c950/packages_data.csv') as csvfile:
    read_csv = csv.reader(csvfile, delimiter=',')
    for row in read_csv:
        p_id = row[0]
        p_addr_street = row[1]
        p_addr_city = row[2]
        p_addr_state = row[3]
        p_addr_zip = row[4]
        p_delivery = row[5]
        p_size = row[6]
        p_sp_note = row[7]
        delivery_start = ''
        addr_loc = ''
        delivery_status = 'At hub'
        value = [p_id, addr_loc, p_addr_street, p_addr_city, p_addr_state, p_addr_zip, p_delivery, p_size, p_sp_note,
                delivery_start, delivery_status]



    # Correct incorrect package details
    if '84104' in value[5] and '10:30' not in value[6]:
        final_delivery.append(value)

    # First truck's first delivery
    if value[6] != 'EOD':
        if 'Must' in value[8] or 'None' in value[8]:
            first_delivery.append(value)

    # Second truck's delivery
    if 'Can only be' in value[8] or 'Delayed' in value[8]:
        second_delivery.append(value)
    
    # Check remaining packages
    if value not in first_delivery and value not in second_delivery and value not in final_delivery:
        second_delivery.append(value) if len(second_delivery) < len(final_delivery) else final_delivery.append(value)

# Get packages on the first delivery -> O(1)
def get_first_delivery():
    return first_delivery

# Get packages on the second delivery -> O(1)
def get_second_delivery():
    return second_delivery

# Get packages on the final delivery -> O(1)
def get_final_delivery():
    return final_delivery

# Get full list of packages -> O(1)
def get_hash_table():
    return hashtable.packages

if __name__=="__main__":
    print(len(get_hash_table()))