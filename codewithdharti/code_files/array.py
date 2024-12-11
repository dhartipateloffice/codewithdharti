# syntax - same  datatype supports, arithmetic computations

friends = ["prachi","yesha","dhara","akshita","grishma","kevins"]

#Acess - 1

def access_friend():
    bff = friends[0]
    print(bff)

#len - 2

def get_len():
    lenfriends = len(friends)
    print(lenfriends)

#loop - 3

def forloop():
    for friend in friends:
        print(friend)

#Add - 4

def add_friend():
    friends.append("kunal")
    print(friends)

#Remove - 5

def remove_friend():
    friends.remove("kunal")
    print(friends)

access_friend()
get_len()
forloop()
add_friend()
remove_friend()


#other methods
# copy()
# insert()
# extend()

# count()
# index()


# pop()
# clear()

# reverse()
# sort()