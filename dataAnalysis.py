import pandas as pd

df = pd.read_csv('summary.csv')

sum = 0

for index, row in df.iterrows():
    if (row[1] <= 40000) and (row[2] <= 40000):
        sum = sum + 1

print(sum)