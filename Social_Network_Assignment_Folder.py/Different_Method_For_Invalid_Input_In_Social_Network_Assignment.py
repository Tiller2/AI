def socialNetwork():
    action = input("1. Edit Profile\n2. Friends\n3. Message\nEnter a number to choose what to do.\n")
    while action != "1" and action != "2" and action != "3":
        print("Invalid input, enter again.")
        action = input("1. Edit Profile\n2. Friends\n3. Message\nEnter a number to choose what to do.\n")
        if action == "1" or action == "2" or action == "3":
            break
    if action == "1":
        editName = input("Name: ")
        name_file = open("Social_Network_Assignment_Name.txt", "w")
        name_file.writelines(editName)
        name_file.close()
        editDescription = input("Description: ")
        socialNetwork()
    elif action == "2":
        friends()
    elif action == "3":
        message()