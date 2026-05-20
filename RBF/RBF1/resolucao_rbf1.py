import numpy as np

# 1. Dados de Treinamento
dados_treino = np.array([
    [0.2563, 0.9503, -1],
    [0.2405, 0.9018, -1],
    [0.1157, 0.3676, 1],
    [0.5147, 0.0167, 1],
    [0.4127, 0.3275, 1],
    [0.2809, 0.5830, 1],
    [0.8263, 0.9301, -1],
    [0.9359, 0.8724, -1],
    [0.1096, 0.9165, -1],
    [0.5158, 0.8545, -1],
    [0.1334, 0.1362, 1],
    [0.6371, 0.1439, 1],
    [0.7052, 0.6277, -1],
    [0.8703, 0.8666, -1],
    [0.2612, 0.6109, 1],
    [0.0244, 0.5279, 1],
    [0.9588, 0.3672, -1],
    [0.9332, 0.5499, -1],
    [0.9623, 0.2961, -1],
    [0.7297, 0.5776, -1],
    [0.4560, 0.1871, 1],
    [0.1715, 0.7713, 1],
    [0.5571, 0.5485, -1],
    [0.3344, 0.0259, 1],
    [0.4803, 0.7635, -1],
    [0.9721, 0.4850, -1],
    [0.8318, 0.7844, -1],
    [0.1373, 0.0292, 1],
    [0.3660, 0.8581, -1],
    [0.3626, 0.7302, -1],
    [0.6474, 0.3324, 1],
    [0.3461, 0.2398, 1],
    [0.1353, 0.8120, 1],
    [0.3463, 0.1017, 1],
    [0.9086, 0.1947, -1],
    [0.5227, 0.2321, 1],
    [0.5153, 0.2041, 1],
    [0.1832, 0.0661, 1],
    [0.5015, 0.9812, -1],
    [0.5024, 0.5274, -1]
])

# 2. Dados de Teste
dados_teste = np.array([
    [0.8705, 0.9329, -1],
    [0.0388, 0.2703, 1],
    [0.8236, 0.4458, -1],
    [0.7075, 0.1502, 1],
    [0.9587, 0.8663, -1],
    [0.6115, 0.9365, -1],
    [0.3534, 0.3646, 1],
    [0.3268, 0.2766, 1],
    [0.6129, 0.4518, -1],
    [0.9948, 0.4962, -1]
])

# Filtra apenas d=1 para K-means
treino_pos = dados_treino[dados_treino[:, 2] == 1][:, :2]

np.random.seed(42)
indices = np.random.choice(len(treino_pos), 2, replace=False)
centros = treino_pos[indices]

for _ in range(100):
    distancias = np.linalg.norm(treino_pos[:, np.newaxis] - centros, axis=2)
    labels = np.argmin(distancias, axis=1)
    novos_centros = np.array([treino_pos[labels == i].mean(axis=0) for i in range(2)])
    if np.allclose(centros, novos_centros):
        break
    centros = novos_centros

var1 = np.mean(np.sum((treino_pos[labels == 0] - centros[0])**2, axis=1))
var2 = np.mean(np.sum((treino_pos[labels == 1] - centros[1])**2, axis=1))

print("=== PARTE 1: K-Means nas amostras d=1 ===")
print(f"Cluster 1: Centro = {centros[0]}, Variancia = {var1:.6f}")
print(f"Cluster 2: Centro = {centros[1]}, Variancia = {var2:.6f}")

# Funções RBF
def phi(x, c, v):
    return np.exp(-np.sum((x - c)**2) / (2 * v))

# Treinamento Regra Delta
X_treino = dados_treino[:, :2]
d_treino = dados_treino[:, 2]

N = len(X_treino)
w = np.random.RandomState(42).rand(3) # w0, w1, w2
eta = 0.01
precisao = 1e-7

epoca = 0
eqm_anterior = float('inf')

while True:
    eqm_atual = 0
    for i in range(N):
        x = X_treino[i]
        d = d_treino[i]
        
        y1 = phi(x, centros[0], var1)
        y2 = phi(x, centros[1], var2)
        
        v = w[0] + w[1]*y1 + w[2]*y2
        erro = d - v
        
        w[0] += eta * erro * 1.0
        w[1] += eta * erro * y1
        w[2] += eta * erro * y2
        
    # Recalcula EQM
    for i in range(N):
        x = X_treino[i]
        y1 = phi(x, centros[0], var1)
        y2 = phi(x, centros[1], var2)
        v = w[0] + w[1]*y1 + w[2]*y2
        eqm_atual += (d_treino[i] - v)**2
    eqm_atual /= N
    
    if abs(eqm_atual - eqm_anterior) <= precisao:
        break
    eqm_anterior = eqm_atual
    epoca += 1

print("\n=== PARTE 2: Treinamento Regra Delta ===")
print(f"Epocas = {epoca}")
print(f"EQM Final = {eqm_atual:.6f}")
print(f"w0 = {w[0]:.6f}")
print(f"w1 = {w[1]:.6f}")
print(f"w2 = {w[2]:.6f}")

# Validacao
print("\n=== PARTE 3 e 4: Validacao ===")
acertos = 0
for i in range(len(dados_teste)):
    x = dados_teste[i, :2]
    d = dados_teste[i, 2]
    
    y1 = phi(x, centros[0], var1)
    y2 = phi(x, centros[1], var2)
    
    v = w[0] + w[1]*y1 + w[2]*y2
    y_pos = 1 if v >= 0 else -1
    
    if y_pos == d:
        acertos += 1
        
    print(f"Amostra {i+1}: d={d}, v={v:.4f}, y_pos={y_pos}")

print(f"\nTaxa de Acerto: {acertos/len(dados_teste)*100:.2f}%")
