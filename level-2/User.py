class user():

    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        name = self.first_name +' '+self.last_name
        print(name.tital())

    def greet_user(self):
        print("Hello")