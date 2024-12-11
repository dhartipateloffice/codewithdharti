# public -methods access everywhere
# private- method access only inside class
# protected - method access inside class + inherited class

class Calculator:
    def __init__(self,num1,num2):
        self.num1 = num1
        # self.num2 = num2

        # declare here private attribute
        self.__num2 = num2  # Private attribute

    def add(self):
        return self.num1 + self.__num2
    
    def multply(self):
        return self.num1 * self.__num2
    
class ACalculator(Calculator):
    def __init__(self, num1, num2,num3):
        super().__init__(num1, num2)
        self.num3 = num3   #using super we will use multply method in inherit class.

    def advancemultply(self):
        return self.num3 * self.multply()

num1 =int(input("Enter num1: "))
num2 =int(input("Enter num2: "))
num3 =int(input("Enter num3: "))

cal_obj = Calculator(num1,num2)
Acal_obj = ACalculator(num1,num2,num3)

cal_add_result = cal_obj.add()  #access to add method of another class
cal_multply_result = cal_obj.multply()
Acal_advancemultply_result =Acal_obj.advancemultply()

print(cal_add_result)
print(cal_multply_result)
print(Acal_advancemultply_result)

#try to print num2 value of Calculator class
print(Calculator.__num2)