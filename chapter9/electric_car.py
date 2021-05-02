from car import Car

class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-KWh battery.")
    
    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge")

    def upgrade_battery(self):
        if self.battery_size < 100:
            self.battery_size = 100
        else:
            print("The battery is already full!")

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)