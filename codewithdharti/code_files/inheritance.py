class Calculator:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    
    def add(self):
        return self.num1 + self.num2
    
    def multy(self):
        return self.num1 * self.num2
    
class AdvanceCalculator(Calculator):

    def __init__(self, num1, num2,num3):
        super().__init__(num1, num2)
        self.num3 = num3

    def advancemulty(self):
        return self.multy() * self.num3

num1 = int(input("Enter Num1: "))
num2 = int(input("Enter Num2: "))
num3 = int(input("Enter Num3: "))

cal_obj = Calculator(num1,num2)
Acal_obj = AdvanceCalculator(num1,num2,num3)

cal_add_result = cal_obj.add()   
cal_multy_result = cal_obj.multy()
Acal_multy_result =Acal_obj.advancemulty()

print(cal_add_result)
print(cal_multy_result)
print(Acal_multy_result)