class GreetMixin:
    def greet(self):
        self.name = "No name"
        print("Hello...Welcome")

class User(GreetMixin):
    def __init__(self,name):
        self.name = name

    def username(self):
        self.greet()
        print(self.name)

class Guest(GreetMixin):
    def username(self):
        self.greet()
        print(self.name)

user = User("man")
user.username()

guest = Guest()
guest.username()