import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('02(1.csv')

die = df['万人']
years = df['年份']

plt.rcParams['font.family'] = 'SimSun'
plt.figure(figsize=(8, 6))
plt.title('灾难总死亡人数', fontsize=20)
plt.plot(years, die, marker='o', c='r')
plt.xlabel('年份', fontsize=16, loc='left')
plt.ylabel('死亡人数(万人)', fontsize=16, loc='top')

plt.xticks(rotation=45)
plt.xticks(range(1906 + 14, 2018 + 3, 20))
plt.show()