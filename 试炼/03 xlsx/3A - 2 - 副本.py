import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('hotel.csv',encoding='gbk')
plt.rcParams['font.family'] = 'SimSun'

plt.figure(figsize=(15,16))
plt.title('各个商圈的酒店总数', fontsize=20)
zs = df.groupby('商圈')['住宿场所名称'].count()
zs.plot(kind='bar')
plt.xlabel('商圈', fontsize=16)
plt.ylabel('酒店数量', fontsize=16)


plt.figure(figsize=(15,16))
plt.title('各个商圈的酒店数量', fontsize=20)
zs = df.groupby('商圈')['各个商圈的酒店数量'].count()
sns.lineplot(data=zs, x='各个商圈的酒店数量', y='商圈', markers='o', ls='s')

plt.show()