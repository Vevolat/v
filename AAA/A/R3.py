import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('3.csv', encoding="GBk")
df = df.groupby(['月份', 'city']).mean().round(2)
df = df.sort_values(by=["id"])
df = df.reset_index()

# print(df)
sns.set()
sns.set_theme(style="darkgrid", font_scale=2)  # 或 sns.set(fontsize=2)
plt.rcParams['font.family'] = 'SimSun'
sns.lineplot(data=df, x='月份', y='avg_high_tem', hue='city', marker='o', linewidth=3)
for i in range(len(df)):
    plt.text(x=df['月份'][i], y=df['avg_high_tem'][i], s=f"{df['avg_high_tem'][i]}", c='#996600', ha='center', va='bottom', fontsize=16)

plt.title('2011-2021年3城市高温均值对比', fontsize=20)
plt.xlabel('月份', fontsize=16)
plt.ylabel('温度（℃）', fontsize=16)
plt.show()