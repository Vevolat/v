import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('CN.csv')
die = df['万人']
year = df['年份']

plt.figure(figsize=(10, 5))
plt.rcParams['font.family'] = 'SimSun'
plt.plot(year, die, marker='o', color='r')
plt.title('死亡人数', fontsize=20)
plt.xlabel('年份', fontsize=16)
plt.ylabel('总死亡人数（万人）', fontsize=16)

plt.show()