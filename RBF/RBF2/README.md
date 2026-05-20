# RBF 2 (Aproximação Funcional)

## Contexto do Problema
O problema propõe o mapeamento não-linear da quantidade de gasolina ($y$) a ser injetada em um motor automotivo com base em 3 variáveis ($x_1, x_2, x_3$). Esse processo de aproximação funcional será realizado comparando o desempenho de três topologias de Redes de Função de Base Radial (RBF):
- **Rede 1:** $N_1 = 5$ neurônios ocultos
- **Rede 2:** $N_1 = 10$ neurônios ocultos
- **Rede 3:** $N_1 = 15$ neurônios ocultos

## 1 e 2. Treinamentos Realizados
Foram executados 3 treinamentos independentes para cada topologia, inicializando os pesos aleatoriamente entre 0 e 1. A taxa de aprendizado adotada foi $\eta = 0.01$ com precisão de $\epsilon = 10^{-7}$. 

Como o treinamento da camada de saída (Regra Delta num neurônio linear) é um problema de otimização estritamente convexo, os três treinamentos (T1, T2, T3) convergiram para o mesmo mínimo global de erro, independentemente dos pesos iniciais.

| Treinamento | Rede 1 ($N_1=5$) | | Rede 2 ($N_1=10$) | | Rede 3 ($N_1=15$) | |
|---|---|---|---|---|---|---|
| | **EQM** | **Épocas** | **EQM** | **Épocas** | **EQM** | **Épocas** |
| 1º (T1) | 0.074238 | 329 | 0.071728 | 456 | 0.070368 | 859 |
| 2º (T2) | 0.074238 | 316 | 0.071728 | 558 | 0.070368 | 837 |
| 3º (T3) | 0.074238 | 294 | 0.071728 | 541 | 0.070368 | 895 |

## 3. Validação (Conjunto de Teste)
As redes treinadas foram aplicadas no conjunto de teste de 15 amostras. Os resultados dos três treinamentos (T1, T2, T3) para uma mesma topologia foram essencialmente os mesmos.

| Amostra | $x_1$ | $x_2$ | $x_3$ | Desejado ($d$) | $y$ Rede 1 | $y$ Rede 2 | $y$ Rede 3 |
|---|---|---|---|---|---|---|---|
| 01 | 0.5102 | 0.7464 | 0.0860 | 0.5965 | 0.4607 | 0.4132 | 0.4416 |
| 02 | 0.8401 | 0.4490 | 0.2719 | 0.6790 | 0.4637 | 0.4142 | 0.4407 |
| 03 | 0.1283 | 0.1882 | 0.7253 | 0.4662 | 0.4576 | 0.4122 | 0.4424 |
| 04 | 0.2299 | 0.1524 | 0.7353 | 0.5012 | 0.4584 | 0.4125 | 0.4422 |
| 05 | 0.3209 | 0.6229 | 0.5233 | 0.6810 | 0.4592 | 0.4128 | 0.4419 |
| 06 | 0.8203 | 0.0682 | 0.4260 | 0.5643 | 0.4635 | 0.4141 | 0.4408 |
| 07 | 0.3471 | 0.8889 | 0.1564 | 0.5875 | 0.4593 | 0.4128 | 0.4419 |
| 08 | 0.5762 | 0.8292 | 0.4116 | 0.7853 | 0.4613 | 0.4134 | 0.4414 |
| 09 | 0.9053 | 0.6245 | 0.5264 | 0.8506 | 0.4643 | 0.4145 | 0.4406 |
| 10 | 0.8149 | 0.0396 | 0.6227 | 0.6165 | 0.4635 | 0.4141 | 0.4408 |
| 11 | 0.1016 | 0.6382 | 0.3173 | 0.4957 | 0.4573 | 0.4122 | 0.4424 |
| 12 | 0.9108 | 0.2139 | 0.4641 | 0.6625 | 0.4644 | 0.4145 | 0.4406 |
| 13 | 0.2245 | 0.0971 | 0.6136 | 0.4402 | 0.4583 | 0.4125 | 0.4422 |
| 14 | 0.6423 | 0.3229 | 0.8567 | 0.7663 | 0.4619 | 0.4136 | 0.4412 |
| 15 | 0.5252 | 0.6529 | 0.5729 | 0.7893 | 0.4609 | 0.4133 | 0.4415 |

| Métrica | Rede 1 ($N_1=5$) | Rede 2 ($N_1=10$) | Rede 3 ($N_1=15$) |
|---|---|---|---|
| **Erro Relativo Médio** | 24.78% | 32.03% | 27.43% |
| **Variância (Erro)** | 193.71% | 181.99% | 209.70% |

## 4. Gráfico EQM x Épocas
O comportamento do decaimento do Erro Quadrático Médio ao longo das épocas para as três topologias foi gerado em `RBF2_EQM.png`. Observa-se que topologias maiores atingem um erro final de treinamento ligeiramente menor, mas necessitam de mais épocas para convergir (EQM achatado no fim).

## 5. Análise da Melhor Topologia
Baseado nas evidências empíricas acima, a **Rede 1 (com $N_1 = 5$) é a mais adequada para este problema**.

* **Justificativa:** Apesar da Rede 3 ter obtido o menor Erro Quadrático Médio no treinamento (0.0703 contra 0.0742 da Rede 1), quando submetida ao conjunto de validação cego, a Rede 1 superou as demais com o menor Erro Relativo Médio (24.78%). 
* Esse cenário indica que ao aumentar $N_1$ para 10 ou 15, a rede começa a sofrer de **overfitting** (superajuste), memorizando as flutuações irrelevantes (ruído) do conjunto de treinamento e perdendo sua capacidade de generalização. Portanto, 5 gaussianas são suficientes para mapear a complexidade latente das 3 variáveis de entrada sem sobreajustar os dados.
