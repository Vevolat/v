import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# 读取数据
df = pd.read_csv('clean_month.csv')

df

# 月份
months = ['一月', '二月', '三月', '四月', '五月', '六月', '七月', '八月', '九月', '十月', '十一月', '十二月']

# 设置图表大小
sns.set()
plt.figure(figsize=(12, 8))
plt.rcParams['font.family'] = 'SimSun'
# 绘制折线图
plt.plot(months, shanghai_data, marker='o', label="上海")
plt.plot(months, cq_data, marker='o', label="重庆")
plt.plot(months, qingdao_data, marker='o', label="青岛")
# x轴的刻度标签
plt.xticks(np.arange(len(months)), months)
# 标题和轴标签
plt.title("2011-2021年3城市每月平均高温对比")
plt.xlabel("月份")
plt.ylabel("温度（℃）")
# 添加图例
plt.legend()
# 加标签
for i, (qd, cq, sh) in enumerate(zip(qingdao_data, cq_data, shanghai_data)):
    plt.annotate(f'{qd:.2f}', (i, sh), textcoords="offset points", xytext=(0,10), ha='center')
    plt.annotate(f'{cq:.2f}', (i, cq), textcoords="offset points", xytext=(0,10), ha='center')
    plt.annotate(f'{sh:.2f}', (i, qd), textcoords="offset points", xytext=(0,10), ha='center')
# 显示图表
plt.show()