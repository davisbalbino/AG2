# AG2
## Classificao de Especies de Pinguins com Decision Tree

Este repositório contém um código em Python para classificação de espécies de pinguins utilizando o algoritmo de árvore de decisão (DecisionTreeClassifier) da biblioteca scikit-learn. O conjunto de dados utilizado é o "Palmer Penguins", que foi previamente processado e salvo em um arquivo CSV.

#### Bibliotecas utilizadas:

`pandas` para manipulação de dados.

 
`scikit-learn` para modelagem e valiação.

#### Carregamento e Pré-processamento dos Dados

Os dados são carregados de um arquivo CSV e pré-processado:
Convertendo valores os valores(`island`, `sex`, `species`) em valores do tipo inteiro, e reorganizando as colunas e salvando o resultado em um novo arquivo CSV.

#### Divisão dos Dados e Treinamento do Modelo
Os dados são divididos em conjuntos de treinamento e teste, e o modelo de árvore de decisão é treinado com os dados de treinamento, a acurácia do modelo é calculada e exibida, juntamente com um relatório de classificação detalhado que inclui precisão


#### Classificação de Novos Dados
Uma função é definida para classificar novos dados inseridos pelo usuário, exibindo a previsão da espécie do pinguim com base no modelo treinado.

#### Resultados Esperados
Ao executar o script, você verá a acurácia do modelo nos dados de teste e um relatório de classificação. Também poderá inserir novos dados para prever a espécie de pinguins.

### Autores:
Davi dos Santos Balbino Marcelino - - GES

Vinicius Batista Ribas - 1508 - GEC

## Link do Videos: