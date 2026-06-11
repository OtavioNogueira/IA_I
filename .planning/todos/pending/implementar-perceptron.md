---
title: Implementar Perceptron (Regra de Aprendizagem do Perceptron) em Python
date: 2026-04-30
priority: high
---

# Implementar Perceptron (Regra de Aprendizagem do Perceptron) em Python

## Objetivo
Criar um script em Python simples e limpo para classificar o grau de pureza de um óleo a partir do dataset de Destilação de Petróleo.

## Detalhes
- Algoritmo: Perceptron
- Regra de aprendizado: Regra de aprendizado do Perceptron (baseada em erro / regra delta: `w = w + taxa * (d - y) * x`)
- Entradas: 3 features (x1, x2, x3) + o bias (x0 = 1 ou -1)
- Classes: C1 (-1), C2 (+1)
- Taxa de aprendizagem: 0.01
- Condição de Parada: Erro no treinamento for igual a zero (todas as classificações ficarem corretas)
- Linguagem: Python sem bibliotecas complexas, focado em clareza didática.

## Ações
1. Processar os dados brutos e estruturá-los (pode usar .csv ou injetar numa matriz pura do python/numpy).
2. Escrever a função de ativação sinal (degrau bipolar).
3. Escrever o loop principal de épocas para treinar os pesos.
4. Mostrar os pesos finais e o número de épocas necessárias.
