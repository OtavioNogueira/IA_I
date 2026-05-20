# PMC 2

## Contexto do Problema (Processamento de Bebidas)
Nesta atividade, a rede Perceptron Multicamadas (PMC) foi utilizada para classificar o tipo de conservante (A, B ou C) a ser aplicado em bebidas, baseado em 4 variáveis reais (Teor de Água, Grau de Acidez, Temperatura e Tensão Superficial).
A topologia tem 4 neurônios de entrada, 15 neurônios na camada oculta, e 3 neurônios de saída, com codificação *one-hot* para a classe.
O objetivo foi comparar o algoritmo de **Backpropagation Padrão** com o **Backpropagation com Momentum** (fator = 0.9), ambos partindo dos mesmos pesos iniciais e $\eta = 0.1$.

## 1 e 2. Padrão vs Momentum
Resultados de convergência para a precisão de $10^{-6}$ e o respectivo tempo de processamento.

| Algoritmo | Épocas | Tempo de Processamento (s) | EQM Final |
|---|---|---|---|
| Backpropagation Padrão | 966 | 15.14 s | 0.017528 |
| Backpropagation com Momentum | 314 | 5.23 s | 0.018759 |

## Gráficos de EQM vs Épocas
Comparativo da evolução do Erro Quadrático Médio. *(Gráfico salvo como `grafico_eqm_pmc2.png` nesta pasta).*

**Análise de Desempenho**
A inserção do termo de *Momentum* na regra de atualização dos pesos acelera dramaticamente o treinamento (reduzindo em quase 7 vezes o número de épocas e o tempo de execução neste caso). Ele atua como um filtro passa-baixa estabilizando a trajetória do gradiente, evitando que a rede fique presa em mínimos locais rasos ou oscile excessivamente em desfiladeiros da superfície de erro.

## 3 e 4. Validação e Pós-Processamento
Aplicando o critério de arredondamento simétrico (pos-processamento), a rede foi exposta a 18 amostras de teste inéditas. 
**Taxa de Acerto Global: 100.00%**
