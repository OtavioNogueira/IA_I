import csv

# 1. Carregar os dados
dados = []
with open('dados.csv', 'r') as f:
    leitor = csv.reader(f)
    next(leitor) # pular o cabeçalho
    for linha in leitor:
        # x1, x2, x3, d
        x1 = float(linha[0])
        x2 = float(linha[1])
        x3 = float(linha[2])
        d = float(linha[3])
        dados.append(([x1, x2, x3], d))

# 2. Inicializar parâmetros do Perceptron
# Pesos: [w0, w1, w2, w3] onde w0 é o bias (ligado a uma entrada constante x0 = 1)
pesos = [0.0, 0.0, 0.0, 0.0]
taxa_aprendizagem = 0.01

# Função de ativação (Degrau Bipolar / Sinal)
def funcao_ativacao(v):
    if v >= 0:
        return 1.0
    else:
        return -1.0

# 3. Treinamento
época = 0
while True:
    erro_na_epoca = 0
    
    for x, d in dados:
        # Montar o vetor de entrada com o bias (x0 = 1)
        entradas = [1.0, x[0], x[1], x[2]]
        
        # Calcular o potencial de ativação (v)
        v = sum(w * e for w, e in zip(pesos, entradas))
        
        # Saída da rede (y)
        y = funcao_ativacao(v)
        
        # Calcular o erro
        erro = d - y
        
        # Se houver erro, atualizar os pesos (Regra de correção de erro)
        if erro != 0:
            erro_na_epoca += 1
            for i in range(len(pesos)):
                # Atualização: w_novo = w_atual + taxa * erro * entrada
                pesos[i] = pesos[i] + taxa_aprendizagem * erro * entradas[i]
                
    época += 1
    
    # Condição de parada: se não houve nenhum erro na época inteira, o treinamento terminou
    if erro_na_epoca == 0:
        break

# 4. Resultados
print(f"Treinamento concluído em {época} épocas.")
print("Pesos finais encontrados:")
print(f"Bias (w0): {pesos[0]:.4f}")
print(f"w1: {pesos[1]:.4f}")
print(f"w2: {pesos[2]:.4f}")
print(f"w3: {pesos[3]:.4f}")

# Validação rápida para mostrar que acerta todos
print("\nValidando os dados com os pesos finais:")
acertos = 0
for x, d in dados:
    entradas = [1.0, x[0], x[1], x[2]]
    v = sum(w * e for w, e in zip(pesos, entradas))
    y = funcao_ativacao(v)
    if y == d:
        acertos += 1
        
print(f"Acertos: {acertos} de {len(dados)} ({(acertos/len(dados))*100}%)")
