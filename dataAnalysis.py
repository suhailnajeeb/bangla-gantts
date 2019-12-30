import pandas as pd

df = pd.read_csv('summary.csv')

for index, row in df.iterrows():
    print(row[1])
    print(row[2])