### --- Importanto bibliotecas --- ###
import pandas as pd

### --- Importando a base --- ###
df = pd.read_csv("./Dados Brutos/BD_Teste BA.xlsx - BD_visitas.csv")

df.head()
df.info()

## -- Análse dos campos -- ##

# - Negócio - Negócio criado em -- ##
df = df.rename(columns={"Negócio - Negócio criado em":"Data de criação"}) #Renomear a coluna
df.iloc[:,0].sort_values()

# -  Negócio - Organização 2  - #
df = df.rename(columns={"Negócio - Organização 2":"Organização"})
df.iloc[:,1].drop_duplicates().count()

# - Negócio - Novo cliente? - #
df = df.rename(columns={"Negócio - Novo cliente?":"Novo cliente?"})
df.iloc[:,2].value_counts()
df.loc[(df["Novo cliente?"].isnull())].count()

# - Negócio - Etapa - #
df = df.rename(columns={"Negócio - Etapa":"Etapa"})
df.iloc[:,3].drop_duplicates().sort_values()

# - Negócio - Status - #
df = df.rename(columns={"Negócio - Status":"Status"})
df.iloc[:,4].value_counts()

# - Negócio - Data de ganho - #
df = df.rename(columns={"Negócio - Data de ganho":"Data de ganho"})
df.iloc[:,5].dropna().count()

# - Negócio - Data de perda -#
df = df.rename(columns={"Negócio - Data de perda":"Data da perda"})
df.iloc[:,6].count()

# - Organização - Canal de Origem - #
df = df.rename(columns={"Organização - Canal de Origem":"Canal de Origem"})
df.iloc[:,7].value_counts()

# - Negócio - Data atualizada - #
df = df.rename(columns={"Negócio - Data atualizada":"Data de atualização"})
df.iloc[:,8].sort_values()

# - Negócio - Data da Última Atividade - #
df = df.rename(columns={"Negócio - Data da Última Atividade":"Data da última atividade"})
df.loc[(df["Data da última atividade"]).isnull()]
df.loc[(df["Data da última atividade"]).isnull()]["Etapa"].value_counts()
df.loc[(df["Data da última atividade"]).isnull()]["Status"].value_counts()
len(df.loc[(df["Data da última atividade"]).isnull()].index)

# - Exibição após tratamento inicial - #
df.head()


# - Exportando a base tratada - #
df.to_csv("./Dados Tratados/Base_tratada.csv")
