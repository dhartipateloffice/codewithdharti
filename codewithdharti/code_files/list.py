friends = ["prachi","yesha","dhara","akshita","grishma","kevins"]
nums = [78,45,8,56,78,12,4,6,23]

#basic-1

def duplicate_allow():
    friends = ["prachi","yesha","dhara","prachi"]
    print(friends)

def multiple_datatype():
    friends = ["prachi",True,4.5,"female"]
    print(friends)

def get_len():
    print(len(friends))

def constor_list():
    tuple = ("prachi","yesha","dhara")
    constor_list = list(tuple)
    print(constor_list)

duplicate_allow()
multiple_datatype()
get_len()
constor_list()

#Access-2
print("Acccess")
friends = ["prachi","yesha","dhara","akshita","grishma","kevins"]
def positive_index():
    positive_index = friends[2]
    print(positive_index)

def negative_index():
    negative_index = friends[-2]
    print(negative_index)

def range_positive_index():
    range_positive_index = friends[2:5]
    print(range_positive_index)

def range_negative_index():
    range_negative_index = friends[-5:-2]
    print(range_negative_index)

def start_positive_index():
    end_positive_index = friends[:2]
    print(end_positive_index)

def end_positive_index():
    end_positive_index = friends[2:]
    print(end_positive_index)

def start_negative_index():
    end_negative_index = friends[:-2]
    print(end_negative_index)

def end_negative_index():
    end_negative_index = friends[-2:]
    print(end_negative_index)


#[start:stop:step] - (start index:end index: incrementbetween each index)
print("3 index slicing")

num = [0,1,2,3,4,5,6,7,8,9,10]
def sss_positive_index():
    positive_index = num[1:6:2]
    print(positive_index)

def sss_negative_index():
    negative_index = num[-2:-7:-2]
    print(negative_index)

def sss_range_positive_index():
    range_positive_index = num[2:5:]
    print(range_positive_index)

def sss_range_negative_index():
    range_negative_index = num[-5:None:-1]
    print(range_negative_index)

def sss_start_positive_index():
    end_positive_index = num[::2]
    print(end_positive_index)

def sss_end_positive_index():
    end_positive_index = num[2::]
    print(end_positive_index)

def sss_start_negative_index():
    end_negative_index = num[::-2]
    print(end_negative_index)

def sss_end_negative_index():
    end_negative_index = num[-2::]
    print(end_negative_index)


def checkin():
    if "prachi" in friends:
        print("yes she is there")

def not_checkin():
    if "prachi" not in friends:
        print("no she is")

positive_index()
negative_index()
range_positive_index()
range_negative_index()
start_positive_index()
end_positive_index()
start_negative_index()
end_negative_index()

sss_positive_index()
sss_negative_index()
sss_range_positive_index()
sss_range_negative_index()
sss_start_positive_index()
sss_end_positive_index()
sss_start_negative_index()
sss_end_negative_index()

checkin()
not_checkin()

#add start stop step slicing concept

#change-3

friends = ["prachi","yesha","dhara","akshita","grishma","kevins"]

def change_positive_index():
    friends[5] = "champa"
    print(friends)
def change_negative_index():
    friends[-1] = "kevins"
    print(friends)
def change_range_positive_index():
    friends[3:5] = ("dhruv","aman")
    print(friends)
def change_range_negative_index():
    friends[-3:-5] = ("dhara","akshita")
    print(friends)

change_positive_index()
change_negative_index()
change_range_positive_index()
change_range_negative_index()

#Add-4

friends = ["prachi","yesha","dhara","akshita","grishma","kevins"]
nums = [78,45,8,56,78,12,4,6,23]

def append_friend():
    friends.append("geeta")
    print(friends)

def extend_friend():
    friends.extend(nums)
    print(friends)

def insert_friend():
    friends.insert(2,"ptk")
    print(friends)

append_friend()
extend_friend()
insert_friend()

#Remove-5
friends = ["prachi","yesha","dhara","akshita","grishma","kevins"]

def remove_friend():
    friends.remove("kevins")
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
del_friend()

#loop-6
friends = ["prachi","yesha","dhara","akshita","grishma","kevins"]
def forloop():
    for friend in friends:
        print(friend)
def lenrange():
    for i in range(len(friends)):
        print(friends[i])
def whileloop(): 
    i=0
    while i < len(friends):
        print(friends)
        i+=1   
def short():
    [print(friend)for friend in friends]

forloop()
lenrange()
whileloop()
short()

#list comprehenstion-7 -  create a new list from the values in a list you already have

friends = ["prachi","yesha","dhara","akshita","grishma","kevins"]
nums = [78,45,8,56,78,12,4,6,23]

def forin_comp():
    girls  =[]
    for friend in friends:
        if "p" in friend:
            girls.append(friend)
            print(girls)

def smart_comp():
    girls = [friend for friend in friends if "p" in friend]
    print(girls)

def iter_comp():
    nums = [num for num in range(6)]
    print(nums)

def expression_comp():
    girls = ['prachi' for friend in friends]
    print(girls)

forin_comp()
smart_comp()
iter_comp()
expression_comp()

#sort-8
friends = ["prachi","yesha","dhara","akshita","grishma","kevins"]
nums = [78,45,8,56,78,12,4,6,23]

def alpha_sort():
    friends.sort()
    print(friends)
def num_sort():
    nums.sort()
    print(nums)
def alpha_reverse_sort():
    friends.sort(reverse=True)
    print(friends)
def num_reverse_sort():
    nums.sort(reverse=True)
    print(nums)
# def customize_sort():

alpha_sort()
num_sort()
alpha_reverse_sort()
num_reverse_sort()
# customize_sort()

#copy-9
def create_copy_friends():
    girls = friends.copy()
    print(girls)
def create_list_friends():
    girls = list(friends)
    print(girls)
def create_slice_friends():
    girls = friends[:]
    print(girls)

create_copy_friends()
create_list_friends()
create_slice_friends()

#Join-10

friends = ["prachi","yesha","dhara","akshita","grishma","kevins"]
nums = [78,45,8,56,78,12,4,6,23]

def join_plus():
    joinlist = friends + nums
    print(joinlist)
def join_for():
    for friend in friends:
        nums.append(friend)
    print(nums)
def join_extend():
    friends = ["prachi","yesha","dhara","akshita","grishma","kevins"]
    nums = [78,45,8,56,78,12,4,6,23]
    friends.extend(nums)
    print(friends)

join_plus()
join_for()
join_extend()

