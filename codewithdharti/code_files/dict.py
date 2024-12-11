#syntax

infodict = {
    "name":"dharti",
    "birth":2002,
    "car":"mercedes",
    "phone":"samsung"
}

#Access-1
def getvalue_fromkey():
    who = infodict["name"]
    print(who)

def getkey():
    infokeys = infodict.keys()
    print(infokeys)

def getvalue():
    infovalues = infodict.values()
    print(infovalues)

def getitem():
    infoitems = infodict.items()
    print(infoitems)

def createitem():
    infodict["job"] = "developer"
    print(infodict)

def checkitem():
    if "car" in infodict:
        print("yes she has")

getvalue_fromkey()
getkey()
getvalue()
getitem()
createitem()
checkitem()

# Change-2
def changeitem():
    infodict["cse"] = "software developer"
    print(infodict)
def updateitem():
    infodict.update({"cse":"developer"})
    print(infodict)

changeitem()
updateitem()

# Add-3
# same as change

# Remove-4

def pop_frominfo():
    infodict.pop("cse")
    print(infodict)

def pop_item():
    infodict.popitem()
    print(infodict)

def clear_item():
    infodict.clear()
    print(infodict)

def del_item():
    infodict = {
    "name":"dharti",
    "birth":2002,
    "car":"mercedes",
    "phone":"samsung"
}

    del infodict
    print(infodict)

pop_frominfo()
pop_item()
clear_item()
# del_item()

# loop-5
infodict = {
    "name":"dharti",
    "birth":2002,
    "car":"mercedes",
    "phone":"samsung"
}

print("****")
def forloopkey():
    for info in infodict:
        print(info)

def forloopvalue():
    for info in infodict:
        print(infodict[info])

def key_items():
    for info in infodict.keys():
        print(info)

def value_items():
    for info in infodict.values():
        print(info)

def item_items():
    for info in infodict.items():
        print(info)
        print("****")

forloopkey()
forloopvalue()
key_items()
value_items()
item_items()

# copy-6
def copydict():
    myself = infodict.copy()
    print(myself)
def makedict():
    myself = dict(infodict)
    print(myself)

copydict()
makedict()

#nested - 7
def nested_dict():
    nest_info_dict = {
        "child1" : {
        "name":"dharti",
        "birth":2002,
        "car":"mercedes",
        "phone":"samsung"
        },
        "child2" : {
        "name":"dharti",
        "birth":2002,
        "car":"mercedes",
        "phone":"samsung"
        }
    }

    print(nest_info_dict)

def particular_item():
    nest_info_dict = {
        "child1" : {
        "name":"dharti",
        "birth":2002,
        "car":"mercedes",
        "phone":"samsung"
        },
        "child2" : {
        "name":"dharti",
        "birth":2002,
        "car":"mercedes",
        "phone":"samsung"
        }
    }

    print(nest_info_dict["child1"]["name"])

def particular_item_asname():
    nest_info_dict = {
        "child1" : {
        "name":"dharti",
        "birth":2002,
        "car":"mercedes",
        "phone":"samsung"
        },
        "child2" : {
        "name":"dharti",
        "birth":2002,
        "car":"mercedes",
        "phone":"samsung"
        }
    }

    for child,dict in nest_info_dict.items():
        for key, value in dict.items():
            print(key + ":" + str(value))

nested_dict()
particular_item()
particular_item_asname()