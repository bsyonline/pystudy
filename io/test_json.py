import json


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


user = User("zhangsan", 30)
data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# 序列化到字符串
jsonStr = json.dumps(data)
print(jsonStr)

with open("data.json", "w") as f:
    # 序列化到文件
    json.dump(data, f)

# 将字符串反序列化
jsonObj = json.loads(jsonStr)
print(jsonObj)

with open("data.json", "r") as f:
    # 从文件反序列化
    s = json.load(f)
    print(s)
