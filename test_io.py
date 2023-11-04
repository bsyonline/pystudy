with open('test_io.py') as f:
    for r in f:
        print(r.rstrip())

with open('test_io.py') as f1:
    for r in f1.readlines():
        print(r.rstrip())

# mode: r 只读 w 可写 a 追加
with open("test_io.txt", 'a') as f2:
    f2.write("this first line\n")
    f2.write("this second line\n")

# -----------
