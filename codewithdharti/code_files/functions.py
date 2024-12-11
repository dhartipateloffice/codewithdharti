# functions - block of code only runs when it get called

# create & call - 1

def function():
    print("this is function")
function()


# parameter or argument?  - info passed to function - 2

def family(member):
    print(member + " " + "Patel")

family("Kevin")  
family("Geeta")  
family("Dinesh")  

# number of Arguments  - function expects 2 arguments, call the function with 2 arguments, not more, and not less. = 3

def familyinfo(name,surname):
    print(name + " " + surname)

familyinfo("Kevin","Patel") 

# don't know how many arugument need to pass to function?

# arbitary arg -  -> * -4
def childs(*kids):
    print("elder one is: " + kids[0])
childs("Dharti","Kevin")

def childs_normal(elder,younger):
    print("elder one is: " + elder)
childs_normal(elder = "Dharti",younger = "Kevin")

# keyword argument -  arguments with the key = value -5
def childs_kv(**kids):
    print("elder one is: " + kids["elder"])
childs_kv(elder = "Dharti",younger = "Kevin")

# default parameter Value - 6

def livein(country = "india"):
    print("ptk is from" + " " + country)

livein("Aus")
livein()
    
# pass list as Argument - 7

def functionlist(friends):
    for friend in friends:
        print(friend)

friends = ["prachi","yesha","dhara"]
functionlist(friends)

# return Value ,pass statement - 8
def function_return(bday):
    return bday
print(function_return(18))
print(function_return(29))
print(function_return(26))

def pass_function():
  pass

# Definition: Positional arguments are arguments that need to be passed in the same order as the function parameters. - order is comp
# Use: Ideal when the order of arguments is obvious and doesn’t lead to confusion.

# Definition: Keyword arguments are passed using the parameter name, allowing you to specify the argument in any order. - any order by specifying name only as key value
# Use: Useful for functions with many parameters or optional parameters, as they improve readability and avoid errors in order.


# positional only -, / -> positional char/num  and then / -9   do not use =
def my_bday_positional(x, /):
  print(x)
my_bday_positional(4)

def my_bday_nonpositional(x):
  print(x)
my_bday_nonpositional(x = 4)

# def my_bday_positional_kv(x, /):
#   print(x)
# my_bday_positional_kv(x = 4)

# keyword only *,  -> -> * and then keyvalue char/num  - 10 use =
def my_bday_keyword_kv(*,x):
  print(x)
my_bday_keyword_kv(x = 4)

def my_bday_nonkeyword(x):
  print(x)
my_bday_nonkeyword(4)

# def my_bday_keyword(*,x):
#   print(x)
# my_bday_keyword(4)

# combine both - 11
def positional_keyword(a, b, /, *, c, d):
  print(a + b + c + d)
positional_keyword(5, 6, c = 7, d = 8)

# recursion - function calls itself - loop through data to reach a result - 12

def recursion(x):
    if (x > 0):
        result = x + recursion(x-1)
        print(result) 
    else:
      result = 0
    return result   
recursion(5)


# recursion(5) calls recursion(4), and waits for its result.
# recursion(4) calls recursion(3), and waits for its result.
# recursion(3) calls recursion(2), and waits for its result.
# recursion(2) calls recursion(1), and waits for its result.
# recursion(1) calls recursion(0), and waits for its result.
# recursion(0) hits the base case (x <= 0), so it returns 0.

# recursion(1) receives 0 from recursion(0), so result = 1 + 0 = 1 and prints 1.
# recursion(2) receives 1 from recursion(1), so result = 2 + 1 = 3 and prints 3.
# recursion(3) receives 3 from recursion(2), so result = 3 + 3 = 6 and prints 6.
# recursion(4) receives 6 from recursion(3), so result = 4 + 6 = 10 and prints 10.
# recursion(5) receives 10 from recursion(4), so result = 5 + 10 = 15 and prints 15.