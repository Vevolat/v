import pandas as pd
import matplotlib.pyplot as plt

# 读取数据
data = pd.read_csv('fj.csv', encoding='gbk')

# 初始化
plt.rcParams['font.family'] = 'SimSun'
plt.title('死亡人数之比', fontsize=20)

# 绘图
plt.pie(data=data, x =data['a'], explode=data['b'], labels=data['国家'], autopct='%.2f%%')

plt.show()