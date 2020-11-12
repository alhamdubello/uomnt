#Adding a user class
class User(object):
    """This is a default class for users
    """
    def __init__(self, id, username, first_name, last_name, email, role, comment, shell):
        self.id = id
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.role = role
        self.comment = comment
        self.shell = shell
    
    def print_name(self): #Just adopting print for now
        print(f"ID: {self.id}")
        print(f"Username: {self.username}")
        print(f"Full Name: {self.first_name} {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Role: {self.role}")
        print(f"Comment: {self.comment}")
        print(f"Default User Shell: {self.shell}")

user1 = User(1024, "ab570", "Alhamdu", "Bello", "alhamdubello@gmail.com", "System Admin", "First time developer", "/bin/bash")
print(user1.print_name())