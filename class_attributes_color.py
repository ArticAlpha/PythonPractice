# Define a class attribute”color” with a default value white. I.e., 
# Every Vehicle should be white.
# Use the following code for this exercise.

class Vehicle:
    color="Black"
    def __init__(self, name, max_speed, mileage, color='Yellow'):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.color=color
      
class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

bus_obj1=Bus("school bus",120,20)
print(f"This is a {bus_obj1.name} with color combo of {bus_obj1.color} and {Vehicle.color}")