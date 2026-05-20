# ADALINE

## Contexto do Problema (Ajuste de Válvulas)
Um sistema envia um sinal codificado de 4 grandezas {x1, x2, x3, x4} para ajustar duas válvulas (A ou B). Durante a transmissão, os sinais sofrem interferências (ruídos). Uma rede **ADALINE** foi treinada com dados ruidosos para classificar se o sinal deve ir para a válvula A (-1) ou B (+1).
Utilizou-se a **Regra Delta**, com taxa de aprendizado $\eta = 0.0025$, precisão de $10^{-6}$, e 5 inicializações aleatórias de pesos.

## 1 e 2. Treinamentos Realizados
Foram executados 5 treinamentos rastreando os pesos iniciais, os pesos finais ao atingir a convergência do Erro Quadrático Médio (EQM) menor que a precisão, e o total de épocas.

| Treino | $w_{0_{in}}$ | $w_{1_{in}}$ | $w_{2_{in}}$ | $w_{3_{in}}$ | $w_{4_{in}}$ | $w_{0_{fin}}$ | $w_{1_{fin}}$ | $w_{2_{fin}}$ | $w_{3_{fin}}$ | $w_{4_{fin}}$ | Épocas |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1º (T1) | 0.1344 | 0.8474 | 0.7638 | 0.2551 | 0.4954 | 1.8131 | 1.3128 | 1.6423 | -0.4277 | -1.1778 | 851 |
| 2º (T2) | 0.9560 | 0.9478 | 0.0566 | 0.0849 | 0.8355 | 1.8131 | 1.3127 | 1.6421 | -0.4281 | -1.1777 | 818 |
| 3º (T3) | 0.2380 | 0.5442 | 0.3700 | 0.6039 | 0.6257 | 1.8131 | 1.3129 | 1.6423 | -0.4277 | -1.1778 | 878 |
| 4º (T4) | 0.2360 | 0.1032 | 0.3961 | 0.1550 | 0.0665 | 1.8131 | 1.3128 | 1.6422 | -0.4279 | -1.1777 | 849 |
| 5º (T5) | 0.6229 | 0.7418 | 0.7952 | 0.9425 | 0.7399 | 1.8131 | 1.3129 | 1.6424 | -0.4276 | -1.1778 | 857 |

## 3. Gráfico do EQM em função da Época
Gráfico dos valores de Erro Quadrático Médio (EQM) ao longo do treinamento para os dois primeiros cenários (T1 e T2).
*(O gráfico foi gerado e salvo como `grafico_eqm.png` nesta mesma pasta).*

## 4. Classificação das Amostras
Resultados da classificação das 15 novas amostras ruidosas por cada treinamento (Válvula A = -1, Válvula B = +1).

| Amostra | y(T1) a y(T5) | Resultado |
|---|---|---|
| 1 a 2 | -1 | Válvula A |
| 3 | +1 | Válvula B |
| 4 a 5 | -1 | Válvula A |
| 6 a 9 | +1 | Válvula B |
| 10 a 11 | -1 | Válvula A |
| 12 | +1 | Válvula B |
| 13 a 14 | -1 | Válvula A |
| 15 | +1 | Válvula B |

## 5. Comportamento da Convergência
**Por que o número de épocas é diferente, mas os pesos convergem para os mesmos valores?**
Ao contrário do Perceptron (que possui múltiplos planos de separação válidos quando os dados são linearmente separáveis), o modelo ADALINE busca minimizar o Erro Quadrático Médio (EQM) contínuo. 
Como a função de custo (EQM) para uma rede com saída linear é uma superfície quadrática estritamente convexa (um paraboloide multidimensional), ela possui um **único ponto de mínimo global**. 
Portanto, não importa de onde o algoritmo comece (pesos iniciais aleatórios), a Regra Delta orientada pelo gradiente sempre "deslizará" a curva em direção ao fundo desse mesmo "poço". O número de épocas varia porque a distância do ponto de partida até esse fundo muda, mas o ponto de destino final (os pesos ótimos) é matematicamente o mesmo.
