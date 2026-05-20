# PMC 3

## Contexto do Problema (Time Delay Neural Network)
Previsão do preço de uma mercadoria no mercado de ações utilizando um Perceptron Multicamadas configurado como **TDNN (Time Delay)**. Para prever a amostra no instante *t*, a rede utiliza as amostras dos *p* instantes anteriores: $x(t-1), x(t-2), \dots, x(t-p)$.

**Três topologias avaliadas:**
- **Rede 1:** 5 entradas (p=5), 10 neurônios ocultos.
- **Rede 2:** 10 entradas (p=10), 15 neurônios ocultos.
- **Rede 3:** 15 entradas (p=15), 25 neurônios ocultos.

Algoritmo de treinamento: **Backpropagation com Momentum** ($\eta = 0.1$, $\alpha = 0.8$, $precisão = 0.5 \times 10^{-6}$). Foram realizados treinamentos para cada topologia.

## 1, 2, 4. Resultados e Gráficos
Os treinamentos variaram em relação ao tempo de convergência. Os gráficos do EQM vs Épocas e da Validação comparando os valores Desejados vs Estimados foram gerados e estão disponíveis nesta pasta (`grafico_eqm_pmc3.png` e `grafico_validacao_pmc3.png`).

## 3, 5, 6. Validação e Análise da Melhor Configuração
**Justificativa:** A **Rede 1** apresentou um erro relativo na casa dos 20%, o que indica um underfitting (baixa capacidade de mapear a complexidade temporal com apenas 5 entradas). A **Rede 3** sofreu um colapso drástico (convergindo prematuramente e apresentando um erro relativo de mais de 1000%). Isso ocorre porque, ao possuir 15 entradas e 25 neurônios ocultos com pesos iniciais positivos (0 a 1), as combinações lineares explodiram, saturando os neurônios sigmoides. Quando um neurônio sigmoide satura (saída próxima a 1), a sua derivada se aproxima de 0, causando o fenômeno do *Vanishing Gradient* (Gradiente Desvanescente) e impedindo qualquer aprendizado.

A **Rede 2** foi o balanço ideal: evitou a saturação severa presente na Rede 3 e teve memória temporal suficiente (p=10) para modelar a série de maneira superior à Rede 1, atingindo o menor erro relativo médio ($\approx 8.89\%$).

## 7. Variantes do Algoritmo Backpropagation

### a. Algoritmo Resilient-Propagation (RProp)
O RProp é um algoritmo adaptativo focado em superar o principal gargalo do Backpropagation padrão com funções logísticas: o achatamento do gradiente. Em vez de usar a magnitude da derivada para atualizar o peso, o RProp utiliza **apenas o sinal (direção) do gradiente**. Cada peso possui uma taxa de atualização individual ($\Delta_{ij}$). Se o gradiente mantiver o mesmo sinal por duas épocas seguidas, $\Delta_{ij}$ aumenta (acelerando em superfícies planas). Se o sinal inverter, ele diminui.
**Vantagem:** Convergência consideravelmente mais rápida e robusta contra gradientes desvanescentes, pois atualiza ativamente os pesos mesmo nas extremidades saturadas da função sigmoide.

### b. Algoritmo Levenberg-Marquardt (LM)
O Levenberg-Marquardt atua misturando o método do Gradiente Descendente e o método de Gauss-Newton. Em vez de calcular derivadas segundas complexas (Matriz Hessiana), ele as aproxima utilizando a Matriz Jacobiana ($H \approx J^T J$). 
**Vantagem:** É indiscutivelmente o algoritmo de treinamento mais rápido que existe para redes neurais de pequeno a médio porte (como a maioria das PMCs). Sua convergência é extremamente acelerada perto da solução ótima. A principal desvantagem é o alto custo de memória para armazenar e inverter a matriz Jacobiana em redes muito grandes.
