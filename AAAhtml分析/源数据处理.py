import pandas as pd

df = pd.read_json('源数据.json')
print(df)
df.to_csv('源数据.csv')