# init function - nitializes a newly created object
# str function - default object will be less informative , by using str function we can print object info as we want
# self - use to access variable that belongs to the class
# pass - if there is nothing to show in class  just use pass

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

#modify object properties - 1
cal_obj.num1 = 10
cal_obj.num2 = 20
result = cal_obj.add()
print(result)

#create new object and try to delete along with properties - 2
num1 = input("Num1 for new object: ")
num2 = input("Num2 for new object: ")
new_cal_obj = Calculator(num1, num2)
del new_cal_obj.num1
del new_cal_obj
try:
    print(new_cal_obj.num1)
except AttributeError:
    print("Object and property have been deleted.")   