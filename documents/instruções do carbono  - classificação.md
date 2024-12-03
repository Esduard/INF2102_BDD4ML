# Projeto Carbono - CLASSIFICAÇÃO

Visualize esse documento no VSCode usando o comando 'Cntrl + Shift + V'

## Descrição Do Projeto

Uma empresa de transporte de carga precisa estimar quanto de gás carbono (CO2) irá emitir em um dado trecho de viagem

Uma equipe de cientistas de dados desenvolveu um modelo de regressão que estima quanto uma viagem irá gerar de C02.

## Pré Processamento

Esse projeto possui um modulo de pré processamento customizado para adequar os dados de teste. Ele deverá ser incluido no código por meio de uma clausula BDD de pré processamento.

## Pós Processamento

Esse projeto possui um modulo de pós processamento customizado para adequar os dados de teste. Ele deverá ser incluido no código por meio de uma clausula BDD de pós processamento.

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

Com o modelo pronto e os dados de teste preparados você deve utilizar o framework BDD4ML para rodar os testes de machine learning. Se trata de um framework com clausulças pré associadas a código, basta achar as clausulas que necessita na documentação e aplica-las em um arquivo de cláusulas.

Utilize da documentação presente no arquivo `Manual_BDD4ML.md` e das referências na pasta `old_features` para prencher o arquivo de cláusulas `classification base.feature` na pasta `features`

### Recursos Dados:
Utilize:

 - O modelo `aframax_2023_model.pkl` localizado na pasta `estimators\`, atente-se a forma que ele deve ser chamado na cláusula. 
 
 - O arquivo de testes `carbon_aframax_2023.csv` localizado na pasta `test_data`

 - Utilize também os modulos de pré e pós processamento conforme instruido nos exemplos da documentação.

Todos os arquivos já estão configurados para serem utilizados, basta preencher o arquivo `.feature` com os elementos corretos.

Com seu conhecimento em aprendizado de máquina, gere cláusulas BDD que atendam aos seguintes critérios:

### Requisitos de Recall

- Meça se a métrica de revocação (recall) alcança 50 porcento dos casos 

- Meça se a métrica de revocação (recall) alcança 40 porcento dos casos da classe D


### Requisitos de Precisão

- Meça se a métrica de precisão alcança 40 porcento dos casos

- Meça se a métrica de precisão alcança 40 porcento dos casos da classe C


### Requisitos de Acurácia

- Meça se a métrica de acurácia alcança 50 porcento dos casos


## Execução

Após gerar as cláusulas, rode uma celula escrito `!behave` caso esteja usando o google colab ou rode o comando `behave` no terminal.