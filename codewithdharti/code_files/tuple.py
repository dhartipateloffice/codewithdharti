# syntax - tuple with one element
friends_tuple = ("prachi",)
print(friends_tuple)

#Acess - 1 = same as list

#add - 2
def append_friend():
    friends = ("prachi","yesha","dhara","akshita","grishma","kevins")
    friends_list = list(friends)
    friends_list.append("kevins")
    friends = tuple(friends_list)
    print(friends)

append_friend()

#remove - 3
def remove_friend():
    friends = ("prachi","yesha","dhara","akshita","grishma","kevins")
    friends_list = list(friends)
    friends_list.remove("kevins")
    friends = tuple(friends_list)
    print(friends)

def del_friend():
    friends = ("prachi","yesha","dhara","akshita","grishma","kevins")
    del friends
    print(friends)

remove_friend()
# del_friend()

#unpack - 4
friends = ("prachi","yesha","dhara","akshita","grishma","kevins")

def unpack_throughcomma():
    f1, f2, f3, f4, f5, f6 = friends
    print(f2)
def unpack_throughasterisk():
    f1, f2, f3, *remain_friends = friends
    print(remain_friends)

unpack_throughcomma()
unpack_throughasterisk()

#loop - 5 same as list

#join - 6
def join_plus():
    friends = ("prachi","yesha","dhara","akshita","grishma","kevins")
    nums = (78,45,8,56,78,12,4,6,23)
    jointuple = friends + nums
    print(jointuple)

def join_plusequal():
    friends = ("prachi","yesha","dhara","akshita","grishma","kevins")
    nums = (78,45,8,56,78,12,4,6,23)
    friends += nums
    print(friends)

def join_multi():
    friends = ("prachi","yesha","dhara","akshita","grishma","kevins")
    jointuple = friends * 2
    print(jointuple)

join_plus()
join_plusequal()
join_multi()