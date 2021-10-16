# Análise Exploratória da base de Dados

A base possui 5367 entradas e 10 variáveis e foi apresentada da seguinte forma:

|Índice| Negócio - Negócio criado em |	Negócio - Organização 2 |	Negócio - Novo cliente? |	Negócio - Etapa |	Negócio - Status | Negócio - Data de ganho |	Negócio - Data de perda |	Organização - Canal de Origem	| Negócio - Data atualizada	| Negócio - Data da Última Atividade|
| :------------- | :------------- |  :------------- |  :------------- |  :------------- |  :------------- |  :------------- |  :------------- |  :------------- |  :------------- |  :------------- |
|0 |	2021-03-22 10:48:41 |	Imobiliária 1 |	Sim |	07 - Negociação |	Perdido |	NaN |	2021-03-29 13:04:16 |	Tipo D |	2021-08-04 11:47:13 |	2021-03-29
|1 |	2021-03-22  10:56:21	| Imobiliária 1 |	Não |	05 - Acompanhamento |	Perdido |	NaN	| 2021-03-22 16:37:50 |	Tipo D |	2021-04-30 14:14:25 |	2021-03-23 |
|2 |	2021-03-22 10:59:57 |	Imobiliária 1 |	Não |	07 - Negociação	| Ganho |	2021-04-01 12:19:44 |	NaN	| Tipo D |	2021-07-30 16:34:17 |	2021-04-01 |
|3 |	2021-03-22 11:03:14 |	Imobiliária 1 |	Não	| 04 - Pós-visita |	Perdido	| NaN |	2021-03-22 15:49:21 |	Tipo D	| 2021-04-30 14:17:10 |	2021-03-23 |
|4 |	2021-03-23 10:37:22 |	Imobiliária 5 |	Não |	01 - Contato |	Perdido	| NaN |	2021-04-12 08:37:17 |	Tipo C |	2021-04-30 14:58:51 |	2021-04-12 |

Após ajuste nos nomes das colunas, temos:

|Índice | Data de criação |	Organização |	Novo cliente? |	Etapa |	Status |	Data de ganho |	Data da perda |	Canal de Origem |	Data de atualização	| Data da última atividade |
| :------------- | :------------- |  :------------- |  :------------- |  :------------- |  :------------- |  :------------- |  :------------- |  :------------- |  :------------- |  :------------- |
|0 |	2021-03-22 10:48:41 |	Imobiliária 1 |	Sim |	07 - Negociação |	Perdido |	NaN |	2021-03-29 13:04:16 |	Tipo D |	2021-08-04 11:47:13 |	2021-03-29
|1 |	2021-03-22  10:56:21	| Imobiliária 1 |	Não |	05 - Acompanhamento |	Perdido |	NaN	| 2021-03-22 16:37:50 |	Tipo D |	2021-04-30 14:14:25 |	2021-03-23 |
|2 |	2021-03-22 10:59:57 |	Imobiliária 1 |	Não |	07 - Negociação	| Ganho |	2021-04-01 12:19:44 |	NaN	| Tipo D |	2021-07-30 16:34:17 |	2021-04-01 |
|3 |	2021-03-22 11:03:14 |	Imobiliária 1 |	Não	| 04 - Pós-visita |	Perdido	| NaN |	2021-03-22 15:49:21 |	Tipo D	| 2021-04-30 14:17:10 |	2021-03-23 |
|4 |	2021-03-23 10:37:22 |	Imobiliária 5 |	Não |	01 - Contato |	Perdido	| NaN |	2021-04-12 08:37:17 |	Tipo C |	2021-04-30 14:58:51 |	2021-04-12 |

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
# Análise da viabilidade de Indicadores a serem avaliados

### 9 Indicadores de desempenho para uma imobiliaria de Locaçao
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

### Guia definitivo de vendas imobiliárias: 8 KPI’s essenciais para seu negócio
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

### 6 indicadores de desempenho que você precisa acompanhar na sua imobiliária
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

## Indicadores escolhidos
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
