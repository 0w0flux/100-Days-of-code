class User:
    def __init__(self, id, username):
        print("New user being created...") # Prints every time an object form this class is created
        self.id = id
        self.username = username
        self.followers = 0 # Set default value so you dont have to accept it as an attribute
        self.following = 0

    def follow(self, user): # Even methods have to have the self attribute
        user.followers += 1
        self.following += 1

user_1 = User("001", "Owe")
user_2 = User("002", "Jonathan")

user_1.follow(user_2)
print(user_1.followers)
print(user_2.followers)

print(user_1.following)
print(user_2.following)