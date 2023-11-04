import json

class User():
    def __init__(self, name, age):
        self.name= name
        self.age = age


user = User("zhangsan", 30)
data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

jsonStr = json.dumps(data)
print(jsonStr)
jsonObj = json.loads(jsonStr)
print(jsonObj)
