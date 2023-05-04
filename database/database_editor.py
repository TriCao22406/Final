import pandas as pd
import random
from datetime import datetime, timedelta

# df = pd.read_csv("employees.csv")
# new_col = pd.Series("", index=df.index)
# df.insert(loc=2, column="new_column", value=new_col)
#
# df.to_csv("employees.csv", index=False)

df = pd.read_csv("employees.csv")

# Set the "mã nv" column to integer data type
df["mã nv"] = df["mã nv"].astype(int)

# Generate employee codes for each row
for i in range(len(df)):
    df.at[i, "mã nv"] = i + 1

df.to_csv("employees.csv", index=False)
