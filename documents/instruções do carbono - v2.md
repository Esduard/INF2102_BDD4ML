# Projeto Carbono  - Versão 2

## Descrição Do Projeto

Uma empresa de transporte de carga precisa estimar quanto de gás carbono (CO2) irá emitir em um dado trecho de viagem

Uma equipe de cientistas de dados desenvolveu um modelo de regressão que estima quanto uma viagem irá gerar de C02 baseado nos seguintes campos:

## Estrutura dos Campos de entrada do Modelo

### Campo: "distance"
- **Descrição**: Distância do trecho em quilômetros.

### Campo: "dwt",
- **Descrição**: Capacidade do navio.

### Campo: "harbor_time",
- **Descrição**: Tempo gasto atracado em porto em um trecho.

### Campo: "fo_per_distance",
- **Descrição**: Consumo de fo por milha nautica.

### Campo: "PETROLEIRO",
- **Descrição**: Booleano informando se o navio é do tipo 'petroleiro'

### Campo: "is_platform",
- **Descrição**: Booleano informando se a viagem é para uma plataforma

### Campo: "Cabotagem",
- **Descrição**: Booleano informando se é viagem de cabotagem

### Campo: "Exportação",
- **Descrição**: Booleano informando se é viagem de exportação

### Campo: "Importação",
- **Descrição**: Booleano informando se é viagem de importação

### Campo: "Internacional",
- **Descrição**: Booleano informando se é viagem de internacional

### Campo: "distance_restricted",
- **Descrição**: Distância navegada em area restrita em um trecho

## Estrutura do campo de saída

### Campo: "co2_with_exclusions"
- **Descrição**: Emissões de co2 com exclusões

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

Com o modelo pronto e os dados de teste preparados você deve utilizar o framework BDD4ML para rodar os testes de machine learning. Utilize da documentação presente no arquivo 'manual_BDD.md' e das referências na pasta 'old_features' para criar os arquivos de cláusulas. Crie os arquivos na pasta 'features' com a extensão ".feature"

Utilize o modelo 'aframax_2023' localizado na pasta 'estimators' e o arquivo de testes 'carbon_aframax_2023' localizado na pasta 'test_data'

Com seu conhecimento em aprendizado de máquina, gere cláusulas BDD que atendam aos seguintes critérios:

### Requisitos de Recall

- Meça se a métrica de revocação (recall) alcança 50 porcento dos casos

- Meça se a métrica de revocação (recall) alcança 40 porcento dos casos da classe D

- Meça se a métrica de revocação (recall) alcança 40 porcento dos casos da classe E


### Requisitos de Precisão

- Meça se a métrica de precisão alcança 40 porcento dos casos da classe C

- Meça se a métrica de precisão alcança 40 porcento em todos os casos usando uma média macro


### Requisitos de Acurácia

- Meça se a métrica de acurácia alcança 50 porcento na classe A

- Meça se a métrica de acurácia alcança 50 porcento em todos os casos
