# overloading is all about parameter - 1 obj - 1 class - same method
# overriding is all about parent class has thier own identity but child has thier own aqnd show it by override parent identity - 2 obj - inherit class - same method

# travel is fix but depend on parameter that drink or not based on that travel will get call as per the parameter
class MathOperations:   #overload of same methods but do follow particular method using its attribute and properties
    def add(self, a: int, b: int) -> int:
        return a + b

    def add(self, a: float, b: float) -> float:
        return a + b

math = MathOperations()
print(math.add(5, 10))      
print(math.add(5.5, 10.5))  

#one class - same method - parametere diff 
# class - multiple methods 
#               with the same name 
#                       different parameter lists 
#                            It allows the same method to perform different tasks based on the input.

class Animal:
    def sound(self):
        return "Some sound"

class Dog(Animal):
    def sound(self):  #  same method in parent and child but Overriding happends with parent class method 
        return "Bark"

animal = Animal()
dog = Dog()
print(animal.sound())  # Outputs: Some sound
print(dog.sound())     # Outputs: Bark

# Overriding occurs when a child's method  is already in its parent class  - tparent-child class - same method in both class