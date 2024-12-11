# Boolean Values - 1
def print_directbool():
    print(10 > 9)
    print(10 == 9)
    print(10 < 9)


def getbool_ifelse():
    a = 200
    b = 33
    if b > a:
        print("b is greater than a")
    else:
        print("b is not greater than a")

print_directbool()
getbool_ifelse()

# Evaluate Values and Variables - 2
def print_directbool_string():
    print(bool("Hello"))
    print(bool(15))

def print_directbool_specifystring():
    x = "Hello"
    y = 15
    print(bool(x))
    print(bool(y))

print_directbool_specifystring()

# Most Values are True False - 3
def most_true():
    bool("abc")
    bool(123)
    bool(["apple", "cherry", "banana"])
def most_false():
    bool(False)
    bool(None)
    bool(0)
    bool("")
    bool(())
    bool([])
    bool({})

    # class falseone():
    #     def __len__(self):
    #         return 0
    # obj = falseone()
    # print(bool(obj))
    
    # output - false 

most_true()
most_false()

# Functions can Return a Boolean - 4

def function_direct_printbool():
    return True

print(function_direct_printbool())

def function_ifelse():
  return True
if function_ifelse():
    print("YES!")
else:
    print("NO!")

def function_isinstance(): #isinstance() function,object with certain data type
    x = 200
    print(isinstance(x, int))

function_direct_printbool()
function_ifelse()
function_isinstance()

