import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# 假设的数据
qingdao = np.array([15.42, 28.27, 5.09, 4.67, 3.00, 27.18, 23.64, 9.83, 20.73, 9.83, 20.73, 12.36, 19.36, 25.36])
shanghai = np.array([20.42, 32.09, 10.27, 8.33, 32.45, 27.45, 14.92, 25.55, 16.91, 22.64, 27.82])
cq = np.array([23.00, 33.45, 10.82, 12.42, 9.58, 32.91, 28.91, 18.33, 26.09, 16.09, 20.91, 27.09])

# 对应的月份
months = np.array(['一月', '二月', '三月', '四月', '五月', '六月', '七月', '八月', '九月', '十月', '十一月', '十二月'])

# 设置图表大小
sns.set()

plt.figure(figsize=(12, 8))
plt.rcParams['font.family'] = 'SimSun'  # 替换为你选择的字体

# 绘制折线图
plt.plot(qingdao, marker='o', label="青岛")
plt.plot(cq, marker='o', label="重庆")
plt.plot(shanghai, marker='o', label="上海")

# 设置x轴的刻度标签
plt.xticks(np.arange(len(months)), months)

# 设置标题和轴标签
plt.title("2011-2021年3城市每月平均高温对比")
plt.xlabel("月份")
plt.ylabel("温度（℃）")

# 添加图例
plt.legend()

# 在每个点上添加标签
for i, txt in enumerate(qingdao):
    plt.annotate(f'{txt:.2f}', (i, qingdao[i]), textcoords="offset points", xytext=(0,10), ha='center')
for i, txt in enumerate(cq):
    plt.annotate(f'{txt:.2f}', (i, cq[i]), textcoords="offset points", xytext=(0,10), ha='center')
for i, txt in enumerate(shanghai):
    plt.annotate(f'{txt:.2f}', (i, shanghai[i]), textcoords="offset points", xytext=(0,10), ha='center')

# 显示图表
plt.show()