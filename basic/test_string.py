# 字符串的表示
s1 = 'hello'
s2 = "world"
s3 = """hello, 
world!
"""

# 转义符
s4 = 'hello\nworld'
s5 = r'hello\nworld'
print(s4)
print(s5)

# 字符串的格式化
name = 'Tom'
print('hello, %s' % name)
print('hello, {}'.format(name))
print(f'hello, {name}')

# 字符串的操作
s6 = 'hello' + 'world'
print(s6)

s7 = 'hello' * 3
print(s7)

s8 = 'hello world'
# 从字符串中取出指定位置的字符(下标运算)
print(s8[0])
# 字符串切片(从指定的开始索引到指定的结束索引)
print(s8[0:5])
print(s8[6:])
print(s8[-1])
print(s8[-5:-1])

# 字符串的方法
s9 = 'hello world hello python'
# 指定字符串出现的次数
print(s9.count('hello'))    # 2
# 将字符串以指定的宽度居中并在两侧填充指定的字符
print(s9.center(50, '*'))   # ****************hello world hello python****************
# 将字符串以指定的宽度靠右放置左侧填充指定的字符
print(s9.rjust(50, ' '))    #                                  hello world hello python
# 通过内置函数len计算字符串的长度
print(len(s9))  # 24
# 获得字符串修剪左右两侧空格之后的拷贝
print(s9.strip())   # hello world hello python
# 获得字符串首字母大写的拷贝
print(s9.capitalize())  # Hello world hello python
# 获得字符串变大写后的拷贝
print(s9.upper())   # HELLO WORLD HELLO PYTHON
# 获得字符串变小写后的拷贝
print(s9.lower())   # hello world hello python
# 获得字符串每个单词首字母大写的拷贝
print(s9.title())   # Hello World Hello Python
# 检查字符串是否以指定的字符串开头
print(s9.startswith('hello'))   # True
# 检查字符串是否以指定的字符串结尾
print(s9.endswith('world')) # False
# 从字符串中查找子串所在位置
print(s9.find('world')) # 6
print(s9.find('python'))    # -1
# 与find类似但找不到子串时会引发异常
print(s9.index('world'))    # 6
print(s9.replace('world', 'python'))    # hello python hello python
print(s9.split(' '))
print(s9.split(' ', 1)) # ['hello', 'world hello python']
print(s9.split(' ', 2)) # ['hello', 'world', 'hello python']
print(s9.split(' ', 3)) # ['hello', 'world', 'hello', 'python']
# 检查字符串是否由数字构成
print(s9.isdigit())  # False
# 检查字符串是否以字母构成
print(s9.isalpha())  # False
# 检查字符串是否以数字和字母构成
print(s9.isalnum())  # False
# 检查字符串是否以空格构成
print(s9.isspace())  # False
# 检查字符串是否以标题显示(每个单词首字母大写)
print(s9.istitle())  # False
# 检查字符串是否以大写显示
print(s9.isupper())  # False
# 检查字符串是否以小写显示
print(s9.islower())  # True
# 检查字符串是否以首字母大写显示
print(s9.istitle())  # False
