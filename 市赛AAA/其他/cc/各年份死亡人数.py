import matplotlib.pyplot as plt
import numpy as np


# 假设的死亡人数数据
death_counts = np.array([100, 10, 200, 40])
# 对应的年份
years = np.arange(2000, 2020, 5)  # 从1920到2020，每隔10年


# 检查年份和死亡人数数据的长度是否一致,   可不加
#if len(death_counts) != len(years):
#   print("年份和死亡人数数据的数量不一致，请检查数据。")
#else:
plt.rcParams['font.family'] = 'SimHei'
# 创建图表
plt.figure(figsize=(10, 6))
# 绘制折线图
plt.plot(years, death_counts, marker='o', color='r')
# 设置x轴和y轴的标签
plt.xlabel("年份", fontsize=16, loc="left")
plt.ylabel('总死亡人数(万人)', fontsize=16, loc="top")
# 设置图表的标题
plt.xticks(rotation=45)
plt.title("死亡人数", fontsize=20)
# 设置x轴的刻度为指定的年份
plt.xticks(years)
# 显示网格（可选）
plt.grid(True)
# 显示图表
plt.show()