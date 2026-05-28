# Mapas Auto-Organizáveis de Kohonen (SOM)

Este repositório contém a resolução do exercício prático sobre a aplicação de uma **Rede Neural de Kohonen** (SOM - Self-Organizing Map) para detectar similaridades e agrupar amostras de imperfeições de borracha no processo de fabricação de pneus.

---

## 📐 Topologia e Configuração da Rede

A Rede de Kohonen é um modelo de aprendizado não supervisionado que realiza o mapeamento de um espaço de entrada multidimensional em um espaço de saída discreto (geralmente unidimensional ou bidimensional), preservando as relações topológicas de vizinhança entre os dados originais.

### 1. Parâmetros Utilizados
*   **Vetor de Entrada ($x$):** 3 grandezas físico-químicas $\{x_1, x_2, x_3\}$.
*   **Grid Topológico de Saída:** Bidimensional $4 \times 4$ (total de $16$ neurônios de saída, indexados de $1$ a $16$).
*   **Taxa de Aprendizado ($\eta$):** $0.001$ (constante).
*   **Vizinhança Topológica ($R$):** Raio de vizinhança igual a $1$ no grid (utilizando distância Chebyshev/bloco $3 \times 3$ ao redor do neurônio vencedor).
*   **Épocas de Treinamento:** $5.000$ épocas.
*   **Conjunto de Dados (Treino):** 120 amostras de apêndice, compostas por:
    *   **Amostras 1 a 20:** Classe A
    *   **Amostras 21 a 60:** Classe B
    *   **Amostras 61 a 120:** Classe C

---

## 🧠 Respostas da Atividade

### 1. Conjunto de Neurônios no Grid por Classe

Após o treinamento da rede de Kohonen com os 120 padrões do apêndice, analisou-se o mapeamento das ativações (neurônio vencedor ou BMU - Best Matching Unit) de cada amostra. O grid topológico $4 \times 4$ dividiu-se nitidamente nas seguintes bacias de atração correspondentes às classes:

*   **Classe A (Amostras 1 a 20):** Representada pelo **Neurônio 16** (canto inferior direito, coordenada $(3,3)$).
*   **Classe B (Amostras 21 a 60):** Representada pelos **Neurônios 3, 4, 7 e 8** (lado superior direito, coordenadas $(0,2), (0,3), (1,2), (1,3)$).
*   **Classe C (Amostras 61 a 120):** Representada pelos **Neurônios 1, 2, 5, 6, 9, 10 e 13** (lado esquerdo, coordenadas $(0,0), (0,1), (1,0), (1,1), (2,0), (2,1), (3,0)$).
*   **Neurônios Inativos/Fronteiras:** Os neurônios **11, 12, 14 e 15** (coordenadas $(2,2), (2,3), (3,1), (3,2)$) não foram vencedores para nenhuma amostra no treinamento. Eles atuam como faixas de separação topológica (fronteiras) livres no grid, refletindo a distância geométrica das classes no espaço de entrada de 3 dimensões.

---

### 2. Classificação das Novas Amostras de Teste

Utilizando os pesos ajustados da rede de Kohonen treinada no item anterior, as 12 novas amostras de imperfeição foram classificadas de acordo com o neurônio vencedor ativado por cada uma:

| Amostra de Teste | $x_1$ | $x_2$ | $x_3$ | Neurônio Vencedor (BMU) | Classe Predita |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | 0.2471 | 0.1778 | 0.2905 | **16** | **Classe A** |
| **2** | 0.8240 | 0.2223 | 0.7041 | **4** | **Classe B** |
| **3** | 0.4960 | 0.7231 | 0.5866 | **2** | **Classe C** |
| **4** | 0.2923 | 0.2041 | 0.2234 | **16** | **Classe A** |
| **5** | 0.8118 | 0.2668 | 0.7484 | **4** | **Classe B** |
| **6** | 0.4837 | 0.8200 | 0.4792 | **5** | **Classe C** |
| **7** | 0.3248 | 0.2629 | 0.2375 | **16** | **Classe A** |
| **8** | 0.7209 | 0.2116 | 0.7821 | **4** | **Classe B** |
| **9** | 0.5259 | 0.6522 | 0.5957 | **2** | **Classe C** |
| **10** | 0.2075 | 0.1669 | 0.1745 | **16** | **Classe A** |
| **11** | 0.7830 | 0.3171 | 0.7888 | **4** | **Classe B** |
| **12** | 0.5393 | 0.7510 | 0.5682 | **2** | **Classe C** |

---

### 3. Demonstração Matemática da Regra de Aprendizado

Pretende-se demonstrar que a regra de atualização de pesos da Rede de Kohonen (baseada na Norma Euclidiana) para um padrão $x$ é obtida a partir da minimização da função de erro quadrático:
$$E = \frac{1}{2} \|x - w_j\|^2$$
onde $j$ é o índice do neurônio vencedor (BMU).

#### **Demonstração:**
Seja o vetor de entrada $x = [x_1, x_2, \dots, x_d]^T$ e o vetor de pesos sinápticos do neurônio vencedor $w_j = [w_{j1}, w_{j2}, \dots, w_{jd}]^T$. A função de erro quadrático associada à distância euclidiana entre a entrada e o neurônio vencedor é dada por:
$$E(w_j) = \frac{1}{2} \sum_{i=1}^{d} (x_i - w_{ji})^2$$

Para encontrar a regra que atualiza os pesos de modo a minimizar o erro $E$, aplica-se a técnica do **Gradiente Descendente**, na qual os pesos são ajustados no sentido oposto ao gradiente da função de custo em relação aos pesos:
$$w_{ji}(t+1) = w_{ji}(t) - \eta \frac{\partial E}{\partial w_{ji}}$$
onde $\eta$ representa a taxa de aprendizado.

Calculando a derivada parcial de $E$ em relação ao peso individual $w_{ji}$ do neurônio vencedor $j$:
$$\frac{\partial E}{\partial w_{ji}} = \frac{\partial}{\partial w_{ji}} \left[ \frac{1}{2} \sum_{k=1}^{d} (x_k - w_{jk})^2 \right]$$

Pela regra da cadeia, derivando em relação ao termo da soma $k = i$:
$$\frac{\partial E}{\partial w_{ji}} = \frac{1}{2} \cdot 2 \cdot (x_i - w_{ji}) \cdot \frac{\partial}{\partial w_{ji}} (x_i - w_{ji})$$
$$\frac{\partial E}{\partial w_{ji}} = (x_i - w_{ji}) \cdot (-1)$$
$$\frac{\partial E}{\partial w_{ji}} = -(x_i - w_{ji})$$

Logo, o vetor gradiente completo em relação ao vetor de pesos $w_j$ é:
$$\nabla_{w_j} E = -(x - w_j)$$

Substituindo o gradiente calculado na equação clássica de atualização de pesos do gradiente descendente:
$$w_j(t+1) = w_j(t) - \eta \cdot \left[ -(x - w_j(t)) \right]$$
$$w_j(t+1) = w_j(t) + \eta \cdot (x - w_j(t))$$

Essa é exatamente a regra de atualização de pesos de Kohonen para o neurônio vencedor! Q.E.D.

*(Nota: Para os demais neurônios, a atualização é modulada por uma função de vizinhança topológica $h_{cj}(t)$, resultando na regra geral $w_k(t+1) = w_k(t) + \eta \cdot h_{ck} \cdot (x - w_k(t))$).*

---

## 💻 Como Rodar a Resolução

Para reproduzir os treinamentos e gerar o arquivo de resultados do Kohonen em formato JSON, rode o comando a partir da pasta raiz:

```bash
python Kohonen/resolucao_kohonen.py
```
