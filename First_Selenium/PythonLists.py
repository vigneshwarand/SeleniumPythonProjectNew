myList = ["Tokyo","London","New York"]
print(myList)
print(myList[2])

myList[2] = "New Delhi"

print(myList)

for val in myList:
    print(val)
print(len(myList))

myList.append("Boston")
print(myList)
myList.insert(3,"Durham")
print(myList)
myList.pop(1)
print(myList)

del myList[1]
print(myList)

fruits = ["apple","oranges","cherry"]
fruits.reverse()
print(fruits)

my_lest = ['apples',2,3.0]
print(my_lest)