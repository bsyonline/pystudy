f = None
try:
    f = open('test_io.py', 'r', encoding='utf-8')
    # 一次性读取整个文件内容
    print(f.read())
except FileNotFoundError:
    print("file not found")
except LookupError:
    print("unknown encoding")
except UnicodeDecodeError:
    print("decode error")
finally:
    if f:
        f.close()

print("---")

with open('test_io.py', 'r', encoding='utf-8') as f:
    for r in f:
        # 逐行读取
        print(r.rstrip())

print("---")

with open('test_io.py', 'r', encoding='utf-8') as f1:
    for r in f1.readlines():
        print(r.rstrip())

print("---")

with open('test_io.py', 'r', encoding='utf-8') as f:
    line = f.readline()

print(line)

print("---")

# mode: r 只读 w 可写 a 追加
with open("test_io.txt", 'a') as f2:
    f2.write("this first line\n")
    f2.write("this second line\n")
