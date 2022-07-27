#Experimenting if x can be used as a translator for a list of people who sent someone a friend request:
#elif action == "2":
#    friendsAction = input("1. View Friends\n2. Add Friends\n3. View Friend Requests\n")
#    if friendsAction == "1":
#        print(friends)
#        friendsGoBack()
#    elif friendsAction == "2":
#        print(people)
#        friendRequest = input("Send friend request to: ")

#        Does Not Work: Variables cannot be used as a translator for a list name.
#        x = "friendRequestsTo" + friendRequest
#        x = []
#        x.append("name")
#        print(x)
#        print(friendRequestsToJack)

#        Does Not Work: Variables cannot be used as a translator for a list name.
#        x = "friendRequestsTo" + friendRequest
#        print(x)
#        x.append("name")
#        print("friendRequestsTo" + friendRequest)

#        friendsGoBack()
#    elif friendsAction == "3":
#        print(friendRequests)
#        friendsGoBack()
#    else:
#        invalidInput = input("Invalid input, enter again.")
#    goBack()

#Experimenting if you can count how many elements of a certain name are in the friends list:
#friends = []

#Does Not Work: You cannot count how many elements of a specific value are in a list.
#def notInFriendsList():
#    x = friends.count(messageFriend)
#    if x == 0:
#        print(messageFriend + " is not in your friends list.")
#        messageFriend = input("Enter who to message.\n")
#        notInFriendsList()

#elif action == "3":
#    print(friends)
#    messageFriend = input("Enter who to message.\n")
#    notInFriendsList()