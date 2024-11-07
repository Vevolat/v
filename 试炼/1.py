import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('1.csv',encoding='GBK')
print(df)
r = df['合计']
n = df['年龄']

plt.rcParams['font.family'] = 'SimSun'
plt.figure(figsize=(10,6))
plt.title('15岁以上')
plt.plot(n,r,marker='o',color='r')
for i in range(len(df)):
    plt.text(x=n[i],y=r[i],s=f'{r[i]}人')
plt.xticks(fontsize=12)
plt.xlabel('总计')
plt.ylabel('年龄')

plt.show()