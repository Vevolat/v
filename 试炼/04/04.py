import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('shop1.csv',encoding='gbk')

z1 = df.groupby('名称')['销量'].max()
z1 = z1.sort_values(ascending=False).head(10)
print('销量王',z1, '\n')

z2 = df.groupby('名称')['价格'].max()
z2 = z2.sort_values(ascending=True).head(6)
print('实惠王', z2, '\n')

z3 = df.groupby('名称')['浏览量'].max()
z3 = z3.sort_values(ascending=False).head(5)
print('吸引王', z3, '\n')

# 1?
plt.rcParams['font.family'] = ['SimSun']
plt.figure(figsize=(15, 10))
plt.title('产品销售情况', fontsize=20)
plt.xlabel('产品类型', fontsize=16)
plt.ylabel('销售量', fontsize=16)
plt.xticks(rotation=90)
t1 = df.groupby('名称')['销量'].max()
t1.plot(kind='bar', color='g')
for i, y in enumerate(t1):
    plt.text(i,y, f'{y}件', va='bottom', ha='center', fontsize=7)

# 2?
plt.figure(figsize=(15, 10))
plt.title('产品价格情况', fontsize=20)
plt.xlabel('产品类型', fontsize=16)
plt.ylabel('价格', fontsize=16)
plt.xticks(rotation=90)
t1 = df.groupby('名称')['价格'].max()
t1.plot(kind='bar', color='b')
for i, y in enumerate(t1):
    plt.text(i,y, f'{y:.0f}元', va='bottom', ha='center', fontsize=7)

# 3?
plt.figure(figsize=(15, 10))
plt.title('产品浏览情况', fontsize=20)
plt.xlabel('产品类型', fontsize=16)
plt.ylabel('浏览量', fontsize=16)
plt.xticks(rotation=90)
t1 = df.groupby('名称')['浏览量'].max()
t1.plot(kind='bar', color='r')
for i, y in enumerate(t1):
    plt.text(i,y, f'{y:.0f}次', va='bottom', ha='center', fontsize=7)


# 4?
# plt.figure(figsize=(15,10))
# # plt.title('品牌销售统计占比')
# t1.plot(kind='pie')

# 5?
# plt.figure(figsize=(15,10))
# plt.title('品牌销售统计占比')
# t1.plot(kind='hist')

plt.show()