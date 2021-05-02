from car import Car
from electric_car import ElectricCar

car1 = Car('Volkswagen', 'beetle', 2019)
print(car1.get_descriptive_name())

car2 = ElectricCar('tesla', 'roadster', 2019)
print(car2.get_descriptive_name())