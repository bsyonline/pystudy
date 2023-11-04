d = {"name": "zhangsan", "age": 20}
print(d)
print(type(d))

print(d["name"])
print(d["age"])

d["gender"]='male'
print(d)

d = {}
d['name'] = "lisi"
d['age'] = 20
print(d)
d['age'] = 21
print(d)

del d['age']
print(d)

d['gender'] = 'female'
d['age'] = 30

for e in d:
    print(e.title() + ":" + str(d[e]))

print("--")

for k in d.keys():
    print(k)

print("--")

for v in d.values():
    print(v)

print("--")

for k,v in d.items():
    print(k.title() + ":" + str(v))

