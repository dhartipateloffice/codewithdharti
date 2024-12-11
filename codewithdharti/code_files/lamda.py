#  one function which can take as many as arguments
#syntax 
# lambda arguments : expression

# lamda with 1 ,2  3 argument -1

def functionk(n):
    result = lambda a : a * n
    return result

result= functionk(2) #n func parameter
print(result(5)) #a lamda parameter

 
def lamda_one(a):
    result = lambda a: a + 10
    print(result(a))
lamda_one(5)

def lamda_two(a,b):
    result = lambda a,b: a + b
    print(result(a,b))
lamda_two(5,3)

def lamda_three(a,b,c):
    result = lambda a,b,c: a + b + c
    print(result(a,b,c))
lamda_three(5,3,2)

# When Lambda? - 2

def lamda_use_dbl(n):
    return lambda a : a * n

doubleit = lamda_use_dbl(2)
print(doubleit(10))


def lamda_use_tpl(n):
    return lambda a : a * n

tripleit = lamda_use_tpl(3)
print(tripleit(10))

def lamda_use_dbl_tpl(n):
    return lambda a : a * n

doubleit = lamda_use_dbl(2)
tripleit = lamda_use_dbl_tpl(3)
print(doubleit(10))
print(tripleit(11))