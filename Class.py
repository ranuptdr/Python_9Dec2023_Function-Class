# 1 class Defination 

class ThisIsMyClass:

    #1. Property

    #2. Constructor

    #3. Method
    def addMyTwoNumbers(self,fa1,fa2):
        result = fa1+fa2
        print(f"The sum of {fa1} and {fa2} is {result}")

# Class Calling/Invoking
# classObject = ClassName()

# Class instantiation
# creating a class Object
co = ThisIsMyClass()

# classObject.method()
co.addMyTwoNumbers(5,5) # actualarg1=5,actualarg2=5 
co.addMyTwoNumbers(10,5) # actualarg1=10,actualarg2=5 
co.addMyTwoNumbers(20,20) # actualarg1=20,actualarg2=20

