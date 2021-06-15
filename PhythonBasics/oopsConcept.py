# classes are user defined blueprint or prototype
# Self keyword is mandatory for calling variables name into method
# instance and class variable have whole different purpose
# constructor name should be __init__
# new keyword is not required when you create object
class Calculator:
    num = 100  # class variable

    # default constructor
    def __init__(self, a, b):
        self.firstNumber = a
        self.secondNumber = b
        print("i am called automatically when object is created")

    def getData(self):
        print("executing as method in class")

    def Summation(self):
        return self.firstNumber + self.secondNumber + self.num


obj = Calculator(2, 3)  # Syntax to create objects in python
obj.getData()
print(obj.Summation())

obj2 = Calculator(4, 5)  # Syntax to create objects in python
obj2.getData()
print(obj2.Summation())
