import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('renwu32.csv', encoding="GBk")
df = df.groupby(['yf', 'city']).mean().round(2)
df = df.sort_values(by=['id'])
df = df.reset_index()

sns.set_theme(style='darkgrid', font_scale=2)
plt.rcParams['font.family'] = 'SimSun'
sns.lineplot(data=df, x='yf', y='avg_high_tem', hue='city')
plt.xlabel('')
plt.ylabel('')
plt.title('')
for i in range(len(df)):
    plt.text(df['yf'][i], df['avg_high_tem'][i], f'{df['avg_high_tem'][i]}度', va='bottom', ha='center', color='#996600')

plt.show()