#create class - 1 
#create function - 2
# get input - 3
#create object - 4
#call object - 5
#print- 6

class Calculator:
    def __init__(self,num1,num2):
        self.num1 = num1 
        self.num2 = num2 
    def add(self):
        return self.num1 + self.num2

num1 = input("Num1: ")
num2 = input("Num2: ")

cal_obj = Calculator(num1,num2)

result = cal_obj.add()
print(result)

