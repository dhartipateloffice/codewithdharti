# int - 1       x = 1  
# float - 2     x = 2.8 
# complex - 3   z = 1j 

# gettype - 1

def gettype():
    x = 1    # int
    y = 2.8  # float
    z = 1j   # complex
    print(type(x))
    print(type(y))
    print(type(z))

gettype() 

# get int,float,float_e,complex - 2

def getint():
    x = 1
    y = 35656222554887711
    z = -3255522

    print(type(x))
    print(type(y))
    print(type(z))

def getfloat():
    x = 1.10
    y = 1.0
    z = -35.59

    print(type(x))
    print(type(y))
    print(type(z))

def getfloat_e():  # "e" to indicate the power of 10
    x = 35e3
    y = 12E4
    z = -87.7e100

    print(type(x))
    print(type(y))
    print(type(z))

def getcomplex():  # "e" to indicate the power of 10
    x = 3+5j
    y = 5j
    z = -5j

    print(type(x))
    print(type(y))
    print(type(z))

getint()
getfloat()
getfloat_e()
getcomplex()

# type conversion - 3

def type_conversion():

    x = float(1)
    #float to int
    y = int(2.8)
    #int to complex
    z = complex(1)

    print(x)
    print(y)
    print(z)

    print(type(x))
    print(type(y))
    print(type(z))

type_conversion()

# generate random values - 4

def gen_randomnum_betweenrange():
    import random
    print(random.randrange(1, 10))

gen_randomnum_betweenrange()