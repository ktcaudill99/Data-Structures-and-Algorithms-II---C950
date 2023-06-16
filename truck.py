#Katherine Caudill
#Student #: 005252042
#WGU: Data Structures and Algorithms II - C950

# get current location of truck and check distance to next location 
# and time to get there and return time to get there 

from package import Package
class Truck:
    def __init__(self):
        self.truck1 = []
        self.truck2 = []
        self.truck3 = []

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
            id = p.get_package_id()

            if id in [13, 14, 15, 16, 19, 20, 29]:
                priority_truck_1.append(p)
            elif 'Can only be on truck 2' in notes or 'Delayed on flight' in notes:
                priority_truck_2.append(p)
            elif 'Wrong address listed' in notes:
                p.set_address('410 S State St')
                p.set_zip('84111')
                non_priority.append(p)
            elif 'Must be delivered with' in notes and deadline != 'EOD':
                priority_truck_1.append(p)
            elif deadline != 'EOD':
                ft_address = [t.get_address() for t in priority_truck_1]
                if address in ft_address:
                    np_truck_1.append(p)
                else:
                    np_truck_2.append(p)
            else:
                non_priority.append(p)

        self._load_trucks(priority_truck_1, np_truck_1, priority_truck_2, np_truck_2, non_priority)

    def _load_trucks(self, priority_truck_1, np_truck_1, priority_truck_2, np_truck_2, non_priority):
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
            if len(self.truck2) < 16:
                self.truck2.append(t)
            elif len(self.truck1) < 16:
                self.truck1.append(t)
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
