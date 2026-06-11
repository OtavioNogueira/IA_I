# LVQ-1 (Learning Vector Quantization 1)

## Contexto do Problema (Previsão de Potência Elétrica)
A previsão de potência elétrica é crucial para o planejamento operacional e manutenção de sistemas elétricos. Nesta atividade, a rede **LVQ-1** foi utilizada para classificar curvas de demanda de potência elétrica medidas nas primeiras horas do dia (7h às 12h) em 4 perfis/classes de consumo.

A base de treinamento consiste de 16 amostras de dias passados distribuídos em 4 classes de consumo. A rede foi treinada com taxa de aprendizagem inicial $\alpha = 0.05$ por 200 épocas.

---

## Protótipos (Vetores de Código) da Rede

Os protótipos representam o "vetor médio ideal" ou centroide ajustado para cada classe de consumo. A inicialização foi feita usando o primeiro elemento de cada classe no conjunto de treinamento.

| Classe | Canal / Horários (7h às 12h) | Vetor Inicial (w_init) | Vetor Final (w_final) |
|---|---|---|---|
| **Classe 1** | Perfil de Baixa Demanda | `[2.3976, 1.5328, 1.9044, 1.1937, 2.4184, 1.8649]` | `[2.3419, 1.4868, 1.9423, 1.2459, 2.3311, 1.8147]` |
| **Classe 2** | Perfil de Pico no Almoço | `[1.1201, 0.0587, 1.3154, 5.3783, 3.1849, 2.4276]` | `[1.0640, 0.1308, 1.2493, 5.3627, 3.1517, 2.3542]` |
| **Classe 3** | Perfil de Pico no Final do Dia | `[1.4871, 2.3448, 0.9918, 2.3160, 1.6783, 5.0850]` | `[1.4054, 2.2807, 1.0350, 2.4218, 1.7344, 5.0961]` |
| **Classe 4** | Perfil de Alta Demanda Contínua | `[2.9364, 1.5233, 4.6109, 1.3160, 4.2700, 6.8749]` | `[2.9490, 1.4921, 4.6615, 1.3816, 4.2521, 6.8545]` |

---

## Gráfico dos Perfis de Consumo (Protótipos)
*(Gráfico salvo como `grafico_perfis_lvq.png` na pasta).*

![Gráfico LVQ-1](file:///c:/Users/Otávio/IA_I/LVQ/grafico_perfis_lvq.png)

---

## Classificação das Amostras de Teste

Após o treinamento dos pesos dos protótipos, a rede foi exposta a 8 novos dias para predição do perfil de potência correspondente:

| Dia | 7h | 8h | 9h | 10h | 11h | 12h | Classe Predita | Descrição do Perfil |
|---|---|---|---|---|---|---|---|---|
| **1** | 2.9817 | 1.5656 | 4.8391 | 1.4311 | 4.1916 | 6.9718 | **Classe 4** | Alta demanda contínua |
| **2** | 1.5537 | 2.2615 | 1.3169 | 2.5873 | 1.7570 | 5.0958 | **Classe 3** | Pico no final do dia |
| **3** | 1.2240 | 0.2445 | 1.3595 | 5.4192 | 3.2027 | 2.5675 | **Classe 2** | Pico no horário de almoço |
| **4** | 2.5828 | 1.5146 | 2.1119 | 1.2859 | 2.3414 | 1.8695 | **Classe 1** | Baixa demanda |
| **5** | 2.4168 | 1.4857 | 1.8959 | 1.3013 | 2.4500 | 1.7868 | **Classe 1** | Baixa demanda |
| **6** | 1.0604 | 0.2276 | 1.2806 | 5.4732 | 3.2133 | 2.4839 | **Classe 2** | Pico no horário de almoço |
| **7** | 1.5246 | 2.4254 | 1.1353 | 2.5325 | 1.7569 | 5.2640 | **Classe 3** | Pico no final do dia |
| **8** | 3.0565 | 1.6259 | 4.7743 | 1.3654 | 4.2904 | 6.9808 | **Classe 4** | Alta demanda contínua |

---

## Discussão dos Resultados

O algoritmo LVQ-1 conseguiu mapear os protótipos de forma excelente. Como o problema exibe uma separação de padrões muito nítida (por exemplo, a Classe 2 tem pico na faixa de 5.3 às 10h, a Classe 4 tem picos nas faixas das 9h e 12h, etc.), a rede adaptou seus vetores de código com sucesso e classificou 100% dos dados de teste nos perfis corretos.
