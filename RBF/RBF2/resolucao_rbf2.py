import json
import numpy as np
import matplotlib.pyplot as plt

# 1. Carregar Dados
with open('/home/alunos/Desktop/ubuntu/RBF/RBF2/teste.json', 'r') as f:
    teste_data = json.load(f)
with open('/home/alunos/Desktop/ubuntu/RBF/RBF2/treino.json', 'r') as f:
    treino_data = json.load(f)[5:] # ignorar lixo inicial

X_treino = np.array([x[:3] for x in treino_data])
d_treino = np.array([x[3] for x in treino_data])

X_teste = np.array([x[:3] for x in teste_data])
d_teste = np.array([x[3] for x in teste_data])

# 2. Implementação K-Means
def kmeans(X, k, seed=42):
    np.random.seed(seed)
    indices = np.random.choice(len(X), k, replace=False)
    centros = X[indices].copy()
    
    for _ in range(100):
        distancias = np.linalg.norm(X[:, np.newaxis] - centros, axis=2)
        labels = np.argmin(distancias, axis=1)
        novos_centros = np.array([X[labels == i].mean(axis=0) if np.sum(labels == i) > 0 else centros[i] for i in range(k)])
        if np.allclose(centros, novos_centros):
            break
        centros = novos_centros
        
    variancias = np.zeros(k)
    for i in range(k):
        pontos = X[labels == i]
        if len(pontos) > 1:
            variancias[i] = np.mean(np.sum((pontos - centros[i])**2, axis=1))
        else:
            variancias[i] = 1.0 # fallback
            
    # Heurística se variância for muito pequena ou zero
    v_mean = np.mean(variancias[variancias > 0.01]) if np.any(variancias > 0.01) else 1.0
    variancias[variancias < 0.01] = v_mean
    return centros, variancias

def phi(x, c, v):
    return np.exp(-np.sum((x - c)**2) / (2 * v))

eta = 0.01
precisao = 1e-7
topologias = [5, 10, 15]

resultados = {}
melhores_eqms_hist = {}

np.random.seed(42)

for n1 in topologias:
    print(f"Treinando Rede com N1 = {n1}")
    centros, variancias = kmeans(X_treino, n1, seed=n1)
    
    # Pre-calcular ativacoes para o treino
    H_treino = np.zeros((len(X_treino), n1))
    for i in range(len(X_treino)):
        for j in range(n1):
            H_treino[i, j] = phi(X_treino[i], centros[j], variancias[j])
            
    H_teste = np.zeros((len(X_teste), n1))
    for i in range(len(X_teste)):
        for j in range(n1):
            H_teste[i, j] = phi(X_teste[i], centros[j], variancias[j])
            
    resultados[n1] = []
    
    for t in range(3):
        w = np.random.rand(n1 + 1) # bias + pesos
        epoca = 0
        eqm_anterior = float('inf')
        
        eqm_hist = []
        
        while True:
            # Forward e Backward
            v_all = np.dot(H_treino, w[1:]) + w[0]
            erros = d_treino - v_all
            
            # Atualiza pesos (Stochastic/Online ou Batch? O comum em aula é Online, vamos fazer online)
            for i in range(len(X_treino)):
                v = np.dot(H_treino[i], w[1:]) + w[0]
                erro = d_treino[i] - v
                w[0] += eta * erro * 1.0
                w[1:] += eta * erro * H_treino[i]
                
            # Calcula EQM Batch
            v_all = np.dot(H_treino, w[1:]) + w[0]
            eqm_atual = np.mean((d_treino - v_all)**2)
            eqm_hist.append(eqm_atual)
            
            if abs(eqm_atual - eqm_anterior) <= precisao or epoca > 10000:
                break
            eqm_anterior = eqm_atual
            epoca += 1
            
        # Calcula saidas teste
        y_teste = np.dot(H_teste, w[1:]) + w[0]
        
        resultados[n1].append({
            'epocas': epoca,
            'eqm': eqm_atual,
            'y_teste': y_teste,
            'eqm_hist': eqm_hist,
            'w': w.copy()
        })
        print(f"  Treinamento {t+1}: Epocas={epoca}, EQM={eqm_atual:.6f}")

# Obter o melhor treinamento para plotar
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
for idx, n1 in enumerate(topologias):
    melhor_t = min(resultados[n1], key=lambda x: x['eqm'])
    axes[idx].plot(melhor_t['eqm_hist'])
    axes[idx].set_title(f"Rede N1={n1}")
    axes[idx].set_xlabel("Épocas")
    axes[idx].set_ylabel("EQM")
    
plt.tight_layout()
plt.savefig('/home/alunos/Desktop/ubuntu/RBF/RBF2/RBF2_EQM.png')

# Imprimir as tabelas solicitadas
print("\n=== TABELA 1: EQM e Epocas ===")
for t in range(3):
    print(f"T{t+1}:", end=" ")
    for n1 in topologias:
        res = resultados[n1][t]
        print(f"N1={n1} [EQM={res['eqm']:.6f}, Ep={res['epocas']}]", end=" | ")
    print()

print("\n=== TABELA 2: Teste Erro Relativo ===")
for i in range(len(X_teste)):
    print(f"Amostra {i+1:02d} d={d_teste[i]:.4f} |", end=" ")
    for n1 in topologias:
        for t in range(3):
            print(f"{resultados[n1][t]['y_teste'][i]:.4f}", end=" ")
        print("|", end=" ")
    print()

# Erro relativo
print("\n--- Erro Relativo Médio (%) e Variância ---")
for n1 in topologias:
    print(f"Rede N1={n1}:")
    for t in range(3):
        y_t = resultados[n1][t]['y_teste']
        erros_rel = np.abs(d_teste - y_t) / d_teste * 100
        erro_medio = np.mean(erros_rel)
        variancia = np.var(erros_rel)
        print(f"  T{t+1}: Erro Relativo = {erro_medio:.2f}%, Variancia = {variancia:.2f}%")
