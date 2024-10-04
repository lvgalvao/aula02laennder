import pandas as pd

# Leitura dos CSVs de clientes e vendas
df_clientes = pd.read_csv('clientes.csv')
df2= pd.read_csv('vendas.csv')
df3 = pd.read_csv('vendas_2.csv')
df4 = pd.read_csv('vendas_3.csv')

df_todas_as_vendas = pd.concat([df2, df3, df4])
print(df_todas_as_vendas)

df_unionall = pd.merge(df_todas_as_vendas,df_clientes,on="cliente_id")

df_unionall["valor_total"] = df_unionall["quantidade"]*df_unionall["valor_unitario"]

from ydata_profiling import ProfileReport

profile = ProfileReport(df_unionall, title="Profiling Report")

profile.to_file("relatorio_vendas_v5.html")