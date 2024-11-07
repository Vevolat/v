import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 设置Seaborn的主题
sns.set_style('whitegrid')

# 设置图像大小和字体
plt.rcParams['font.family'] = 'SimSun'
plt.rcParams['font.size'] = 3  # 可以根据需要调整字体大小

# 读取CSV文件
df = pd.read_csv('clean_day.csv')

# 计算每个城市的最高温度
city_max_temp = df.groupby('city')['hightest_tem'].max().reset_index()
top_10 = city_max_temp.nlargest(10, 'hightest_tem')

# 获取颜色
colors = sns.color_palette("hls", len(top_10))

# 设置图像大小
plt.figure(figsize=(15, 10))

# 绘制柱形图，使用从Seaborn调色板获取的颜色
bars = plt.bar(top_10['city'], top_10['hightest_tem'], color=colors)

# 在柱形图上添加文本
for bar in bars:
    y_val = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/3.5, y_val, f'{y_val}℃', va='bottom', fontsize=12)

# 设置标题和轴标签
plt.title("2011-2021中高温城市排名", fontsize=20)
plt.xlabel("城市", fontsize=18)
plt.ylabel("最高温（℃）", fontsize=18)

# 设置横轴的刻度标签
plt.xticks(rotation=45, fontsize=16)  # 旋转45度以便更好地显示城市名称

# 设置纵轴的刻度范围
plt.ylim(0, 55)

# 显示图表
plt.show()