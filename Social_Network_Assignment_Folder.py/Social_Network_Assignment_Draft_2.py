action = input("1. Edit Profile\n2. Friends\n3. Message\nEnter a number to choose what to do.\n")

people = ["Jack", "Will", "Josh", "Lauren", "Emily", "Sophia"]

friends = []

if action == "1":
    name = input("Name: ")
    description = input("Description: ")
elif action == "2":
    print(people)
    friendRequest = input("Send friend request to: ")
elif action == "3":
    chooseFriend = input(print(friends) + "\nEnter who to message.")
else:
    invalidInput = input("Invalid input, enter again.")