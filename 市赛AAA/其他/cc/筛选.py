import pandas
import pandas as pd

df = pd.read_csv('clean_month.csv')
qingdao_rows = df[df['city'] == '青岛']

# 获取'year_month'列的值的后三位和对应的'avg_high_tem'列的值
qingdao_rows['month_end'] = qingdao_rows['month'].apply(lambda x: x[-3:])

# 按'month_end'分组并计算每个组的'avg_high_tem'值的总和
sum_temps_by_month_end = qingdao_rows.groupby('month_end')['avg_high_tem'].sum()

# 计算每个'month_end'的数量
counts_by_month_end = qingdao_rows.groupby('month_end')['avg_high_tem'].count()

# 计算平均值
avg_temps_by_month_end = sum_temps_by_month_end / counts_by_month_end

# 打印结果
print('青岛')
for month_end, avg_temp in avg_temps_by_month_end.items():
    print(f"{month_end}: {avg_temp:.2f}℃")









sh_rows = df[df['city'] == '上海']

# 获取'year_sh'列的值的后三位和对应的'avg_high_tem'列的值
sh_rows['month_sh'] = sh_rows['month'].apply(lambda x: x[-3:])

# 按'month_sh'分组并计算每个组的'avg_high_tem'值的总和
sum_temps_by_month_end = sh_rows.groupby('month_sh')['avg_high_tem'].sum()

# 计算每个'month_sh'的数量
sh_counts_by_month_end = sh_rows.groupby('month_sh')['avg_high_tem'].count()

# 计算平均值
avg_temps_by_month_end = sum_temps_by_month_end / sh_counts_by_month_end

# 打印结果
print('上海')
for month_sh, avg_temp in avg_temps_by_month_end.items():
    print(f"{month_sh}: {avg_temp:.2f}℃")


















cq_rows = df[df['city'] == '重庆']

# 获取'year_cq'列的值的后三位和对应的'avg_high_tem'列的值
cq_rows['month_cq'] = cq_rows['month'].apply(lambda x: x[-3:])

# 按'month_sh'分组并计算每个组的'avg_high_tem'值的总和
sum_temps_by_month_end = cq_rows.groupby('month_cq')['avg_high_tem'].sum()

# 计算每个'month_cq'的数量
cq_counts_by_month_end = cq_rows.groupby('month_cq')['avg_high_tem'].count()

# 计算平均值
avg_temps_by_month_end = sum_temps_by_month_end / cq_counts_by_month_end

# 打印结果
print('重庆')
for month_cq, avg_temp in avg_temps_by_month_end.items():
    print(f"{month_cq}: {avg_temp:.2f}℃")
