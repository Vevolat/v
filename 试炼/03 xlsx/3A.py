import matplotlib.pyplot as plt
import pandas as pd

# 读取 CSV 文件
df = pd.read_csv('hotel.csv', encoding='gbk')
plt.rcParams['font.family'] = 'SimSun'

# 统计各个商圈的酒店总数
ht = df['商圈'].value_counts()
top_5_ht = ht.sort_values(ascending=False).head(5)

# 按商圈分组并计算平均房间数
rom = df.groupby('商圈')['房间数'].mean()
top_5_rom = rom.sort_values(ascending=True).head(5)

# 筛选出五星级酒店的数据并计算平均评分
hotels = df[df['星级'] == '五星级']
average_rating = hotels['评分'].mean()

# 绘制每个商圈的酒店总数的柱状图
plt.figure(figsize=(15, 12))
hotel_counts = df.groupby('商圈')['住宿场所名称'].count()
hotel_counts.plot(kind='bar')
plt.title('各商圈酒店总数')
plt.xlabel('商圈')
plt.ylabel('酒店总数')

# 绘制前 100 个住宿场所名称的平均评分的折线图
gd = df.groupby('住宿场所名称')['评分'].mean().reset_index().head(100)
plt.figure(figsize=(15, 16))
plt.plot(gd['住宿场所名称'], gd['评分'], marker='.')
plt.title('各星级酒店平均评分变化')
plt.xlabel('住宿场所名称')
plt.ylabel('平均评分')
plt.xticks(rotation=90)

# 输出
print(top_5_ht)
print('房间数', top_5_rom)
print(f"所有五星级酒店的平均评分为：{average_rating:.2f}")
plt.show()