# syntax
# import this from that
#write like - from that import this

from ..play_withbasics import userinput
print(userinput)


x = [1, 2, 3]
y = x
print(x is y)  # Output: True (both variables refer to the same list object)

fruits = ["apple", "banana", "cherry"]
print("apple" in fruits)  # Output: True