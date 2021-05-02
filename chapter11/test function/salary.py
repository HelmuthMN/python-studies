class Employee:
    def __init__(self, first_name, last_name, annual_salary = 5000):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary
    
    def give_raise(self, raise_value = 0):
        if raise_value:
            self.annual_salary += raise_value
            message = f"The new salary of {self.first_name} {self.last_name} is {self.annual_salary}"
        else:
            message = f"The new salary of {self.first_name} {self.last_name} is {self.annual_salary}"
        
        return message