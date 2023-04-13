# Project Rossman Store Sales Forecast
Este repositório contém todos os arquivos do projeto Rossmann, onde foi realizado a previsão de vendas através de algoritmos de regressão linear.
![This is an image](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Rossmann_Logo.svg/2560px-Rossmann_Logo.svg.png)
# 1. Problema de Negócio
Rossmann é uma rede de drogaria que opera com mais de 3.000 lojas em 7 países da Europa e os respectivos gerentes de cada loja são os responsáveis por realizar a previsão de vendas das próximas 6 semanas da loja de sua responsabilidade. Com vários gerentes realizando as predições baseados em sua própria experiência e opinião, a acurácia não é a ideal para o tamanho da empresa. A proposta aqui é a que as previsões passam a ser realizadas por um algoritmo de Machine Learning para aumentar a eficácia e auxiliar o CEO nas tomadas de decisões mais assertivas.

# 2. Premissas
Para o desenvolvimento do modelo:
- Foi considerado apenas dados em que as vendas eram maior que zero
- Para lojas sem registro da distancia de competidores, foi setado o valor de 200.000, para explicitar que o competidor mais próximo está muito distante

# 3. Produto Final
Foi combinado com o CEO que iremos disponibilizar o modelo e suas previsões via bot no Telegram, onde o usuário deverá digitar o ID da loja que deverá ser realizado a previsão de vendas.

# 4. Estratégia da Solução

![This is an image](https://miro.medium.com/v2/resize:fit:640/0*tA5OjppLK627FfFo)

A solução seguirá as etapas do framework CRISP-DM, que é composta por seis fases sequenciais e de modo ciclico: 
  1. Entendimento do problema de negócios
  2. Entendimento dos dados disponíveis
  3. Preparação dos dados
  4. Modelagem de dados
  5. Avaliação do modelo
  6. Deploy do modelo 


# 5. Modelos de Machine Learning
  No primeiro ciclo do CRISP foi testado 5 algoritmos com o objetivo de encontrar o modelo com a melhor performance ao mesmo tempo em que o custo de sua implantação estivesse dentro do budget disponível.
  Após os testes foram obtidos os seguintes resultados para cada modelo:
  
  | Modelo | MAE | MAPE | RMSE |
  | ------ | ------ | ------ | ------ |
  | Random Forest Regressor | 678.390540 | 0.099811 | 1008.885714 |
  | Average Model	 | 1354.800353 | 0.455051 | 1835.135542 |
  | Linear Regression	 | 1867.089774 | 0.292694 | 2671.049215 |
  | Linear Regression - Lasso | 1891.704881 | 0.289106 | 2744.451737 |
  | XGBoost Regressor	 | 6683.424265 | 0.949437 | 7330.711283 |
  
# 6. Modelo Final e Performance
Para escolha do modelo final foi escolhido o XGBoost Regressor, que a primeiro momento foi o que teve o pior desempenho, porém após a realização do Fine Tunning ele teve um dos melhores desempenhos, porém era o único em estava dentro do budget da empresa (0 dólares) e conseguiriamos hospedar na cloud Heroku sem custos adicionais. Por esse motivo que ele foi escolhido como modelo final.

| Modelo | MAE | MAPE | RMSE |
| ------ | ------ | ------ | ------ |
|XGBoost Regressor|	640.831331|	0.093136|	939.816872|

# 7. Resultados de Negócios
Falando o idioma de negócios, a previsão para as próximas 6 semanas obtida pelo modelo para a rede Rossmann foi de:

 | Cenário | Previsão |
  | ------ | ------ |
  | Previsto | R$283.544.192,00 |
  | Melhor Cenário | R$282.825.717,05 |
  | Pior Cenário | R$284.262.719,46 |
  
 Também é possível realizar a previsão por loja, auxiliando em uma estratégia personalizada. Veja algumas previsões abaixo:
  
  | Loja | Pior Cenário | Previsão | Melhor Cenário | 
  | ------ | ------ | ------ | ------ |
  |292 | 101.569,20 |104.893,86 | 108.218,53|
  |909 | 229.289,83 |236.826,75 | 244.363,66|
  |876 | 196.197,60 |200.245,46 | 204.293,32|
  |595 | 371.519,77 |375.669,59 | 379.819,41|
  |274 | 195.766,71 |197.075,92 | 198.385,13|
  
  ![This is an image](https://i.imgur.com/3M9qd3P.png)
  
  # 8. Entregando o Produto Final - Bot no Telegram
  Como prometido ao CEO, agora ele e toda a equipe conseguem acessar os resultados via Telegram, basta enviar o ID da loja. Para ter acesso ao bot basta clicar no botão:
  
<a href="https://t.me/ds_rossmann_model_bot"> 
  <img src="https://img.shields.io/badge/-Telegram-blue?style=flat-square&logo=Telegram&logoColor=white" alt="Bot no Telegram">
</a>  

Imagem do funcionamento do bot:

  <img src="https://i.imgur.com/0IWUfXk.jpg" width="246" height="533">
