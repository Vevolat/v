import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('2初中.csv',encoding='gbk')
print(df)

n = df['年  龄']
r = df['合计1']

plt.figure(figsize=(15,10))
plt.rcParams['font.family'] = 'SimSun'
plt.title('全国初高中受教育程度人口(镇)',fontsize=16)
plt.plot(n,r,marker='o',color='blue')
for i in range(len(df)):
    plt.text(x=n[i],y=r[i],s=f'{r[i]}人')

df = pd.read_csv('2高中.csv',encoding='gbk')
print(df)
n = df['年龄']
r = df['合计1']
plt.plot(n,r,marker='o',color='r')
for i in range(len(df)):
    plt.text(x=n[i],y=r[i],s=f'{r[i]}万人')

plt.xlabel('年龄',fontsize=16)
plt.ylabel('人数(万)',fontsize=16)


plt.show()