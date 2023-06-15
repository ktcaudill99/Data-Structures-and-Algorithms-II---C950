# HashTable class using chaining.
import csv
import os
from package import Package

class HashTable:
    # Constructor
    def __init__(self):
        path = os.getcwd()
        file_name = "/Package_File.csv"
        self.total_packages = self.get_csv_len(path, file_name)  # Get the total number of packages from the CSV file
        self.packages = []  # Create an empty list to store the packages
        for i in range(self.total_packages):
            self.packages.append([])  # Initialize each index of the list with an empty list for chaining
        self.parse_csv(path, file_name)  # Parse the CSV file and populate the hash map with packages

    # get the hash key
    def get_hash(self, key):
        return key % self.total_packages  # Calculate the hash key based on the total number of packages

    # add package to packages hash map
    def add(self, key, package):
        self.packages[key] = package  # Add the package to the specified index in the hash map

    # delete package from packages hash map
    def delete(self, id):
        key = self.get_hash(id)  # Get the hash key for the package ID
        if id in self.packages[key]:  # Check if the package ID exists in the hash map
            del self.packages[key][id]  # Delete the package from the hash map

    # insert package into hash map
    def insert(self, id, address, city, state, zip, deadline, weight, status):
        delivery = Package(id, address, city, state, zip, deadline, weight, status, '')  # Create a new Package object
        key = self.get_hash(id)  # Get the hash key for the package ID
        self.packages[key] = delivery  # Add the package to the hash map

    # lookup package from hash map
    def lookup(self, id):
        key = self.get_hash(id)  # Get the hash key for the package ID
        return self.packages[key]  # Return the package at the specified index in the hash map

    # Search functions by different fields

    # Lookup package by ID
    def lookup_by_id(self, id):
        for package in self.packages:
            if package.get_package_id() == id:
                return package

    # Lookup packages by address
    def lookup_by_address(self, address):
        result = []
        for package in self.packages:
            if isinstance(package, list):
                for p in package:
                    if p.get_address() == address:
                        result.append(p)
            else:
                if package.get_address() == address:
                    result.append(package)
        return result

    # Lookup packages by city
    def lookup_by_city(self, city):
        result = []
        for package in self.packages:
            if package.get_city().lower() == city.lower():
                result.append(package)
        return result

    # Lookup packages by zip code
    def lookup_by_zip(self, zip):
        result = []
        for package in self.packages:
            if package.get_zip() == zip:
                result.append(package)
        return result

    # Lookup packages by weight
    def lookup_by_weight(self, weight):
        result = []
        for element in self.packages:
            # If the element is a list, iterate over it
            if isinstance(element, list):
                for package in element:
                    if int(package.get_weight()) == weight:
                        result.append(package)
            # If the element is a Package object, check its weight
            elif isinstance(element, Package):
                if int(element.get_weight()) == weight:
                    result.append(element)
        return result if result else "No package with the weight '{}' found.".format(weight)

    # Lookup packages by deadline
    def lookup_by_deadline(self, deadline):
        result = []
        for package in self.packages:
            if package.get_deadline() == deadline:
                result.append(package)
        return result

    # Lookup packages by status
    def lookup_by_status(self, status):
        result = []
        for package_list in self.packages:
            for package in package_list:
                if package.get_delivery_status().lower() == status.lower():
                    result.append(package)
        return result

    # read package data from csv to hash map
    def parse_csv(self, path, file_name):
        with open(path + file_name) as file:
            reader = csv.reader(file, delimiter=',')
            next(reader, None)  # skip headers
            for row in reader:
                delivery = Package(row[0], row[1], row[2], row[3], row[4], row[5], row[6], "AT_HUB", row[7])  # Create a new Package object from the CSV data
                key = self.get_hash(delivery.get_package_id())  # Get the hash key for the package ID
                self.add(key, delivery)  # Add the package to the hash map

    # grab length for hash map size
    def get_csv_len(self, path, file_name):
        with open(path + file_name) as file:
            reader = csv.reader(file, delimiter=',')
            next(reader, None)  # skip headers
            return len(list(reader))  # Return the number of rows in the CSV file
