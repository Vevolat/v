import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('yuan.csv')
yuan = df['亿元']
year = df['年份']

plt.figure(figsize=(10, 5))
plt.rcParams['font.family'] = 'SimSun'
plt.plot(year, yuan, marker='o', color='violet')
plt.title('经济损失', fontsize=20)
plt.xlabel('年份', fontsize=16)
plt.ylabel('总经济损失（亿元）', fontsize=16)

plt.show()