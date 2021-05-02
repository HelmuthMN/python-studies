class Restaurant:
    def __init__(self,restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        print(f"""Information of restaurant:
        Name - {self.restaurant_name}
        Cuisine type - {self.cuisine_type}\n""")
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open!!\n")
    def set_number_served(self, set_number):
        self.number_served = set_number
        print(self.number_served)
    def increment_number_served(self, i_customers):
        self.number_served += i_customers
        print(self.number_served)

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["grape", "lemon", "strawberry"]
    
    def display_flavors(self):
        for f in self.flavors:
            print(f)

