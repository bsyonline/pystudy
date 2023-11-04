import pandas as pd

print("\n--普通列表转Series--")
arr = [1, 2, 3, 4, 5]
pd_arr = pd.Series(arr)
print(pd_arr)
print(pd_arr.index)
print(pd_arr.values)

print("\n--转换成二维数组--")
data = {"beijing": 3000, "shanghai": 5000, "guanzhou": 2000, "xian": 1500}
pd_data = pd.Series(data)
print(pd_data)

print("\n--重新指定索引--")
pd_data.index = ['bj', 'sh', 'gz', 'xa']
print(pd_data)

print("\n--")
s = pd.Series(['apple', 'orange', 'banana'], index=[0, 2, 4])
print(s)

print("\n--reindex--")
s1 = s.reindex(range(6))
print(s1)

print("\n--给空值填充默认值--")
s2 = s.reindex(range(6), fill_value="--")
print(s2)

print("\n--用上面的行的值填充--")
s3 = s.reindex(range(6), method='ffill')
print(s3)

print("\n--用下边的行的值填充--")
s4 = s.reindex(range(6), method='bfill')
print(s4)

print("\n--删除缺失的值--")
from numpy import nan as NAN

s5 = pd.Series([1, NAN, 2])
print(s5)
print(s5.dropna())

print("\n--多层索引--")
s6 = pd.Series(NAN,
               index=[['sales', 'sales', 'sales', 'rd', 'rd', 'rd', 'test', 'test', 'test'],
                      ['t1', 't2', 't3', 't1', 't2', 't3', 't1', 't2', 't3']])
print(s6)
print(s6['test'])

print("--转DataFrame--")
print(s6.unstack())

print("--转回来--")
print(s6.unstack().stack())

print("\n--转DataFrame--")
df_data = {"city": ['shanghai', 'beijing', 'guangzhou', 'beijing', 'shanghai'],
           "year": [2016, 2017, 2018, 2016, 2017],
           "pop": [1.5, 1.6, 1.7, 1.8, 1.9]
           }
df = pd.DataFrame(df_data)
print(df)

print("\n--指定列排序--")
df1 = pd.DataFrame(df_data, columns=['year', 'city', 'pop'])
print(df1)

print("\n--取一列的值--")
print(df1['city'])
print(df1.city)

print("\n--增加一列--")
df['min'] = 10
print(df)

print("\n--转置--")
print(df.T)

print("\n--DF删除缺失的值--")
data1 = [[1, 2, 3, NAN], [4, NAN, 6, NAN], [NAN, NAN, NAN, NAN]]
df2 = pd.DataFrame(data1)
print(df2)
print("--有NAN就删--")
print(df2.dropna())
print("--整行NAN就删")
print(df2.dropna(how='all'))
print("--整列NAN就删")
print(df2.dropna(how='all', axis=1))

print("\n--NAN填充值，修改副本--")
print(df2.fillna(-1))

print("\n--NAN填充值，修改本身--")
df2.fillna(-1, inplace=True)
print(df2)
