# https://docs.python.org/3/library/itertools.html
import itertools

# 全排列，顺序有关
for p in itertools.permutations('ABCD', 3):
    print(p)

print('---')
# 组合，顺序无关
for p in itertools.combinations('ABCD', 3):
    print(p)

print('---')
# 笛卡尔积
for p in itertools.product('ABC', '123'):
    print(p)

print('---')
# 无限循环
for p in itertools.cycle('ABC'):
    print(p)
