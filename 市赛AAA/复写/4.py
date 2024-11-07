import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('clean_day.csv')
df = df.groupby('city')['hightest_tem'].max().reset_index()
df['hightest_tem'] = df['hightest_tem'].round(2)
top = df.nlargest(10, 'hightest_tem')
color = sns.color_palette('hls', len(top))

plt.rcParams['font.family'] = 'SimSun'
plt.bar(top['city'], top['hightest_tem'], color=color)
plt.title('')
plt.xlabel('')
plt.ylabel('')
for i, temp in enumerate(top['hightest_tem']):
    plt.text(i, temp, f'{temp}度', va='bottom', ha='center')

plt.show()