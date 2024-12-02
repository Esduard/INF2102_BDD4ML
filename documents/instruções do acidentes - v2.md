# Projeto Prevenção de Acidentes - Versão 1

Visualize esse documento no VSCode usando o comando 'Cntrl + Shift + V'

## Descrição Do Projeto

Uma empresa de rede elétrica realiza manutenções frequentes em sua infraestrutura e precisa estimar a probabilidade de um acidente ocorrer em uma operação.

Uma equipe de cientistas de dados desenvolveu um modelo de classificação que estima se um acidente irá ocorrer.


## Objetivo

Com o modelo pronto e os dados de teste preparados você deve utilizar o framework BDD4ML para rodar os testes de machine learning. Se trata de um framework com clausulças pré associadas a código, basta achar as clausulas que necessita na documentação e aplicalas em um arquivo de cláusulas.

Utilize da documentação presente no arquivo 'manual_BDD.md' e das referências na pasta 'old_features' para criar os arquivos de cláusulas. Crie os arquivos na pasta 'features' com a extensão ".feature"

Utilize: 
 - O modelo `acidentes_model.pkl` localizado na pasta `estimators\`, atente-se a forma que ele deve ser chamado na cláusula. 
 
 - O arquivo de testes `dataset_acidentes.csv` localizado na pasta `test_data\`

Com seu conhecimento em aprendizado de máquina, gere cláusulas BDD que atendam aos seguintes critérios:

### Requisitos de Recall

- Meça se a métrica de revocação (recall) alcança 10 porcento dos casos 

- Meça se a métrica de revocação (recall) alcança 10 porcento dos casos da classe 'True'


### Requisitos de Precisão

- Meça se a métrica de precisão alcança 10 porcento em todos os casos


### Requisitos de Acurácia

- Meça se a métrica de acurácia alcança 10 porcento em todos os casos


## Execução

Após gerar as cláusulas, rode uma celula escrito `!behave` caso esteja usando o google colab ou rode o comando `behave` no terminal.