import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('02(2.csv')
yuan = df['亿元']
year = df['年份']

plt.rcParams['font.family'] = 'SimSun'
plt.figure(figsize=(8, 6))
plt.plot(year, yuan, marker='o', c='violet')
plt.title('灾难总经济损失', fontsize=20)
plt.xlabel('年份', fontsize=16)
plt.ylabel('总经济损失（亿元）', fontsize=16)

plt.show()
