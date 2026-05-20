# PMC 1

## Contexto do Problema (Ressonância Magnética)
Estimar a energia absorvida (y) a partir de três grandezas (x1, x2, x3) para um processador de imagens de ressonância magnética utilizando um **Perceptron Multicamadas (PMC)**. 
Topologia utilizada: 3 entradas, 5 neurônios na camada oculta, 1 neurônio na camada de saída. Função de ativação logística em todas as camadas, $\eta = 0.1$, e precisão de $10^{-6}$.

## 1 e 2. Treinamentos Realizados
Foram executados 5 treinamentos com pesos iniciais aleatórios. Abaixo estão os resultados de erro e épocas.

| Treinamento | Erro Quadrático Médio | Número de Épocas |
|---|---|---|
| 1º (T1) | 0.001645 | 153 |
| 2º (T2) | 0.001714 | 182 |
| 3º (T3) | 0.001708 | 176 |
| 4º (T4) | 0.001654 | 157 |
| 5º (T5) | 0.001637 | 151 |

## 3. Gráfico do EQM em Função da Época (Piores Casos)
Gráfico dos valores de EQM ao longo do treinamento para os dois casos que exigiram mais épocas para convergir (T2 e T3).
*(O gráfico foi gerado e salvo como `grafico_eqm_pmc1.png` nesta mesma pasta).*

## 4. Análise de Variação
**Por que o EQM e o número de épocas variam entre os treinamentos?**
A variação decorre da **inicialização aleatória dos pesos sinápticos**. Diferente do modelo ADALINE de camada única, cuja superfície de erro é convexa (possuindo apenas um mínimo global), as redes Perceptron Multicamadas (PMC) formam uma superfície de erro complexa, cheia de vales, planaltos e múltiplos **mínimos locais**.
Dependendo do ponto de partida (pesos iniciais), o algoritmo de *backpropagation* (descida do gradiente) percorre um caminho diferente através desse espaço de peso, atingindo diferentes pontos de convergência na superfície de erro, resultando em diferentes valores de EQM final e exigindo um número distinto de épocas para satisfazer o critério de parada.

## 5 e 6. Validação com Conjunto de Teste
Os 5 modelos foram avaliados em 20 amostras de teste não vistas no treinamento. O Erro Relativo (%) e a Variância foram calculados em relação à saída desejada (d). O erro relativo médio girou em torno de 1.5% a 2.2%.

**6. Configuração Mais Adequada**
A configuração mais adequada é o **Treinamento 1 (T1)**. Embora o T5 tenha convergido em menos épocas durante o treinamento, o **T1** apresentou o **menor Erro Relativo Médio (1.5233%)** quando exposto a dados inéditos (conjunto de teste), demonstrando a melhor capacidade de **generalização** para o sistema de ressonância magnética.
