# HashTable class using chaining.
class HashTable:

    # Constructor with optional initial capacity parameter.
    # Assigns all buckets with an empty list.
    def __init__(self, init_cap=10):
        # initialize the hash table with empty bucket list entries.
        self.table = []
        for x in range(init_cap):
            self.table.append([])

    # finds  the bucket_list
    def bucket_list(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        return bucket_list


    # Inserts a new item into the hash table.
    def insert(self, key, item):
        key_value = [key, item]
        self.bucket_list(key).append(key_value)
        return True


    # update key if it is already in the bucket
    def update(self, key, item):
        for x in self.bucket_list(key):
            # print (key_value)
            if x[0] == key:
                x[1] = item
                return True


    # Removes an item with matching key from the hash table.
    def remove(self, key):
        for x in self.bucket_list(key):
            # print (key_value)
            if x[0] == key:
                self.bucket_list(key).remove([x[0], x[1]])


    # Searches for an item with matching key in the hash table.
    # Returns the item if found, or None if not found.
    def search(self, key):
        if self.bucket_list(key) is not None:
            for x in self.bucket_list(key):
                # print (key_value)
                if x[0] == key:
                    return x[1]  # value
        return None
    
    
    # in the HashTable class
    def get_all_values(self):
        all_values = []
        for bucket in self.table:
            for key_value in bucket:
                all_values.append(key_value[1])
        return all_values
    
    @property    
    def packages(self):
        return self.get_all_values()
    
    
    def __len__(self):
        #print((self.table))
        for item in self.table:
            print(item)
            print() 
        print(len(self.get_all_values()))
        return len(self.get_all_values())
class HashTableEntry:
     def __init__(self, key, item):
         self.key = key
         self.item = item

        
    
    
    
# class HashMap:
#     def __init__(self, capacity=10):
#         self.map = []
#         for _ in range(capacity):
#             self.map.append([])

#     # Create hash key -> O(1)
#     def create_hash_key(self, key):
#         return int(key) % len(self.map)

#     # Insert package into hash table -> O(n)
#     def insert(self, key, value):
#         key_hash = self.create_hash_key(key)
#         key_value = [key, value]

#         if self.map[key_hash] == None:
#             self.map[key_hash] = list([key_value])
#             return True
#         else:
#             for pair in self.map[key_hash]:
#                 if pair[0] == key:
#                     pair[1] = key_value
#                     return True
#             self.map[key_hash].append(key_value)
#             return True

#     # Update package in hash table -> O(n)
#     def update(self, key, value):
#         key_hash = self.create_hash_key(key)
#         if self.map[key_hash] != None:
#             for pair in self.map[key_hash]:
#                 if pair[0] == key:
#                     pair[1] = value
#                     print(pair[1])
#                     return True
#         else:
#             print('There was an error with updating on key: ' + key)

#     # Get a value from hash table -> O(n)
#     def get_value(self, key):
#         key_hash = self.create_hash_key(key)
#         if self.map[key_hash] != None:
#             for pair in self.map[key_hash]:
#                 if pair[0] == key:
#                     return pair[1]
#         return None

#     # Delete a value from hash table -> O(n)
#     def delete(self, key):
#         key_hash = self.create_hash_key(key)

#         if self.map[key_hash] == None:
#             return False
#         for i in range(0, len(self.map[key_hash])):
#             if self.map[key_hash][i][0] == key:
#                 self.map[key_hash].pop(i)
#                 return True
#         return False

# class HashTableEntry:
#     def __init__(self, key, item):
#         self.key = key
#         self.item = item
