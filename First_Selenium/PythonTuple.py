mytuple = ("Apples","Oranges","Grapes")
print(mytuple)
print(mytuple[1])
print(mytuple[-2])
print(mytuple[0:2])
print(mytuple[0:3])


for val in mytuple:
    print(val)

# mytuple[1] = "cherry"

mytuple2 =("Banana",(1,2,3),["Tokyo","New Delhi","London"])
print(mytuple2)
print(mytuple2[2][1])
mytuple2[2][1] = "New York"
print(mytuple2)
print("Banana" in mytuple2)
print("Cherry" in mytuple2)
