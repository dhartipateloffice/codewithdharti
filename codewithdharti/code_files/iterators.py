# object that any user can iterate over - Iterable
# helps to interate - Iterator 

# Iteration through loop - 1
# 1.tuple 
# 2.string

def loop_tuple():
    friends = ("prachi", "yesha", "dhara")
    for friend in friends:
        print(friend)
    

def loop_string():
    info = "dharti"
    for char in info:
        print(char)

loop_tuple()
loop_string()

# Iteration through iter & next -2
# 1.tuple 
# 2.string

def iter_tuple():
    friends = ("prachi", "yesha", "dhara")
    friend = iter(friends)

    print(next(friend))
    print(next(friend))
    print(next(friend))

def iter_string():
    info = "dharti"
    char = iter(info)

    print(next(char))
    print(next(char))
    print(next(char))
    print(next(char))
    print(next(char))
    print(next(char))

iter_tuple()
iter_string()

# Create Iterator - 3

class NumberIterator:
    def __iter__(self):
        self.x = 1
        return self
        
    def __next__(self):
        valuex = self.x
        self.x += 1
        return valuex

NumberIterator_obj = NumberIterator()
NumberIterator_result = iter(NumberIterator_obj)  #iter in build method on object

print(next(NumberIterator_result))
print(next(NumberIterator_result))
print(next(NumberIterator_result))
print(next(NumberIterator_result))
print(next(NumberIterator_result))

# Stop Iteration - 4
class NumberIterator:
    def __iter__(self):
        self.x = 1
        return self
        
    def __next__(self):
        valuex = self.x
        if valuex < 10 :
            self.x += 1
            return valuex
        else:
            raise StopIteration    
        

NumberIterator_obj = NumberIterator()
NumberIterator_result = iter(NumberIterator_obj)

for x in NumberIterator_result:
    print(x)