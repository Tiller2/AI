print("Create an account.")
name = input("Name: ")
name_file = open("Social_Network_Assignment_Name.txt", "w")
name_file.writelines(name)
name_file.close()
description = input("Description: ")

people = ["Jack", "Will", "Josh", "Lauren", "Emily", "Sophia"]

friendsList = []

friendRequestsToJack = []
friendRequestsToWill = []
friendRequestsToJosh = []
friendRequestsToLauren = []
friendRequestsToEmily = []
friendRequestsToSophia = []
friendRequestsToMe = []

messagesToMeFromJack = []
messagesToMeFromWill = []
messagesToMeFromJosh = []
messagesToMeFromLauren = []
messagesToMeFromEmily = []
messagesToMeFromSophia = []

messagesToJackFromMe = []
messagesToWillFromMe = []
messagesToJoshFromMe = []
messagesToLaurenFromMe = []
messagesToEmilyFromMe = []
messagesToSophiaFromMe = []

def addFriends():
    print(people)
    friendRequest = input("Enter who to send a friend request to.\n")
    x = open("Social_Network_Assignment_Name.txt", "r")
    y = x.read()
    x.close()
    if friendRequest == "Jack":
        friendRequestsToJack.append(y)
    elif friendRequest == "Will":
        friendRequestsToWill.append(y)
    elif friendRequest == "Josh":
        friendRequestsToJosh.append(y)
    elif friendRequest == "Lauren":
        friendRequestsToLauren.append(y)
    elif friendRequest == "Emily":
        friendRequestsToEmily.append(y)
    elif friendRequest == "Sophia":
        friendRequestsToSophia.append(y)
    else:
        print(friendRequest + " is not a person.")
        addFriends()
    friends()

def acceptFriendRequests():
    acceptFriend = input("Choose who's friend request to accept.\nIf you do not want to accept any of these friend requests, press enter.\n")
    if acceptFriend == "Jack" or acceptFriend == "Will" or acceptFriend == "Josh" or acceptFriend == "Lauren" or acceptFriend == "Emily" or acceptFriend == "Sophia":
        friendRequestsToMe.remove(acceptFriend)
        friendsList.append(acceptFriend)
    elif acceptFriend != "":
        print(acceptFriend + " is not a person.")
        acceptFriendRequests()

def declineFriendRequests():
    declineFriend = input("Choose who's friend request to decline.\nIf you do not want to decline any of these friend requests, press enter.\n")
    if declineFriend == "Jack" or declineFriend == "Will" or declineFriend == "Josh" or declineFriend == "Lauren" or declineFriend == "Emily" or declineFriend == "Sophia":
        friendRequestsToMe.remove(declineFriend)
    elif declineFriend != "":
        print(declineFriend + " is not a person.")
        declineFriendRequests()

def friends():
    friendsAction = input("1. View Friends\n2. Add Friends\n3. View Friend Requests\n4. Go Back\nEnter a number to choose what to do.\n")
    if friendsAction == "1":
        print(friendsList)
        friends()
    elif friendsAction == "2":
        addFriends()
    elif friendsAction == "3":
        print(friendRequestsToMe)
        acceptFriendRequests()
        declineFriendRequests()
        friends()
    elif friendsAction == "4":
        socialNetwork()
    else:
        print("Invalid input, enter again.")
        friends()

def message():
    print(friendsList)
    messageFriend = input("Enter who to message.\n")
    if messageFriend != "Jack" and messageFriend != "Will" and messageFriend != "Josh" and messageFriend != "Lauren" and messageFriend != "Emily" and messageFriend != "Sophia":
        print(messageFriend + " is not a person.")
        message()
    sendMessage = input("Enter message.\n")
    if messageFriend == "Jack":
        print("\nMy Chat With Jack")
        i = 0
        x = len(messagesToMeFromJack)
        while i < x:
            print("Jack:\n" + messagesToMeFromJack[i] + "\n")
            i += 1
        messagesToJackFromMe.append(sendMessage)
        y = len(messagesToJackFromMe)
        while i < y:
            print("Me:\n" + messagesToJackFromMe[i] + "\n")
            i += 1
    elif messageFriend == "Will":
        print("\nMy Chat With Will")
        i = 0
        x = len(messagesToMeFromWill)
        while i < x:
            print("Will:\n" + messagesToMeFromWill[i] + "\n")
            i += 1
        messagesToWillFromMe.append(sendMessage)
        y = len(messagesToWillFromMe)
        while i < y:
            print("Me:\n" + messagesToWillFromMe[i] + "\n")
            i += 1
    elif messageFriend == "Josh":
        print("\nMy Chat With Josh")
        i = 0
        x = len(messagesToMeFromJosh)
        while i < x:
            print("Josh:\n" + messagesToMeFromJosh[i] + "\n")
            i += 1
        messagesToJoshFromMe.append(sendMessage)
        y = len(messagesToJoshFromMe)
        while i < y:
            print("Me:\n" + messagesToJoshFromMe[i] + "\n")
            i += 1
    elif messageFriend == "Lauren":
        print("\nMy Chat With Lauren")
        i = 0
        x = len(messagesToMeFromLauren)
        while i < x:
            print("Lauren:\n" + messagesToMeFromLauren[i] + "\n")
            i += 1
        messagesToLaurenFromMe.append(sendMessage)
        y = len(messagesToLaurenFromMe)
        while i < y:
            print("Me:\n" + messagesToLaurenFromMe[i] + "\n")
            i += 1
    elif messageFriend == "Emily":
        print("\nMy Chat With Emily")
        i = 0
        x = len(messagesToMeFromEmily)
        while i < x:
            print("Emily:\n" + messagesToMeFromEmily[i] + "\n")
            i += 1
        messagesToEmilyFromMe.append(sendMessage)
        y = len(messagesToEmilyFromMe)
        while i < y:
            print("Me:\n" + messagesToEmilyFromMe[i] + "\n")
            i += 1
    elif messageFriend == "Sophia":
        print("\nMy Chat With Sophia")
        i = 0
        x = len(messagesToMeFromSophia)
        while i < x:
            print("Sophia:\n" + messagesToMeFromSophia[i] + "\n")
            i += 1
        messagesToSophiaFromMe.append(sendMessage)
        y = len(messagesToSophiaFromMe)
        while i < y:
            print("Me:\n" + messagesToSophiaFromMe[i] + "\n")
            i += 1
    socialNetwork()

def socialNetwork():
    action = input("1. Edit Profile\n2. Friends\n3. Message\nEnter a number to choose what to do.\n")
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
    else:
        print("Invalid input, enter again.")
        socialNetwork()

socialNetwork()