import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 读取 CSV 文件
df = pd.read_csv('CN.csv')

wan = df['万人']
years = df['年份']

# 设置字体
plt.rcParams['font.family'] = 'SimSun'
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 创建图表并调整尺寸
plt.figure(figsize=(15, 10))  # 增大图表尺寸

# 绘制折线图
plt.title('死亡人数', fontsize=16)  # 设置标题字体大小
plt.plot(years, wan, marker='o', color='r', linestyle='-')  # 增加线型
plt.xlabel("年份", fontsize=16, loc="left")  # 设置x轴标签字体大小
plt.ylabel('死亡人数(万人)', fontsize=16, loc="top")  # 设置y轴标签字体大小

# 获取最小和最大年份
start_year = years.min()
end_year = years.max()

# 设置x轴刻度标签
plt.xticks(rotation=45)  # 将刻度标签旋转90度
plt.xticks(years)  # 设置x轴刻度为所有年份

# 显示图表
plt.tight_layout()  # 自动调整子图参数, 使之填充整个图表区域
plt.show()