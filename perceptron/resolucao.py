import csv
import random

# 1. Carregar os dados de treinamento
dados_treino = []
with open('dados.csv', 'r') as f:
    leitor = csv.reader(f)
    next(leitor) # pular o cabeçalho
    for linha in leitor:
        x1, x2, x3, d = map(float, linha)
        dados_treino.append(([x1, x2, x3], d))

# Amostras de teste
amostras_teste = [
    [-0.3565, 0.0620, 5.9891],
    [-0.7842, 1.1267, 5.5912],
    [ 0.3012, 0.5611, 5.8234],
    [ 0.7757, 1.0648, 8.0677],
    [ 0.1570, 0.8028, 6.3040],
    [-0.7014, 1.0316, 3.6005],
    [ 0.3748, 0.1536, 6.1537],
    [-0.6920, 0.9404, 4.4058],
    [-1.3970, 0.7141, 4.9263],
    [-1.8842,-0.2805, 1.2548]
]

def funcao_ativacao(v):
    return 1.0 if v >= 0 else -1.0

taxa_aprendizagem = 0.01
num_treinamentos = 5
resultados_treinamento = [] # Guarda (epocas, pesos_finais)

print("--- ITEM 1 e 2: RESULTADOS DOS TREINAMENTOS ---")
for t in range(1, num_treinamentos + 1):
    # Inicializar pesos com valores aleatórios entre 0 e 1
    # random.random() gera entre 0.0 e 1.0
    pesos = [random.random(), random.random(), random.random(), random.random()]
    
    epoca = 0
    while True:
        erro_na_epoca = 0
        for x, d in dados_treino:
            entradas = [1.0, x[0], x[1], x[2]]
            v = sum(w * e for w, e in zip(pesos, entradas))
            y = funcao_ativacao(v)
            erro = d - y
            if erro != 0:
                erro_na_epoca += 1
                for i in range(len(pesos)):
                    pesos[i] += taxa_aprendizagem * erro * entradas[i]
        
        epoca += 1
        if erro_na_epoca == 0:
            break
            
    resultados_treinamento.append({
        'treinamento': t,
        'epocas': epoca,
        'pesos': pesos.copy()
    })
    
    print(f"Treinamento {t}: {epoca} épocas. Pesos finais: [w0={pesos[0]:.4f}, w1={pesos[1]:.4f}, w2={pesos[2]:.4f}, w3={pesos[3]:.4f}]")

print("\n--- ITEM 3: CLASSIFICAÇÃO DAS AMOSTRAS ---")
print("Amostra\ty(T1)\ty(T2)\ty(T3)\ty(T4)\ty(T5)")

for i, amostra in enumerate(amostras_teste, 1):
    saidas = []
    for res in resultados_treinamento:
        pesos = res['pesos']
        entradas = [1.0, amostra[0], amostra[1], amostra[2]]
        v = sum(w * e for w, e in zip(pesos, entradas))
        y = funcao_ativacao(v)
        saidas.append(f"{int(y):2d}")
        
    print(f"{i}\t{saidas[0]}\t{saidas[1]}\t{saidas[2]}\t{saidas[3]}\t{saidas[4]}")
