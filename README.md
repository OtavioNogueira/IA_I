# Atividade: Redes Neurais - Classificação com Perceptron

Este repositório contém a resolução da atividade sobre a aplicação de um modelo Perceptron para a classificação de duas classes de pureza ($C_1$ e $C_2$) obtidas através da destilação fracionada de petróleo.

## Contexto e Premissas

O problema de classificação baseia-se em 3 grandezas ($x_1, x_2, x_3$) que representam as propriedades físico-químicas do óleo. Para solucionar a atividade, foi desenvolvido o script em Python (`resolucao.py`) que implementa e treina o Perceptron utilizando a **Regra de Aprendizagem de Hebb** (aprendizado supervisionado), com as seguintes definições:
- **Taxa de aprendizagem ($\eta$)**: `0.01`
- **Valores das Classes**: Classe $C_1 = -1$ e Classe $C_2 = +1$
- **Critério de Parada**: O treinamento para apenas quando o erro no conjunto de treinamento for igual a zero.
- **Pesos Iniciais**: Vetor inicializado randomicamente com valores entre `0` e `1` a cada execução.

---

## 1 e 2. Execuções de Treinamento e Pesos Finais

Conforme solicitado, a rede foi treinada 5 vezes com o gerador de números aleatórios inicializando pesos diferentes entre $0$ e $1$ em cada treinamento. Abaixo estão os resultados das convergências obtidas pelas 5 baterias de execução:

| Treinamento | Quantidade de Épocas | Bias ($w_0$) | Peso $w_1$ | Peso $w_2$ | Peso $w_3$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **T1** | 401 | 3.0962 | 1.5763 | 2.5009 | -0.7385 |
| **T2** | 386 | 3.1050 | 1.5580 | 2.4874 | -0.7390 |
| **T3** | 424 | 3.1365 | 1.6047 | 2.5198 | -0.7464 |
| **T4** | 358 | 3.0413 | 1.5454 | 2.4485 | -0.7256 |
| **T5** | 327 | 2.9099 | 1.4042 | 2.4142 | -0.6965 |

> **Nota:** Como os pesos iniciais são pseudo-aleatórios, execuções subsequentes do script gerarão quantidades diferentes de épocas, mas invariavelmente encontrarão um vetor de pesos (hiperplano) válido que zera o erro no treinamento.

---

## 3. Aplicação do Modelo nas Amostras de Teste

Abaixo está a tabela de classificação automática das novas amostras de óleo. Foi aplicado o vetor de pesos finais encontrado em cada um dos cinco treinamentos realizados no item anterior para prever a classe $y$:

| Amostra | $x_1$ | $x_2$ | $x_3$ | $y(T_1)$ | $y(T_2)$ | $y(T_3)$ | $y(T_4)$ | $y(T_5)$ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **1** | -0.3565 | 0.0620 | 5.9891 | **-1** | **-1** | **-1** | **-1** | **-1** |
| **2** | -0.7842 | 1.1267 | 5.5912 | **1** | **1** | **1** | **1** | **1** |
| **3** | 0.3012 | 0.5611 | 5.8234 | **1** | **1** | **1** | **1** | **1** |
| **4** | 0.7757 | 1.0648 | 8.0677 | **1** | **1** | **1** | **1** | **1** |
| **5** | 0.1570 | 0.8028 | 6.3040 | **1** | **1** | **1** | **1** | **1** |
| **6** | -0.7014 | 1.0316 | 3.6005 | **1** | **1** | **1** | **1** | **1** |
| **7** | 0.3748 | 0.1536 | 6.1537 | **-1** | **-1** | **-1** | **-1** | **-1** |
| **8** | -0.6920 | 0.9404 | 4.4058 | **1** | **1** | **1** | **1** | **1** |
| **9** | -1.3970 | 0.7141 | 4.9263 | **-1** | **-1** | **-1** | **-1** | **-1** |
| **10** | -1.8842 | -0.2805 | 1.2548 | **-1** | **-1** | **-1** | **-1** | **-1** |

> Como é possível observar, mesmo com matrizes de pesos diferentes e variando o número de épocas, a consistência preditiva das classes geradas indica que o Perceptron encontrou em todos os 5 testes uma superfície de separação válida generalizável (100% de concordância nas saídas).

---

## 4. Por que o número de épocas de treinamento varia a cada vez que executamos o treinamento do perceptron?

O algoritmo de treinamento de um Perceptron procura iterativamente ajustar seus pesos até que trace no espaço um hiperplano capaz de separar todas as amostras das duas classes. 

A quantidade de ajustes necessários (que se traduz no número de épocas) depende diretamente do **ponto de partida no espaço de pesos**. Como, de acordo com o enunciado, a rede foi configurada para inicializar os pesos com números aleatórios entre $0$ e $1$ a cada nova execução, o algoritmo sempre começará a busca por uma fronteira de decisão a partir de uma "rota" diferente. Por começar de um ponto aleatório distinto, a trajetória até a convergência ótima varia, resultando na flutuação natural do número total de épocas gastas no ajuste fino.

---

## 5. Qual a principal limitação do perceptron quando aplicado em problemas de classificação de padrões?

A restrição fundamental do algoritmo de Perceptron Clássico de camada única é que ele é **capaz de aprender a separar apenas padrões que sejam perfeitamente e linearmente separáveis**.

Se a distribuição dos padrões das classes $C_1$ e $C_2$ for muito mesclada ou disposta em um modelo curvo e complexo (impossível de ser cortado de forma limpa por uma única reta ou hiperplano liso - como acontece, por exemplo, no famoso problema geométrico da função lógica *XOR*), o Perceptron falhará em convergir. Nesse cenário não-linear, o algoritmo fica oscilando infinitamente na atualização dos pesos e o erro nunca zera.

---

## Como visualizar e executar

Para reproduzir os resultados:

1. **Testando via Interface Gráfica:** 
   Abra o arquivo `index.html` em qualquer navegador web (Chrome, Firefox, etc) para visualizar a representação rica dos dados e a ilustração gráfica do modelo.
2. **Rodando o Script Principal:** 
   Pelo terminal, com o Python 3 instalado, execute o comando:
   ```bash
   python3 resolucao.py
   ```
