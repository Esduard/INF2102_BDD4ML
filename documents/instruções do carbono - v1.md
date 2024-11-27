# Projeto Carbono  - Versão 1

Visualize esse documento usando o comando 'Cntrl + Shift + V'

## Descrição Do Projeto

Uma empresa de transporte de carga precisa estimar quanto de gás carbono (CO2) irá emitir em um dado trecho de viagem

Uma equipe de cientistas de dados desenvolveu um modelo de regressão que estima quanto uma viagem irá gerar de C02.

## Pós processamento

Após a estimativa de valor exato da quantidade de CO2. O algoritimo passa por uma rotina de pós-processamento o qual atribui uma classe (`A` até `E`) ao valor estimado. Essa classificação é baseada em intervalos fechados:

- Os limites dependem do tipo de embarcação, parametrizando eles em `d1`, `d2`, `d3` e `d4`, o sistema cria categorias de classificação para o valor de CO2:

## Classificação de Emissão de CO2

| Classe | Intervalo de Valores de CO2 | Descrição                              |
|--------|------------------------------|----------------------------------------|
| A      | < `d1`                       | Emissões muito baixas                  |
| B      | `d1` ≤ CO2 < `d2`            | Emissões baixas                        |
| C      | `d2` ≤ CO2 < `d3`            | Emissões moderadas                     |
| D      | `d3` ≤ CO2 < `d4`            | Emissões altas                         |
| E      | ≥ `d4`                       | Emissões muito altas                   |


- Cada valor estimado de CO2 é comparado com esses limites para receber uma classificação correspondente. Tornando o problem de regressão em um de classificação.

## Transformação de Regressão para Classificação


## Objetivo

Com o modelo pronto e os casos de teste preparados você deve gerar clausulas BDD em texto livre para informar seus superiores sobre o desempenho do modelo em termos de classificar as viagens corretamente. Tenha em mente que sua audicencia não tem conhecimento de métricas de classificação então você deverá gerar clausulas que, além de mostrar os resultados das metricas, as expliquem diretamente.

Este desafio consiste em gerar cláusulas BDD *Em Inglês* para analisar o desempenho desse modelo classificando os valores em seus ranks corretos.

Com seu conhecimento em aprendizado de máquina, gere cláusulas BDD que atendam aos seguintes critérios:

### Requisitos do contexto do problema

- Instrua o nome do arquivo do modelo que deseja testar

- Instrua o nome do arquivo de testes que deseja utilizar para avaliar o modelo

- Instrua se o modelo é de classificação ou de regressão.

- Instrua que deseja utilizar um pré-processador customizado

- Instrua que deseja utlizar um pós-processador customizado

### Requisitos de Recall

- Meça se a métrica de revocação (recall) alcança 50 porcento dos casos 

- Meça se a métrica de revocação (recall) alcança 40 porcento dos casos da classe D


### Requisitos de Precisão

- Meça se a métrica de precisão alcança 40 porcento dos casos

- Meça se a métrica de precisão alcança 40 porcento dos casos da classe C


### Requisitos de Acurácia

- Meça se a métrica de acurácia alcança 50 porcento dos casos
