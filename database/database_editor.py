import pandas as pd


df = pd.read_csv("employees.csv")
new_col = pd.Series("", index=df.index)
df.insert(loc=2, column="new_column", value=new_col)

df.to_csv("employees.csv", index=False)