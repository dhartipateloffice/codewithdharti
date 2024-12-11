# function returns - iterator using the Yield keyword
# like a normal function, but whenever it needs to generate a value, it does so with the yield keyword rather than return
#if the body contains yield keyword it autmatically becomes generetor

def simple_generator():
    yield 1
    yield 2
    yield 3

for value in simple_generator():
    print(value)

def range_generator(start,end):
    current = start
    while current < end:
        yield current
        current+=1

for value in range_generator(1,4):
    print(value)

def fibo_generator(endvalue):
    a,b = 0,1
    while a < endvalue:
        yield a
        a,b = b, a + b
for value in fibo_generator(10):
    print(value)

def infinite_generator():
    a = 0
    while True:
        yield a
        a += 2
for a in infinite_generator():
    if a > 20:
        break
    print(a)

def list_comprehension():
    x = [x * x for x in range(4)]
    print(x)

def expression_generator():
    x = (x * x for x in range(4))
    print(list(x))

list_comprehension()
expression_generator()