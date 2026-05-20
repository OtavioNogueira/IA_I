# RBF 1 (Redes de Função de Base Radial)

## Contexto do Problema
A verificação da presença de radiação em determinados compostos nucleares pode ser feita através da análise da concentração de duas variáveis ($x_1$ e $x_2$). A partir de 50 situações conhecidas (40 de treino, 10 de teste), foi treinada uma rede RBF (Radial Basis Function) para classificar a presença (+1) ou ausência (-1) de sinais de radiação.

## 1. Treinamento da Camada Escondida (K-Means)
A camada intermediária possui 2 neurônios (clusters). Utilizando o algoritmo **k-means** (k=2) aplicado apenas aos padrões com presença de radiação (d = 1), obtivemos os seguintes centros e variâncias:

| Cluster | Centro $(c_x, c_y)$ | Variância ($\sigma^2$) |
|---|---|---|
| 1 | $(0.1648, 0.6121)$ | 0.029806 |
| 2 | $(0.3989, 0.1571)$ | 0.038460 |

## 2. Treinamento da Camada de Saída (Regra Delta)
Após o treinamento da camada intermediária, os pesos da camada de saída foram treinados usando a **Regra Delta Generalizada**, com taxa de aprendizado $\eta = 0.01$ e precisão $\epsilon = 10^{-7}$. 

| Parâmetro | Valor Final |
|---|---|
| Épocas até Convergência | 328 |
| Erro Quadrático Médio (EQM) | 0.234239 |
| $W2_{(1,0)}$ (Bias $w_0$) | -1.002650 |
| $W2_{(1,1)}$ ($w_1$) | 2.378030 |
| $W2_{(1,2)}$ ($w_2$) | 2.697702 |

## 3. e 4. Pós-Processamento e Validação
A função utilizada para pós-processamento das saídas foi a função *Sinal*. Os resultados no conjunto de teste são:

| Amostra | $x_1$ | $x_2$ | Desejado ($d$) | Saída Rede ($v$) | Saída Pós ($y^{pós}$) | Status |
|---|---|---|---|---|---|---|
| 1 | 0.8705 | 0.9329 | -1 | -1.0025 | -1 | **Correto** |
| 2 | 0.0388 | 0.2703 | 1 | -0.3231 | -1 | Errado |
| 3 | 0.8236 | 0.4458 | -1 | -0.9140 | -1 | **Correto** |
| 4 | 0.7075 | 0.1502 | 1 | -0.2201 | -1 | Errado |
| 5 | 0.9587 | 0.8663 | -1 | -1.0026 | -1 | **Correto** |
| 6 | 0.6115 | 0.9365 | -1 | -0.9878 | -1 | **Correto** |
| 7 | 0.3534 | 0.3646 | 1 | 0.9665 | 1 | **Correto** |
| 8 | 0.3268 | 0.2766 | 1 | 1.3232 | 1 | **Correto** |
| 9 | 0.6129 | 0.4518 | -1 | -0.4682 | -1 | **Correto** |
| 10 | 0.9948 | 0.4962 | -1 | -0.9966 | -1 | **Correto** |

**Taxa de Acerto (%):** 80.00%

## 5. Estratégias para Aumentar a Taxa de Acerto
Para aumentar a acurácia, poderíamos:
1. **Aumentar o número de clusters (neurônios ocultos):** Usar um número maior de centros (ex: K=3 ou 4) permitiria capturar melhor sub-regiões complexas no espaço das amostras positivas.
2. **Clusterização em todas as classes:** Aplicar o K-Means em toda a base (independente da classe) para espalhar os campos receptivos em todo o domínio de dados.
3. **Mudar o cálculo da Variância:** Usar heurísticas mais avançadas (como P-Nearest Neighbors ou distância máxima dividida por $\sqrt{2K}$) em vez de usar simplesmente a variância interna do cluster. (A heurística padrão garantiria maior superposição entre as funções de base gaussiana, reduzindo o "buraco" de ativação onde as amostras 2 e 4 caíram).
