# Projeto Prevenção de Acidentes - Versão 1

## Descrição Do Projeto

Uma empresa de rede elétrica realiza manutenções frequentes em sua infraestrutura e precisa estimar a probabilidade de um acidente ocorrer em uma operação.

Uma equipe de cientistas de dados desenvolveu um modelo de classificação que estima se um acidente irá ocorrer baseado nos seguintes campos:

## Estrutura dos Campos de entrada do Modelo

### Campo: "hh_total"
- **Descrição**: Total de Homem-Hora (HH) executado em todas as operações e atividades de manutenção.

### Campo: "hh_de_deslocamento"
- **Descrição**: Quantidade de Homem-Hora utilizada em deslocamento para a execução das atividades de manutenção.

### Campo: "hh_de_preparo"
- **Descrição**: Quantidade de Homem-Hora dedicada ao preparo para iniciar as atividades de manutenção.

### Campo: "hh_de_servico"
- **Descrição**: Quantidade de Homem-Hora efetivamente aplicada na realização do serviço de manutenção.

### Campo: "hh_de_supervisao"
- **Descrição**: Quantidade de Homem-Hora utilizada para supervisão das atividades de manutenção.

### Campo: "hh_de_outros"
- **Descrição**: Quantidade de Homem-Hora para atividades diversas que não se enquadram nas demais categorias.

### Campo: "hh_de_laboratorio"
- **Descrição**: Quantidade de Homem-Hora dedicada a atividades realizadas em laboratório, como análises e testes.

### Campo: "hh_de_PREVENTIVA PERIÓDICA"
- **Descrição**: Quantidade de Homem-Hora aplicada em atividades de manutenção preventiva periódica.

### Campo: "hh_de_outros_de_denominacao_tam"
- **Descrição**: Quantidade de Homem-Hora para outras atividades de denominação específica, de acordo com o tipo de operação.

### Campo: "hh_de_INSPEÇÃO PERIÓDICA"
- **Descrição**: Quantidade de Homem-Hora utilizada em atividades de inspeção periódica de equipamentos ou instalações.

### Campo: "hh_de_COMISSIONAMENTO"
- **Descrição**: Quantidade de Homem-Hora aplicada em atividades de comissionamento, ou seja, preparação e verificação antes do uso efetivo.

### Campo: "hh_de_REPARO DE DEFEITO"
- **Descrição**: Quantidade de Homem-Hora dedicada ao reparo de defeitos identificados em equipamentos ou instalações.

### Campo: "hh_de_Análise cromatográfica óleo"
- **Descrição**: Quantidade de Homem-Hora para análises cromatográficas de óleo como parte das atividades de manutenção.

### Campo: "hh_de_REPARO DEFEITO"
- **Descrição**: Quantidade de Homem-Hora para atividades de reparo de defeito. Similar ao campo anterior, com possível diferença em denominação.

### Campo: "hh_de_Análise físico-química de óleo"
- **Descrição**: Quantidade de Homem-Hora para análise físico-química do óleo durante a manutenção.

### Campo: "hh_de_Corrente de fuga"
- **Descrição**: Quantidade de Homem-Hora dedicada à análise de corrente de fuga em componentes elétricos.

### Campo: "hh_de_Termovisionamento"
- **Descrição**: Quantidade de Homem-Hora aplicada para inspeções por termovisão (termografia) para identificar problemas de aquecimento.

### Campo: "hh_de_Avaliação qualitativa"
- **Descrição**: Quantidade de Homem-Hora utilizada em avaliações qualitativas dos equipamentos ou processos.

### Campo: "weather_code"
- **Descrição**: Código meteorológico que representa as condições climáticas gerais no local de operação.

### Campo: "temperature_2m_max"
- **Descrição**: Temperatura máxima registrada a 2 metros de altura no local de operação.

### Campo: "temperature_2m_min"
- **Descrição**: Temperatura mínima registrada a 2 metros de altura no local de operação.

### Campo: "apparent_temperature_max"
- **Descrição**: Temperatura aparente máxima, considerando fatores de sensação térmica e umidade.

### Campo: "apparent_temperature_min"
- **Descrição**: Temperatura aparente mínima, considerando sensação térmica e umidade.

### Campo: "precipitation_sum"
- **Descrição**: Soma total de precipitação (chuva) registrada durante o período de operação.

### Campo: "precipitation_hours"
- **Descrição**: Quantidade de horas em que houve precipitação durante as operações.

### Campo: "wind_speed_10m_max"
- **Descrição**: Velocidade máxima do vento registrada a 10 metros de altura no local de operação.

### Campo: "wind_gusts_10m_max"
- **Descrição**: Velocidade máxima das rajadas de vento registradas a 10 metros de altura.

### Campo: "et0_fao_evapotranspiration"
- **Descrição**: Taxa de evapotranspiração de referência, indicando a perda de água para a atmosfera, calculada segundo o método FAO.


## Objetivo

Com o modelo pronto e os casos de teste preparados você deve gerar clausulas BDD em texto livre para informar seus superiores sobre o desempenho do modelo em termos de classificar os acidentes corretamente. Tenha em mente que sua audicencia não tem conhecimento de métricas de classificação então você deverá gerar clausulas que, além de mostrar os resultados das metricas, as expliquem diretamente.

Este desafio consiste em gerar cláusulas BDD __Em Inglês__ para analisar o desempenho desse modelo classificando se as ocorrencias terão ou não acidentes.

Com seu conhecimento em aprendizado de máquina, gere cláusulas BDD que atendam aos seguintes critérios:

### Requisitos de Recall

- Meça se a métrica de revocação (recall) alcança 10 porcento dos casos 

- Meça se a métrica de revocação (recall) alcança 40 porcento dos casos da classe 'True'


### Requisitos de Precisão

- Meça se a métrica de precisão alcança 10 porcento em todos os casos usando uma média macro


### Requisitos de Acurácia

- Meça se a métrica de acurácia alcança 10 porcento em todos os casos
