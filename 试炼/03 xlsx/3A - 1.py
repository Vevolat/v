import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('hotel.csv',encoding='gbk')
# 1
z1 = df.groupby('商圈')['住宿场所名称'].count()
z1 = z1.sort_values(ascending=False).head(5)
print('\n', f'各个商圈的的酒店总数: {z1}')

# 2
z2 = df.groupby('商圈')['房间数'].mean()
z2 = z2.sort_values(ascending=True).head(5)
print('\n', f'各个商圈酒店的平均房间数: {z2}')

#3
sj = df[df['星级'] == '五星级']
z3 = sj['评分'].mean()
print('\n', f'所有五星级酒店的平均评分: {z3:.2f}')

plt.rcParams['font.family'] = 'SimSun'

# 1
plt.figure(figsize=(15,10))
plt.title('各个商圈的酒店总数', fontsize=20)
plt.xlabel('商圈', fontsize=16)
plt.xticks(rotation=90)
plt.ylabel('酒店总数', fontsize=16)
t1 = df.groupby('商圈')['住宿场所名称'].count()
t1.plot(kind='bar')

# 2
plt.figure(figsize=(15,10))
plt.title('各星级酒店平均评分走势', fontsize=20)
plt.xlabel('酒店', fontsize=16)
plt.ylabel('评分', fontsize=16)
plt.xticks(rotation=90)
t2 = df.groupby('住宿场所名称')['评分'].mean().reset_index().head(100)
plt.plot(t2['住宿场所名称'], t2['评分'], marker='.')

plt.show()