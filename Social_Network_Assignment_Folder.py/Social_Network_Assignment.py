print("Create an account.")
name = input("Name: ")
name_file = open("Social_Network_Assignment_Name.txt", "w")
name_file.writelines(name)
name_file.close()
description = input("Description: ")

friends = []

people = ["Jack", "Will", "Josh", "Lauren", "Emily", "Sophia"]

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

def acceptFriendRequest(x):
    friendRequestsToMe.remove(x)
    friends.append(x)

def declineFriendRequest(x):
    friendRequestsToMe.remove(x)

def friends():
    friendsAction = input("1. View Friends\n2. Add Friends\n3. View Friend Requests\n")
    if friendsAction == "1":
        print(friends)
        friends()
    elif friendsAction == "2":
        print(people)
        friendRequest = input("Enter who to send a friend request to.\n")
        x = open("Social_Network_Assignment_Name.txt", "r")
        y = x.read()
        x.close()
        if friendRequest == "Jack":
            friendRequestsToJack.append(y)
            #addFriendsGoBack()
        elif friendRequest == "Will":
            friendRequestsToWill.append(y)
            #addFriendsGoBack()
        elif friendRequest == "Josh":
            friendRequestsToJosh.append(y)
            #addFriendsGoBack()
        elif friendRequest == "Lauren":
            friendRequestsToLauren.append(y)
            #addFriendsGoBack()
        elif friendRequest == "Emily":
            friendRequestsToEmily.append(y)
            #addFriendsGoBack()
        elif friendRequest == "Sophia":
            friendRequestsToSophia.append(y)
            #addFriendsGoBack()
        else:
            invalidInput = input("Invalid input, enter again.\n")
            #addFriendsGoBack()
        friends()
    elif friendsAction == "3":
        print(friendRequestsToMe)
        acceptFriend = input("Choose who's friend request to accept.\n")
        acceptFriendRequest(acceptFriend)
        declineFriend = input("Choose who's friend request to decline.\n")
        declineFriendRequest(declineFriend)
        friends()
    else:
        invalidInput = input("Invalid input, enter again.\n")
        friends()
    socialNetworkActions()

def socialNetworkActions():
    action = input("1. Edit Profile\n2. Friends\n3. Message\nEnter a number to choose what to do.\n")
    if action == "1":
        editName = input("Name: ")
        name_file = open("Social_Network_Assignment_Name.txt", "w")
        name_file.writelines(editName)
        name_file.close()
        editDescription = input("Description: ")
        socialNetworkActions()
    elif action == "2":
        friends()
    elif action == "3":
        print(friends)
        messageFriend = input("Enter who to message.\n")
        message = input("Enter message.\n")
        if messageFriend == "Jack":
            print("\nMy Chat With Jack")
            i = 0
            x = len(messagesToMeFromJack)
            while i < x:
                print("\nJack:\n" + messagesToMeFromJack[i] + "\n")
                i += 1
            messagesToJackFromMe.append(message)
            y = len(messagesToJackFromMe)
            while i < y:
                print("\nMe:\n" + messagesToJackFromMe[i] + "\n")
                i += 1
            #messageGoBack()
        elif messageFriend == "Will":
            print("\nMy Chat With Will")
            i = 0
            x = len(messagesToMeFromWill)
            while i < x:
                print("\nWill:\n" + messagesToMeFromWill[i] + "\n")
                i += 1
            messagesToWillFromMe.append(message)
            y = len(messagesToWillFromMe)
            while i < y:
                print("\nMe:\n" + messagesToWillFromMe[i] + "\n")
                i += 1
            #messageGoBack()
        elif messageFriend == "Josh":
            print("\nMy Chat With Josh")
            i = 0
            x = len(messagesToMeFromJosh)
            while i < x:
                print("\nJosh:\n" + messagesToMeFromJosh[i] + "\n")
                i += 1
            messagesToJoshFromMe.append(message)
            y = len(messagesToJoshFromMe)
            while i < y:
                print("\nMe:\n" + messagesToJoshFromMe[i] + "\n")
                i += 1
            #messageGoBack()
        elif messageFriend == "Lauren":
            print("\nMy Chat With Lauren")
            i = 0
            x = len(messagesToMeFromLauren)
            while i < x:
                print("\nLauren:\n" + messagesToMeFromLauren[i] + "\n")
                i += 1
            messagesToLaurenFromMe.append(message)
            y = len(messagesToLaurenFromMe)
            while i < y:
                print("\nMe:\n" + messagesToLaurenFromMe[i] + "\n")
                i += 1
            #messageGoBack()
        elif messageFriend == "Emily":
            print("\nMy Chat With Emily")
            i = 0
            x = len(messagesToMeFromEmily)
            while i < x:
                print("\nEmily:\n" + messagesToMeFromEmily[i] + "\n")
                i += 1
            messagesToEmilyFromMe.append(message)
            y = len(messagesToEmilyFromMe)
            while i < y:
                print("\nMe:\n" + messagesToEmilyFromMe[i] + "\n")
                i += 1
            #messageGoBack()
        elif messageFriend == "Sophia":
            print("\nMy Chat With Sophia")
            i = 0
            x = len(messagesToMeFromSophia)
            while i < x:
                print("\nSophia:\n" + messagesToMeFromSophia[i] + "\n")
                i += 1
            messagesToSophiaFromMe.append(message)
            y = len(messagesToSophiaFromMe)
            while i < y:
                print("\nMe:\n" + messagesToSophiaFromMe[i] + "\n")
                i += 1
            #messageGoBack()
        else:
            invalidInput = input("Invalid input, enter again.\n")
            #messageGoBack()
        socialNetworkActions()
    else:
        invalidInput = input("Invalid input, enter again.\n")
        socialNetworkActions()

socialNetworkActions()