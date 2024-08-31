# Create a child class Bus that will inherit all of the variables and methods of the Vehicle class

class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Bus(Vehicle):
    pass

bus1=Bus('School Bus', 100,20)
print(f" Bus Type:{bus1.name} \n Bus Speed:{bus1.max_speed} \n Bus Mileage:{bus1.mileage}")