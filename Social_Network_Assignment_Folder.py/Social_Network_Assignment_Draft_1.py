friends = []

def addFriend(x):
    friends.append(x)
    print(friends)

def message(y, z):
    print("To " + y + " From Me: " + z)

addFriend("Colin")
addFriend("Will")

message("Colin", "Hello")