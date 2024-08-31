# Create a Bus class that inherits from the Vehicle class. 
# Give the capacity argument of Bus.seating_capacity() a default value of 50.

class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers with top speed of {self.max_speed}"
    

class Bus(Vehicle):
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity)


class Car(Vehicle):

    def seating_capacity(self, capacity=5):
        return super().seating_capacity(capacity)  

bus_obj1=Bus("School Bus",120,18)
print(bus_obj1.seating_capacity(60))


car_obj1=Bus("Honda City modified",200,16)
print(car_obj1.seating_capacity(4))
