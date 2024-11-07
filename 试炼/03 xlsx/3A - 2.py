import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('hotel.csv',encoding='gbk')
plt.rcParams['font.family'] = 'SimSun'

plt.figure(figsize=(15,10))
plt.title('各个商圈的酒店总数', fontsize=20)
plt.xlabel('商圈', fontsize=16)
plt.ylabel('酒店数量', fontsize=16)
jd = df.groupby('商圈')['住宿场所名称'].count()
jd.plot(kind='bar')

plt.figure(figsize=(15,10))
plt.title('各星级酒店平均评分走势', fontsize=20)
plt.xlabel('商圈', fontsize=16)
plt.ylabel('评分', fontsize=16)
plt.xticks(rotation=90)
jdzs = df.groupby('住宿场所名称')['评分'].mean().reset_index().head(100)
sns.lineplot(data=jdzs, x='住宿场所名称', y='评分', markers='o')

plt.show()