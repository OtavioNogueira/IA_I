import os
import json
import random
import numpy as np

# Definindo os diretórios
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.join(BASE_DIR, "dados_simulacao.json")

# 1. Definição dos Padrões (Matrizes 9x5)
P1 = np.array([
    [-1, -1,  1,  1, -1],
    [-1,  1,  1,  1, -1],
    [-1, -1,  1,  1, -1],
    [-1, -1,  1,  1, -1],
    [-1, -1,  1,  1, -1],
    [-1, -1,  1,  1, -1],
    [-1, -1,  1,  1, -1],
    [-1, -1,  1,  1, -1],
    [-1, -1,  1,  1, -1]
])

P2 = np.array([
    [ 1,  1,  1,  1,  1],
    [ 1,  1,  1,  1,  1],
    [-1, -1, -1,  1,  1],
    [-1, -1, -1,  1,  1],
    [ 1,  1,  1,  1,  1],
    [ 1,  1, -1, -1, -1],
    [ 1,  1, -1, -1, -1],
    [ 1,  1,  1,  1,  1],
    [ 1,  1,  1,  1,  1]
])

P3 = np.array([
    [ 1,  1,  1,  1,  1],
    [ 1,  1,  1,  1,  1],
    [-1, -1, -1,  1,  1],
    [-1, -1, -1,  1,  1],
    [ 1,  1,  1,  1,  1],
    [-1, -1, -1,  1,  1],
    [-1, -1, -1,  1,  1],
    [ 1,  1,  1,  1,  1],
    [ 1,  1,  1,  1,  1]
])

P4 = np.array([
    [ 1,  1, -1,  1,  1],
    [ 1,  1, -1,  1,  1],
    [ 1,  1, -1,  1,  1],
    [ 1,  1,  1,  1,  1],
    [ 1,  1,  1,  1,  1],
    [-1, -1, -1,  1,  1],
    [-1, -1, -1,  1,  1],
    [-1, -1, -1,  1,  1],
    [-1, -1, -1,  1,  1]
])

padrões_originais = [P1, P2, P3, P4]
padrões_achatados = [p.flatten() for p in padrões_originais]
N = len(padrões_achatados[0]) # 45 neurônios
M = len(padrões_achatados)     # 4 padrões

# 2. Construção da Matriz de Pesos W (Regra de Hebb com auto-associação nula)
W = np.zeros((N, N))
for p in padrões_achatados:
    W += np.outer(p, p)
np.fill_diagonal(W, 0) # W_ii = 0

# 3. Função de Ativação do Hopfield (Tangente hiperbólica com ganho muito grande => função sinal)
def sgn(v, estado_anterior):
    res = np.zeros_like(v)
    for i in range(len(v)):
        if v[i] > 0:
            res[i] = 1
        elif v[i] < 0:
            res[i] = -1
        else:
            res[i] = estado_anterior[i]
    return res

# 4. Função para recuperar padrão (Atualização Assíncrona para garantir convergência de Lyapunov)
def recuperar_hopfield(vetor_ruidoso, max_iter=100):
    estado = np.array(vetor_ruidoso, dtype=float)
    iteracao = 0
    convergido = False
    
    # Executamos atualizações até estabilizar
    for _ in range(max_iter):
        estado_antigo = estado.copy()
        
        # Na atualização assíncrona, atualizamos a ordem dos neurônios aleatoriamente
        indices = list(range(N))
        random.shuffle(indices)
        
        for idx in indices:
            net = np.dot(W[idx], estado)
            if net > 0:
                estado[idx] = 1
            elif net < 0:
                estado[idx] = -1
            # Se for 0, mantém o estado anterior (estado[idx] não muda)
            
        iteracao += 1
        if np.array_equal(estado, estado_antigo):
            convergido = True
            break
            
    return estado, iteracao, convergido

# 5. Função para gerar ruído aleatório de 20% (exatamente 9 pixels invertidos)
def gerar_ruido(vetor, percent=0.20):
    res = vetor.copy()
    n_pixels_ruidosos = int(N * percent) # 45 * 0.20 = 9 pixels
    indices_para_inverter = random.sample(range(N), n_pixels_ruidosos)
    for idx in indices_para_inverter:
        res[idx] = -res[idx] # Inverte o pixel
    return res

# 6. Geração dos dados de simulação
# Para garantir reprodutibilidade, definiremos uma semente aleatória
random.seed(42)
np.random.seed(42)

simulações_resultados = []
for p_idx, p_orig in enumerate(padrões_achatados):
    for s_idx in range(3): # 3 simulações por padrão
        vetor_ruidoso = gerar_ruido(p_orig)
        vetor_recuperado, iteracoes, convergido = recuperar_hopfield(vetor_ruidoso)
        
        # Verificar se recuperou com sucesso o padrão correto
        sucesso = np.array_equal(vetor_recuperado, p_orig)
        
        simulações_resultados.append({
            "padrao_id": p_idx + 1,
            "simulacao_id": s_idx + 1,
            "original": p_orig.tolist(),
            "distorcido": vetor_ruidoso.tolist(),
            "recuperado": vetor_recuperado.tolist(),
            "iteracoes": iteracoes,
            "convergido": convergido,
            "sucesso": sucesso
        })

# Salvar como JSON para o dashboard
with open(JSON_PATH, 'w', encoding='utf-8') as f:
    json.dump(simulações_resultados, f, indent=4)

print(f"Resultados de simulação gerados e salvos em: {JSON_PATH}")

# 7. Imprimir no terminal para conferência em modo texto
def imprimir_matriz(vetor):
    mat = vetor.reshape((9, 5))
    linhas = []
    for r in mat:
        linhas.append(" ".join(["#" if x == 1 else "." for x in r]))
    return linhas

for r in simulações_resultados:
    print(f"\n==================================================")
    print(f"Padrão {r['padrao_id']} - Simulação {r['simulacao_id']} | Iterações: {r['iteracoes']} | Sucesso: {r['sucesso']}")
    print(f"==================================================")
    orig_lines = imprimir_matriz(np.array(r['original']))
    dist_lines = imprimir_matriz(np.array(r['distorcido']))
    rec_lines = imprimir_matriz(np.array(r['recuperado']))
    
    print(f"{'ORIGINAL':<12} | {'COM RUÍDO':<12} | {'RECUPERADA':<12}")
    print("-" * 50)
    for o, d, rec in zip(orig_lines, dist_lines, rec_lines):
        print(f"{o:<12} | {d:<12} | {rec:<12}")
