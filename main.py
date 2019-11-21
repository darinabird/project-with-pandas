import pandas as pd

df1 = pd.read_csv("cidr_optim.txt", delimiter='\t')
df2 = pd.read_csv("cities.txt", delimiter='\t')
df3 = pd.read_csv("test(new).csv")

df3.merge(df2, how='outer')
