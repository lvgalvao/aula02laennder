# %%
import pandas as pd

df_pessoas = pd.read_csv("exemplo.csv")

print(df_pessoas)

print(df_pessoas["idade"])

print((df_pessoas["idade"].mean()))
print((df_pessoas["idade"].median()))