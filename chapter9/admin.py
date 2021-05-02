import users

class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print("List of Admin privileges: ")
        for p in self.privileges:
            print(p)

class Admin(User):
    def __init__(self, first_name, last_name, age, gender, nationality):
        super().__init__(first_name, last_name, age, gender, nationality)
        self.privileges = Privileges()