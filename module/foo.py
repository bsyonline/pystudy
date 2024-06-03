def foo():
    print('hello, world!')


# 下面的代码在被import的时候就会执行
print("test foo")
foo()

# 下面的代码在被import的时候不会执行
if __name__ == '__main__':
    print("test foo")
    foo()
