my_Dict = {
    "class" : "animal",
    "name" : "giraffe",
    "age" : 10
}

print(my_Dict)
print(my_Dict["name"])
print(my_Dict.get("name"))
print(my_Dict.values())

for x in my_Dict:
    print(x)
for x in my_Dict:
    print(my_Dict[x])

