class User:
    def __init__(self, first_name, last_name, age, gender, nationality):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.nationality = nationality
        self.login_atempts = 0

    def describe_user(self):
        print(f"""Summary of the user:
        Name - {self.first_name.title()} {self.last_name.title()}
        Age - {self.age}
        Gender - {self.gender.title()}
        Nationality - {self.nationality.title()}
        """)
    def greet_user(self):
        print(f"Hello {self.first_name.title()}, how are you? Welcome to the forum!\n")

    def increment_login_atempts(self):
        self.login_atempts += 1
    
    def reset_login_atempts(self):
        self.login_atempts = 0