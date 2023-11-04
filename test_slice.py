list = [1, 2, 3, 4, 5, 6]

print(list[0:3])
print(list[:3])
print(list[2:])
print(list[2:5])
print(list[-3:])
print(list[:])

for e in list[2:]:
    print(e)

list1 = list[:]
print(list1)