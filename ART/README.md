# ART-1 (Adaptive Resonance Theory)

## Contexto do Problema (Diagnóstico Industrial)
O comportamento de um processo industrial foi analisado levando em consideração 16 variáveis de status relativas às fases do processo. Foram fornecidas 10 situações do comportamento do processo (vetores binários de 16 dimensões) com o objetivo de agrupar as situações "parecidas" usando uma rede **ART-1** para auxiliar em diagnósticos de manutenção preventiva.

A rede foi simulada com os seguintes graus de vigilância ($\rho$):
*   $\rho = 0.5$
*   $\rho = 0.8$
*   $\rho = 0.9$
*   $\rho = 0.99$

---

## Resultados das Simulações

Abaixo estão os resultados consolidados obtidos após a convergência do algoritmo de treinamento:

| Grau de Vigilância ($\rho$) | Épocas até Convergir | Classes Ativas | Agrupamento de Situações |
|---|---|---|---|
| **0.50** | 3 | 3 | **Classe 1:** {3, 4, 8, 9}<br>**Classe 2:** {2, 5, 7, 10}<br>**Classe 3:** {1, 6} |
| **0.80** | 2 | 5 | **Classe 1:** {1, 6}<br>**Classe 2:** {2, 7}<br>**Classe 3:** {3, 8}<br>**Classe 4:** {4, 9}<br>**Classe 5:** {5, 10} |
| **0.90** | 2 | 7 | **Classe 1:** {1, 6}<br>**Classe 2:** {2}<br>**Classe 3:** {3, 8}<br>**Classe 4:** {4}<br>**Classe 5:** {5, 10}<br>**Classe 6:** {7}<br>**Classe 7:** {9} |
| **0.99** | 2 | 8 | **Classe 1:** {1}<br>**Classe 2:** {2}<br>**Classe 3:** {3, 8}<br>**Classe 4:** {4}<br>**Classe 5:** {5, 10}<br>**Classe 6:** {6}<br>**Classe 7:** {7}<br>**Classe 8:** {9} |

---

## Gráfico de Classes vs. Vigilância
*(Gráfico salvo como `grafico_classes_art1.png` na pasta).*

![Gráfico ART-1](file:///c:/Users/Otávio/IA_I/ART/grafico_classes_art1.png)

---

## Análise do Comportamento da Rede

1. **Influência do Parâmetro de Vigilância ($\rho$):**
   * O parâmetro de vigilância controla o quão rigorosa é a rede ao classificar um padrão em um grupo existente.
   * Com **baixa vigilância ($\rho = 0.5$)**, a tolerância a diferenças é alta, agrupando as situações em apenas **3 classes**.
   * Conforme aumentamos a vigilância para **$\rho = 0.8$** e **$\rho = 0.9$**, a rede torna-se mais exigente. Situações que antes compartilhavam a mesma classe são separadas em novos grupos (como as situações 2 e 7, e as situações 4 e 9).
   * Com **vigilância máxima ($\rho = 0.99$)**, a rede se comporta de forma quase estritamente discriminante, gerando **8 classes**. Apenas as situações idênticas (Situação 3 e 8, e Situação 5 and 10) permanecem agrupadas no mesmo cluster.

2. **Convergência Rápida:**
   * O algoritmo ART-1 possui a garantia teórica de estabilidade e convergência rápida. Em todos os testes, a rede estabilizou seus pesos e agrupamentos em no máximo **3 épocas**.
