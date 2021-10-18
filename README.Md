# Processo Seletivo - Casa Mineira - Analista de BI/Dados

O Dashboard pode ser acessado através [deste link](https://app.powerbi.com/view?r=eyJrIjoiNTg5YWZkZTctNTc3Mi00M2M3LTgzNjktNjQwNDBiMTAzZmJjIiwidCI6ImFmOTdjMzM5LTE3ODMtNDIzZi1iZGNmLTQ5ODViZmMwOTQ3ZSJ9).

O repositório está organizado da seguinte maneira:

    ├── Dados Brutos                          # Base de dados original
    ├── Dados Tratados                        # Base de dados tratada
    ├── Scripts Tratamento                    # Scripts em Python utilizados para tratamento dos dados
    ├── Dashboard.pbix                        # Arquivo do Microsoft Power BI com Dashboard                    
    ├── JeffersonBASIlva_Apresentacao.pdf     # Apresentação sobre os análise feita
    ├── LICENSE
    └── README.md

# Introdução

## Cenário

A empresa **Casa Mineira Imóveis** disponibilizou uma base de dados com **5.367** entradas e **10** variáveis para análise como parte do Processo Seletivo para **Analista de BI/Dados Jr.**.

## Objetivo Gerais

- Entender os dados presentes na base fornecida para extrair o máximo de
informações relevantes;
- Apresentar as informações obtidas através de um dashboard

## Objetivos Específicos
- Analisar a evolução do volume de ocorrências geradas ao longo do período;
- Calcular a taxa de conversão de ocorrências;
- Identificar as Imobiliárias que geram maior número de ocorrências;
- Avaliar se há diferença na taxa de conversão de clientes novos e recorrentes;
- Avaliar o impacto dos tipos de Canal de Origem na geração de ocorrências;
- Identificar a etapa do processo que acumula maior número de ocorrências
perdidas;
- Calcular o tempo médio de duração das ocorrências.

## Ferramentas Utilizadas
- **Python**: Utilizado para tratamento da base de dados, definição das variáveis a serem utilizadas e realização de análises preliminares;
  - O script de tratamento pode se encontrado na pasta `Script Tratamento`;
- **Microsoft Power BI**: Utilizado para análise mais detalhada dos dados,
definição de indicadores a serem acompanhados e criação do dashboard.

## Base de Dados

A base possui 5367 entradas e 10 variáveis e foi apresentada da seguinte forma:

|Índice| Negócio - Negócio criado em |	Negócio - Organização 2 |	Negócio - Novo cliente? |	Negócio - Etapa |	Negócio - Status | Negócio - Data de ganho |	Negócio - Data de perda |	Organização - Canal de Origem	| Negócio - Data atualizada	| Negócio - Data da Última Atividade|
| :------------- | :------------- |  :------------- |  :------------- |  :------------- |  :------------- |  :------------- |  :------------- |  :------------- |  :------------- |  :------------- |
|0 |	2021-03-22 10:48:41 |	Imobiliária 1 |	Sim |	07 - Negociação |	Perdido |	NaN |	2021-03-29 13:04:16 |	Tipo D |	2021-08-04 11:47:13 |	2021-03-29
|1 |	2021-03-22  10:56:21	| Imobiliária 1 |	Não |	05 - Acompanhamento |	Perdido |	NaN	| 2021-03-22 16:37:50 |	Tipo D |	2021-04-30 14:14:25 |	2021-03-23 |
|2 |	2021-03-22 10:59:57 |	Imobiliária 1 |	Não |	07 - Negociação	| Ganho |	2021-04-01 12:19:44 |	NaN	| Tipo D |	2021-07-30 16:34:17 |	2021-04-01 |
|3 |	2021-03-22 11:03:14 |	Imobiliária 1 |	Não	| 04 - Pós-visita |	Perdido	| NaN |	2021-03-22 15:49:21 |	Tipo D	| 2021-04-30 14:17:10 |	2021-03-23 |
|4 |	2021-03-23 10:37:22 |	Imobiliária 5 |	Não |	01 - Contato |	Perdido	| NaN |	2021-04-12 08:37:17 |	Tipo C |	2021-04-30 14:58:51 |	2021-04-12 |

Após primeiro contato com a base de dados, foram realizados pequenos ajustes nos nomes das colunas para facilitar o trabalho.

|Índice | Data de criação |	Organização |	Novo cliente? |	Etapa |	Status |	Data de ganho |	Data da perda |	Canal de Origem |	Data de atualização	| Data da última atividade |
| :------------- | :------------- |  :------------- |  :------------- |  :------------- |  :------------- |  :------------- |  :------------- |  :------------- |  :------------- |  :------------- |
|0 |	2021-03-22 10:48:41 |	Imobiliária 1 |	Sim |	07 - Negociação |	Perdido |	NaN |	2021-03-29 13:04:16 |	Tipo D |	2021-08-04 11:47:13 |	2021-03-29
|1 |	2021-03-22  10:56:21	| Imobiliária 1 |	Não |	05 - Acompanhamento |	Perdido |	NaN	| 2021-03-22 16:37:50 |	Tipo D |	2021-04-30 14:14:25 |	2021-03-23 |
|2 |	2021-03-22 10:59:57 |	Imobiliária 1 |	Não |	07 - Negociação	| Ganho |	2021-04-01 12:19:44 |	NaN	| Tipo D |	2021-07-30 16:34:17 |	2021-04-01 |
|3 |	2021-03-22 11:03:14 |	Imobiliária 1 |	Não	| 04 - Pós-visita |	Perdido	| NaN |	2021-03-22 15:49:21 |	Tipo D	| 2021-04-30 14:17:10 |	2021-03-23 |
|4 |	2021-03-23 10:37:22 |	Imobiliária 5 |	Não |	01 - Contato |	Perdido	| NaN |	2021-04-12 08:37:17 |	Tipo C |	2021-04-30 14:58:51 |	2021-04-12 |


## Variáveis Utilizadas

Após tratamento da base de dados, foram utilizadas as seguintes variáveis:

- **Data de Criação**: Apresenta a data de criação da ocorrência;
- **Organização**: Identifica a imobiliária que gerou a ocorrência;
- **Novo cliente?**: Identifica se a ocorrência foi gerada por um novo cliente;
- **Etapa**: Apresenta em qual etapa a ocorrência se encontra desde a última atualização;
- **Status**: Identifica o status da ocorrência;
- **Data de ganho**: Indica a data que a ocorrência foi ganha;
- **Data da perda**: Indica a data que a ocorrência foi perdida;
- **Canal de origem**: Indica qual a partir de qual canal a ocorrência foi gerada.
7

## Premissas
- Devido ao baixo índice de ocorrências ganhas, estas não foram utilizadas
como parâmetro para análises;
- Os campos **Data de Atualização** e **Data da Última Atividade**
não foram utilizados na análise por não apresentarem informações
relevantes;
- Assumimos o campo **Novo Cliente?** independente do campo **Organização**.

<!--- # Análise Exploratória

## Variáveis utilizadas


Destes campos, podemos obter as seguintes informações iniciais:
- **Data de criação**
  - A base possui ocorrências registradas no período entre 22/03/2021 e 14/10/2021;
- **Organização**
  - As ocorrências registradas partem de 258 imobiliárias distintas;
- **Novo cliente?**
  - Destas ocorrências, 1709 vieram de novos clientes, 1689 de clientes antigos e 1969 não possuem descrição; *Como vamos considerar os que não possuem descrição?*
- **Etapa**
  - O processo se desenvolve em **6** etapas, a saber:
    1. Contato;
    2. Tá quente;
    3. Visita agendada;
    4. Pós-visita;
    5. Acompanhamento;
    6. Negociação.
- **Status**
  - Das ocorrências, 4081 foram perdidas, 1264 estão em aberto e 22 foram ganhas.
- **Data de ganho**
  - Todas as 22 conclusões positivas possuem data.
- **Data da perda**
  - Todas as 4081 ocorrências perdidas possuem data, o que coincide com os 1264 em aberto e 22 ganhas.
- **Canal de origem**
  - Existem 4 tipos de origem para a ocorrência, a saber:
    - Tipo A, com 546 ocorrências;
    - Tipo B, com 1906 ocorrências;
    - Tipo C, com 1368 ocorrências;
    - Tipo D, com 1547 ocorrências.
- **Data de atualização**
  - Nada a declarar
- **Data da última atividade**
  - Existem 1690 ocorrência que não possuem data de última atividade;
  - Estas possuem os três possíveis status e 6 possíveis etapas.

# Análises

- Evolução da quantidade de negócios a cada mês;
  - O número de ocorrências têm crescido ao longo dos meses registrados;
  - Podemos observar, em especial, um aumento maior entre os meses de junho e julho de 2021;
  - *Vale a pena remover os dados de Outubro para ter uma visualizaçao mais real dos dados?*
- Taxa de conversão para negócios ganhos;
  - As ocorrências ganhas representam 0.41% (22 de 5367) de todas as ocorrências registradas;
- Top N imobiliárias na geração de ocorrências;
  - 12 imobiliárias representam 25% das ocorrências;
- Proporção de ocorrências com respeito a novos clientes;
  - 36,69% (1969) das ocorrências não possuem informação sobre o status do cliente;
  - Desconsiderando os que não possuem informação, a divisão é bem equilibrada: 50,29% (1709) clientes novos e 49,71%(1689) clientes antigos.
- Proporção de ocorrências com respeito ao canal de origem;
  - O Canal Tipo B gerou o maior número de ocorrências, seguido pelo Tipo D, C e A respectivamente;
  - Apesar da diferença no volume de ocorrências, a taxa de conversão de todos os canais foi igual. Além disso, estes possuem correlação positiva, isto é, quanto maior o número de ocorrências geradas, maior o número de ocorrências ganhas para todas os canais.
  quanto maior o número
- Distribuição dos negócios perdidos com respeito às etapas;
  - Dos negócios perdidos, 41,41% foram perdidos na Etapa 5 (Acompanhamento)
- Duração média da ocorrência;
  - A duração média das ocorrências é de 20,60 dias, sendo 20,40 para ocorrências ganhas e 20,80 para ocorrências perdidas. --->

# Análise da viabilidade de Indicadores a serem avaliados

Foi realizada uma busca por referências que indicassem indicadores relevantes para o mercado imobiliário. Através desta pesquisa, foram identificados os seguintes indicadores:

## Indicadores escolhidos para acompanhamento
- Negócios Fechados
  - Quantidade de negócios fechados
- Oportunidades Criadas
  - Quantidade de negócios iniciados
- Negócios em aberto
  - Quantidade de negócios em aberto
- Tempo para fechar o negócios
  - Auto explicativo
- Taxa de Conversão
  - Numero de Oportunidades divididos pelo de negócios fechados

### Referências Utilizadas

#### 9 Indicadores de desempenho para uma imobiliária de Locação

[Referência](https://imobireport.com.br/9-indicadores-de-desempenho-kpis-para-uma-imobiliaria-de-locacao/)
- Taxa de Conversão
  - Numero de Oportunidades dividios pelo de negócios fechados
- ~~Custo de aquisiçao de cliente~~
  - ~~Soma de todas as despesas em um período dividido pelo numero de clientes adquiridos no período~~
- ~~Valor Geral de Aluguel~~
  - ~~Faturamento bruto com aluguéis~~
- ~~Tícket médio~~
  - ~~Divisão do faturamento com alguel pelo número de imóveis alugados~~
- ~~Visitas por locação~~
  - ~~Auto explicativo~~
- ~~Tempo médio do imóvel em divulgação~~
  - ~~Auto explicativo~~
- ~~Net Promoter Score~~
  - ~~Avaliação de 0 a 10 de um cliente recomendar a empresa~~
- ~~Índice de permanêcia de imóveis desocupados~~
  - ~~Dentre os imóveis que são desocupados, quantos permanecem na carteira~~;
- ~~Percentual de imóveis alocados~~
  - ~~Percentual dos imóveis disponíveis que foram alugados em determinado período de tempo~~.
- Negócios Fechados (Status do negócio = Ganho)
- Oportunidades Criadas (Negocio Criado)
- Negócios em aberto

#### Guia definitivo de vendas imobiliárias: 8 KPI’s essenciais para seu negócio
[Referência](https://www.vistasoft.com.br/vendas-imobiliarias/)
- Negócios fechados
  - Auto explicativo
- Oportunidades Criadas
  - Auto explicativa
- Propostas Feitas
  - Verifica quantas das oportunidades geraram Propostas
- ~~Custo de aquisiçao de clientes~~
  - ~~Custo gerado para imobiliária para que uma oportunidade se torne um cliente~~
- ~~Retorno sobre investimento~~
  - ~~Quanto do que foi investido retornou como lucro~~
- ~~Ranqueamento em motores de buscas~~
  - ~~Auto explicativo~~
- ~~Nível de Engajamento do Cliente On-line~~
  - ~~Auto explicativo~~
- ~~Taxa de Retenção de Clientes~~
  -  ~~Porcentagem de clientes que continuam sendo clientes.~~

#### 6 indicadores de desempenho que você precisa acompanhar na sua imobiliária
[Referência](https://www.groupsoftware.com.br/blog/indicadores-de-desempenho/)
- ~~Ticket médio~~
  - ~~Receita total dividido pelo número de negócios realizados~~
- Taxa de Conversão
  -  Porcentagem de negócios que foram concluidos
-  ~~Taxa de Churn~~
  - ~~Porcentagem de cancelamentos~~
- Tempo para fechar o negócios
  - Auto explicativo
-  ~~Taxa de followup~~
  - ~~Quantidade de contatos atendidos dividido pelo contato com clientes que apresentaram recusas~~
- ~~Índice de recomendação~~

# Conclusão

## Ações Sugeridas

Baseado na análise dos dados fornecidos, pode-se sugerir as seguintes ações:

- Trabalhar juntamente com a equipe responsável pela **Etapa 5 – Acompanhamento** do processo, pois das
ocorrências perdidas **41,41%** delas ocorreram nesta etapa;
- Alinhar com os colaboradores sobre a necessidade de preenchimento do campo **"Novo Cliente?"**
corretamente, uma vez que este pode auxiliar no melhor direcionamento de ações a serem tomadas;
- Análise das **ações** realizadas durante o mês de **Junho/2021** para possível aplicação em meses futuros;
- Analisar mais a fundo o **desempenho** do canal **Tipo A**, uma vez que este gerou **menos ocorrências** quando
comparado aos outros.

## Próximos Passos

Caminhos para a continuação destas análises são:

- Trabalhar com informações relacionadas à receita gerada pelos negócios fechados e investimento necessário
em cada Canal de Origem para avaliar a retorno sobre o investimento;
- Estudo da organização do preenchimento dos campos “Data de Atualização” e “Data da Última Atividade” para
avaliar a viabilidade de um possível retrabalho das ocorrências perdidas após determinado tempo.
- Trabalhar com informações geográficas para análise de desempenho separado por região;
- Trabalhar com informações de Analytics para analisar desempenho por faixa etária, sexo, renda e etc
