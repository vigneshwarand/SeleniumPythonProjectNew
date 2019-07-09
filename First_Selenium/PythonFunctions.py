def printHello():
    print("Hello...")

printHello()

def printHi(name):

    print("Hi " +name)

printHi("Vignesh")

def printHi(name="John"):

    print("Hi " +name)

printHi()

def sum(a,b,c):
    print(a+b+c)

sum(10,20,30)

def returnSum(a,b):
    return(a+b)

Test = returnSum(10,20)
print(Test)