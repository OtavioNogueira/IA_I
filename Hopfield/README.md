# Memória Associativa com Rede de Hopfield

Este repositório contém a resolução do exercício prático sobre a aplicação de uma **Rede Neural de Hopfield** de 45 neurônios para atuar como memória associativa, capaz de armazenar e recuperar 4 padrões de dígitos ($9 \times 5$ pixels).

---

## 📐 Topologia e Fundamentação Matemática

A Rede de Hopfield é uma rede neural recorrente de camada única, na qual todos os neurônios são conectados entre si, exceto consigo mesmos (auto-associação nula).

### 1. Codificação dos Padrões
Os pixels das imagens são representados em formato bipolar:
*   **Pixel Branco:** codificado como $-1$
*   **Pixel Escuro:** codificado como $+1$

Cada imagem $9 \times 5$ é achatada em um vetor coluna $x^{\mu}$ de dimensão $N = 45$.

### 2. Matriz de Pesos ($W$)
A matriz de pesos sinápticos $W$ de dimensão $45 \times 45$ é calculada de acordo com a **Regra de Aprendizagem de Hebb** (produto externo) acumulada para os $M = 4$ padrões:
$$W_{ij} = \sum_{\mu=1}^{M} x_i^{\mu} x_j^{\mu} \quad (\text{para } i \neq j)$$
$$W_{ii} = 0 \quad (\text{auto-associação nula para garantir a convergência})$$

### 3. Função de Ativação e Regra de Atualização
A função de ativação é uma **Tangente Hiperbólica com ganho $\lambda$ muito grande**, o que equivale no limite à função de sinal bipolar ($\text{sgn}$):
$$x_i(t+1) = \text{sgn}\left(\sum_{j=1}^{N} W_{ij} x_j(t)\right)$$

Onde a regra de atualização é implementada de forma a manter o estado anterior caso a soma ponderada de entradas seja nula:
$$x_i(t+1) = \begin{cases} +1, & \text{se } \sum_j W_{ij} x_j(t) > 0 \\ -1, & \text{se } \sum_j W_{ij} x_j(t) < 0 \\ x_i(t), & \text{se } \sum_j W_{ij} x_j(t) = 0 \end{cases}$$

O processo de atualização adotado é **assíncrono** (um neurônio por vez atualizado em ordem aleatória), o que garante que a função de energia de Lyapunov da rede:
$$E = -\frac{1}{2} \sum_{i=1}^{N} \sum_{j=1}^{N} W_{ij} x_i x_j$$
nunca aumente ($dE/dt \leq 0$), garantindo a convergência da rede para um ponto fixo estável.

---

## 📌 Padrões Armazenados (Imagens Originais)

Os 4 padrões numéricos extraídos diretamente da tabela do arquivo original `Hopfield.docx` possuem a seguinte distribuição espacial de pixels ($9 \times 5$):

```text
  Padrão 1 (Dígito 1)       Padrão 2 (Dígito 2)       Padrão 3 (Dígito 3)       Padrão 4 (Dígito 4)
     . . # # .                 # # # # #                 # # # # #                 # # . # #
     . # # # .                 # # # # #                 # # # # #                 # # . # #
     . . # # .                 . . . # #                 . . . # #                 # # . # #
     . . # # .                 . . . # #                 . . . # #                 # # # # #
     . . # # .                 # # # # #                 # # # # #                 # # # # #
     . . # # .                 # # . . .                 . . . # #                 . . . # #
     . . # # .                 # # . . .                 . . . # #                 . . . # #
     . . # # .                 # # # # #                 # # # # #                 . . . # #
     . . # # .                 # # # # #                 # # # # #                 . . . # #
```

---

## 🧪 Simulação de Cenários com 20% de Ruído

Foram simuladas 12 transmissões (3 testes para cada um dos 4 padrões) invertendo o sinal de **exatamente 9 pixels (20%)** gerados de forma pseudo-aleatória. Abaixo estão descritos os resultados textuais obtidos pela rede:

### Resumo das Execuções

*   **Padrão 1 (Dígito 1):**
    *   *Simulação 1:* Recuperado com sucesso em 2 iterações.
    *   *Simulação 2:* Recuperado com sucesso em 2 iterações.
    *   *Simulação 3:* Recuperado com sucesso em 2 iterações.
*   **Padrão 2 (Dígito 2):**
    *   *Simulação 1:* **Falha** (divergiu para um estado espúrio próximo em 3 iterações).
    *   *Simulação 2:* Recuperado com sucesso em 2 iterações.
    *   *Simulação 3:* Recuperado com sucesso em 2 iterações.
*   **Padrão 3 (Dígito 3):**
    *   *Simulação 1:* Recuperado com sucesso em 2 iterações.
    *   *Simulação 2:* Recuperado com sucesso em 2 iterações.
    *   *Simulação 3:* Recuperado com sucesso em 2 iterações.
*   **Padrão 4 (Dígito 4):**
    *   *Simulação 1:* Recuperado com sucesso em 2 iterações.
    *   *Simulação 2:* Recuperado com sucesso em 2 iterações.
    *   *Simulação 3:* **Falha** (divergiu para o Padrão 3 em 3 iterações).

### Análise das Falhas Experimentais
Nas simulações **Padrão 2 - Teste 1** e **Padrão 4 - Teste 3**, a rede convergiu para estados incorretos. Isso ilustra um conceito fundamental das redes de Hopfield: os dígitos 2, 3 e 4 compartilham uma alta quantidade de pixels na mesma posição (forte correlação cruzada, ou seja, baixa ortogonalidade vetorial). 
Quando o ruído afeta pixels chave que distinguem esses padrões (por exemplo, a parte esquerda e direita central dos números), a imagem ruidosa inicial é empurrada para fora da **bacia de atração** do dígito original, caindo na bacia de atração de outro dígito (como o 4 convergindo para o 3) ou em um **estado espúrio** (um mínimo local que não é nenhum dos padrões originais).

---

## 📈 Consequências do Aumento Excessivo de Ruído

Quando aumentamos substancialmente a porcentagem de pixels corrompidos na transmissão (ruído superior a 25%-30%), observam-se os seguintes fenômenos na rede de Hopfield:

1.  **Divergência para Estados Espúrios:**
    A função de custo de energia da rede possui mínimos de energia locais estáveis que não correspondem a nenhuma imagem originalmente gravada. Esses estados são chamados de *estados espúrios* (misturas lineares dos padrões originais). Quanto maior o ruído, maior a chance do sinal ruidoso inicial deslizar pela superfície de Lyapunov em direção a esses "falsos atratores".
2.  **Convergência para a Imagem Invertida (Negativo):**
    A função de energia de Hopfield é simétrica em relação à origem:
    $$E(x) = E(-x)$$
    Isso significa que para todo padrão estável $x^{\mu}$ armazenado, o seu inverso complementar $-x^{\mu}$ (imagem em negativo, onde brancos viram pretos e vice-versa) também é um ponto de convergência estável. Se o nível de ruído ultrapassar $50\%$, o vetor de estado inicial estará mais próximo do complementar $-x^{\mu}$ do que do padrão original $x^{\mu}$, fazendo com que a rede converja perfeitamente para o negativo da imagem original.
3.  **Ultrapassagem da Capacidade de Armazenamento:**
    A capacidade de armazenamento teórica de uma rede de Hopfield convencional para que não haja erros de associação é de $C \approx 0.138 \times N$ padrões. Como $N=45$, o limite é de aproximadamente $6$ padrões. Armazenar $4$ padrões bastante correlacionados faz com que as bacias de atração fiquem "rasas" e deformadas. Sob alto ruído, as bacias de atração colapsam e a rede perde totalmente a capacidade de recuperar a memória associativa.

---

## ⚙️ Como Executar a Simulação

Com o Python instalado no sistema, execute o comando na raiz do projeto:

```bash
python Hopfield/resolucao_hopfield.py
```

Isso recriará as 12 simulações exibindo a visualização em formato de grade ASCII diretamente no terminal e atualizará o arquivo de dados `Hopfield/dados_simulacao.json`.
