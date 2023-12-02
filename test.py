import pandas as pd
# Carregar os dados do Excel para um DataFrame Pandas
df = pd.read_excel('Financial.xlsx')

df_dataframe = pd.DataFrame()
# Verificar as colunas presentes no DataFrame
print(df.columns)

# Verificar as primeiras linhas do DataFrame para garantir a presença da coluna 'Year'
print(df.head)

