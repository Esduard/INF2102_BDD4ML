# Projeto Carbono - REGRESSÃO

Visualize esse documento no VSCode usando o comando 'Cntrl + Shift + V'

## Descrição Do Projeto

Uma empresa de transporte de carga precisa estimar quanto de gás carbono (CO2) irá emitir em um dado trecho de viagem

Uma equipe de cientistas de dados desenvolveu um modelo de regressão que estima quanto uma viagem irá gerar de C02.

## Pré Processamento

Esse projeto possui um modulo de pré processamento customizado para adequar os dados de teste. Ele deverá ser incluido no código por meio de uma clausula BDD de pré processamento.

## Transformação de Regressão para Classificação


## Objetivo

Com o modelo pronto e os dados de teste preparados você deve utilizar o framework BDD4ML para rodar os testes de machine learning. Se trata de um framework com clausulças pré associadas a código, basta achar as clausulas que necessita na documentação e aplica-las em um arquivo de cláusulas `.feature`.

Utilize da documentação presente no arquivo `Manual_BDD4ML.md` e das referências na pasta `old_features` para prencher o arquivo de cláusulas `regression base.feature` na pasta `features`

### Recursos Dados:
Utilize:

 - O modelo `aframax_2023_model.pkl` localizado na pasta `estimators\`, atente-se a forma que ele deve ser chamado na cláusula. 
 
 - O arquivo de testes `carbon_aframax_2023.csv` localizado na pasta `test_data`

Utilize também o modulos de pré processamento conforme instruido no exemplo da documentação

Todos os arquivos já estão configurados para serem utilizados, basta preencher o arquivo `.feature` com os elementos corretos.

Com seu conhecimento em aprendizado de máquina, gere cláusulas BDD que atendam aos seguintes critérios:

### Requisitos de MSE

- Meça se a métrica de Mean Squared Error alcança um valor inferior a 200000

### Requisitos de R2 score

- Meça se a métrica de R2 score alcança um valor superior a 0.2

### Requisitos de MAE

- Meça se a métrica de Mean Absolute Error alcança um valor abaixo de 200

### Requisitos de RMSE

- Meça se a métrica de Root Mean Squared Error alcança um valor abaixo de 425

### Requisitos de Median Absolute Error

- Meça se a métrica de Median Absolute Error alcança um valor abaixo de 90

## Execução

Após gerar as cláusulas, rode uma celula escrito `!behave` caso esteja usando o google colab ou rode o comando `behave` no terminal.