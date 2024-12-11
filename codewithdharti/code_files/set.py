# add,update,discard,union
#syntax
friends = {"prachi","yesha","dhara","akshita","grishma","kevins"}

#Acess - 1 
def forloop():
    for friend in friends:
        print(friend) 

def checkin():
    if "prachi" in friends:
        print("yes she is there")

forloop()
checkin()

#add - 2

def add_friend():
    friends.add("geeta")
    print(friends)

def update_friends():
    extrafriends = {"kunal","viral"}
    friends.update(extrafriends)
    print(friends)

add_friend()
update_friends()

#remove - 3

friends = {"prachi","yesha","dhara","akshita","grishma","kevins"}
def remove_friend():
    friends.remove("kevins")
    print(friends)

def discard_friend():
    friends.discard("anju")  # do not through exception if its not in set
    print(friends)

def pop_friend():
    friends.pop()
    print(friends)

def clear_friend():
    friends.clear()
    print(friends)

def del_friend():
    del friends
    print(friends)

remove_friend()
pop_friend()
clear_friend()
# del_friend()

#loop - 4 - forloop

#join,intersaction & diffrence - 5

print("operation")
nums = {78,45,8,56,78,12,4,6,23}
friends = {"prachi", "yesha", "dhara", "akshita", "grishma", "kevins"}
extrafriends = {"prachi", "yesha", "dhara", "akshita", "grishma", "kevins", "vishal", "jadi"}


def union():
    unifriends = friends.union(nums)
    print(unifriends)

def multi_union():
    multi_union = friends.union(nums,extrafriends)
    print(multi_union)

def intersact():
    friends = {"Alice", "Bob", "Charlie"}
    extrafriends = {"Bob", "David", "Eve"}
    intersact = friends.intersection(extrafriends)
    print(f"intersact: {intersact}") 
    

def intersact_update():
    friends = {"Alice", "Bob", "Charlie"}
    extrafriends = {"Bob", "David", "Eve"}
    intersact_update = friends.intersection_update(extrafriends)
    # print(intersact_update)
    # print(friends) #store intrasact one only in friends as updated one
    print(f"intersact_update: {intersact_update}")   #None
    print(f"friends: {friends}")  #friends = {"Alice", "Bob", "Charlie"} to friends = {'Bob'}
    

def diff():
    friends = {"Alice", "Bob", "Charlie"}
    extrafriends = {"Bob", "David", "Eve"}
    diff = friends.difference(extrafriends)
    print(f"diff: {diff}")


def diff_update():
    friends = {"Alice", "Bob", "Charlie"}
    extrafriends = {"Bob", "David", "Eve"}
    diff_update = friends.difference_update(extrafriends)
    print(f"diff_update: {diff_update}") #None
    print(f"friends: {friends}")     # friends = {"Alice", "Bob", "Charlie"} to friends = {'Charlie', 'Alice'}
    

def symm_diff():
    friends = {"Alice", "Bob", "Charlie"}
    extrafriends = {"Bob", "David", "Eve"}
    symm_diff = friends.symmetric_difference(extrafriends)
    print(f"symm_diff: {symm_diff}")
    print(f"friends: {friends}")

def symm_diff_update():
    friends = {"Alice", "Bob", "Charlie"}
    extrafriends = {"Bob", "David", "Eve"}
    symm_diff_update = friends.symmetric_difference_update(extrafriends)
    print(f"symm_diff_update: {symm_diff_update}")  #None
    print(f"friends: {friends}") #friends = {"Alice", "Bob", "Charlie"} to friends: {'Eve', 'David', 'Charlie', 'Alice'}

union()
multi_union()
intersact()
intersact_update()
diff()
diff_update()
symm_diff()
symm_diff_update()