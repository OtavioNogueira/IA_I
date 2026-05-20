# Perceptron

## Contexto do Problema
A partir da análise de um processo de destilação fracionada de petróleo observou-se que determinado óleo poderia ser classificado em duas classes de pureza {C1 e C2} a partir da medição de três grandezas {x1, x2 e x3} que representam propriedades físico-químicas.
A classificação é feita com um **Perceptron** usando a regra de Hebb (aprendizado supervisionado) com taxa de aprendizagem $\eta = 0.01$, inicializando os pesos com valores aleatórios entre 0 e 1.

## 1 e 2. Treinamentos Realizados
Foram executados 5 treinamentos independentes até o erro chegar a zero na base de dados de treinamento. Em cada execução, os pesos iniciais foram gerados aleatoriamente entre 0 e 1.

| Treinamento | Épocas | Bias ($w_0$) | $w_1$ | $w_2$ | $w_3$ |
|---|---|---|---|---|---|
| T1 | 401 | 3.0962 | 1.5763 | 2.5009 | -0.7385 |
| T2 | 386 | 3.1050 | 1.5580 | 2.4874 | -0.7390 |
| T3 | 424 | 3.1365 | 1.6047 | 2.5198 | -0.7464 |
| T4 | 358 | 3.0413 | 1.5454 | 2.4485 | -0.7256 |
| T5 | 327 | 2.9099 | 1.4042 | 2.4142 | -0.6965 |

## 3. Classificação das Novas Amostras
O perceptron treinado foi aplicado nas novas amostras (dados de teste). Como as 5 execuções convergiram corretamente para um plano de separação global equivalente, a classificação resultante é idêntica em todos os modelos.

| Amostra | x1 | x2 | x3 | y(T1) | y(T2) | y(T3) | y(T4) | y(T5) |
|---|---|---|---|---|---|---|---|---|
| 1 | -0.3565 | 0.0620 | 5.9891 | -1 (C1) | -1 | -1 | -1 | -1 |
| 2 | -0.7842 | 1.1267 | 5.5912 | 1 (C2) | 1 | 1 | 1 | 1 |
| 3 | 0.3012 | 0.5611 | 5.8234 | 1 (C2) | 1 | 1 | 1 | 1 |
| 4 | 0.7757 | 1.0648 | 8.0677 | 1 (C2) | 1 | 1 | 1 | 1 |
| 5 | 0.1570 | 0.8028 | 6.3040 | 1 (C2) | 1 | 1 | 1 | 1 |
| 6 | -0.7014 | 1.0316 | 3.6005 | 1 (C2) | 1 | 1 | 1 | 1 |
| 7 | 0.3748 | 0.1536 | 6.1537 | -1 (C1) | -1 | -1 | -1 | -1 |
| 8 | -0.6920 | 0.9404 | 4.4058 | 1 (C2) | 1 | 1 | 1 | 1 |
| 9 | -1.3970 | 0.7141 | 4.9263 | -1 (C1) | -1 | -1 | -1 | -1 |
| 10 | -1.8842 | -0.2805 | 1.2548 | -1 (C1) | -1 | -1 | -1 | -1 |

## 4 e 5. Questões Teóricas

**4. Explique por que o número de épocas de treinamento varia a cada vez que executamos o treinamento.**
O algoritmo do Perceptron realiza uma busca no espaço para encontrar um "hiperplano" (uma reta/plano no espaço vetorial) que consiga separar perfeitamente as classes C1 e C2. 
O tempo que ele leva para encontrar esse plano depende unicamente de onde ele começou a busca. Como inicializamos o vetor de pesos com valores aleatórios diferentes a cada execução, o ponto de partida muda. Isso faz com que a trajetória de ajustes e a quantidade de passos (épocas) até o erro zerar variem significativamente.

**5. Qual a principal limitação do perceptron quando aplicado em problemas de classificação?**
A principal limitação do Perceptron clássico (de camada única) é que ele **só consegue resolver problemas que sejam linearmente separáveis**.
Isso significa que ele só terá sucesso se for possível traçar um limite reto (uma reta no plano 2D, ou um hiperplano em n-dimensões) dividindo as duas classes sem sobreposição. Se os dados possuírem uma distribuição não-linear (como no famoso problema lógico do XOR), o perceptron entrará em um loop infinito, ajustando os pesos sem parar, pois nunca conseguirá alcançar o erro igual a zero.
