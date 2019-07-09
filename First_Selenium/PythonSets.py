mySets = {"Chalk","Duster","Board"}

print(mySets)
for x in mySets:
    print(x)
print("Chalk" in mySets)

mySets.add("Pen")
print(mySets)
mySets.update(["Pencil","Eraser"])
print(mySets)
mySets.remove("Pencil")
print(mySets)
mySets.discard("Pencil")
print(mySets)

mySets.pop()
print(mySets)
mySets.clear()
print(mySets)

myset2 = {"Apples",1,2,3,(3,4,5)}
print(myset2)

my_List = [1,2,3]
print(my_List)
myset3 = set(my_List)
print(myset3)

A = {'A','B',1,2,3}
B = {'B','C',3,4,5}
print(A.union(B))
print(A | B)

print(A.intersection(B))
print(A & B)

print(A.difference(B))
print(A - B)