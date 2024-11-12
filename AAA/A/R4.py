import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('clean_day.csv')
# print(df)
city_max = df.groupby('city')['hightest_tem'].max().reset_index()
city_max['hightest_tem'] = city_max['hightest_tem'].round(2)
top_10 = city_max.nlargest(10, 'hightest_tem')
# print(city_max)
colors = sns.color_palette('hls', len(top_10))

plt.figure(figsize=(8, 6))
plt.rcParams['font.family'] = 'SimSun'
plt.bar(top_10['city'], top_10['hightest_tem'], color=colors)
plt.title("2011-2021中高温城市排名")
plt.xlabel("城市")
plt.ylabel("最高温（℃）")
plt.xticks(rotation=45, fontsize=16)
plt.ylim(0, 55)
for i, y in enumerate(top_10['hightest_tem']):
    plt.text(i, y, f'{y}℃', ha='center', va='bottom', fontsize=16)
plt.ylim(0, 55)
plt.show()