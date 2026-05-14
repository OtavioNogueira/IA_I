import csv
import math
import random
import time
import matplotlib.pyplot as plt
import json
import statistics

def sigmoid(v):
    v = max(-500, min(v, 500))
    return 1.0 / (1.0 + math.exp(-v))

def sigmoid_derivative(out):
    return out * (1.0 - out)

# Carregar série temporal completa
serie = {}
with open('dados_serie.csv', 'r') as f:
    leitor = csv.reader(f)
    next(leitor)
    for linha in leitor:
        t = int(linha[0])
        v = float(linha[1])
        serie[t] = v

def constroi_janela(p, t_inicio, t_fim):
    """
    Constrói o dataset no formato Time Delay para o intervalo de tempo [t_inicio, t_fim].
    Para prever f(t), usa x = [f(t-1), f(t-2), ..., f(t-p)].
    """
    dados = []
    for t in range(t_inicio, t_fim + 1):
        x = [serie[t - i] for i in range(1, p + 1)]
        d = serie[t]
        dados.append((x, [d], t)) # d é lista com 1 elemento
    return dados

# Configurações globais
taxa_aprendizagem = 0.1
fator_momentum = 0.8
precisao = 0.5e-6
max_epocas = 10000

topologias = [
    {'nome': 'Rede 1', 'p': 5, 'N1': 10},
    {'nome': 'Rede 2', 'p': 10, 'N1': 15},
    {'nome': 'Rede 3', 'p': 15, 'N1': 25}
]

resultados_finais = {}

def treinar_rede(nome_topologia, p, num_oculta, id_treino):
    print(f"[{nome_topologia}] Iniciando Treinamento {id_treino}...")
    num_entradas = p
    num_saida = 1
    
    dados_treino = constroi_janela(p, p + 1, 100)
    
    # Inicialização aleatória nova para cada treinamento
    seed_val = int(time.time() * 1000) % 10000 + int(id_treino.replace("T", ""))
    random.seed(seed_val) # Varia semente
    
    pesos_oculta = [[random.random() for _ in range(num_entradas)] for _ in range(num_oculta)]
    bias_oculta = [random.random() for _ in range(num_oculta)]
    pesos_saida = [[random.random() for _ in range(num_oculta)] for _ in range(num_saida)]
    bias_saida = [random.random() for _ in range(num_saida)]
    
    delta_w_oculta_prev = [[0.0 for _ in range(num_entradas)] for _ in range(num_oculta)]
    delta_b_oculta_prev = [0.0 for _ in range(num_oculta)]
    delta_w_saida_prev = [[0.0 for _ in range(num_oculta)] for _ in range(num_saida)]
    delta_b_saida_prev = [0.0 for _ in range(num_saida)]
    
    epoca = 0
    eqm_anterior = float('inf')
    historico_eqm = []
    
    while epoca < max_epocas:
        eqm_atual = 0.0
        
        # Embaralhar dados de treino não foi solicitado estritamente, mas é comum. Faremos sequencial por simplicidade
        for x, d, _ in dados_treino:
            # FORWARD
            out_oculta = []
            for j in range(num_oculta):
                v_j = bias_oculta[j] + sum(pesos_oculta[j][i] * x[i] for i in range(num_entradas))
                out_oculta.append(sigmoid(v_j))
                
            out_saida = []
            for k in range(num_saida):
                v_k = bias_saida[k] + sum(pesos_saida[k][j] * out_oculta[j] for j in range(num_oculta))
                out_saida.append(sigmoid(v_k))
                
            # BACKWARD
            delta_saida = []
            for k in range(num_saida):
                e_k = d[k] - out_saida[k]
                delta_saida.append(e_k * sigmoid_derivative(out_saida[k]))
                
            delta_oculta = []
            for j in range(num_oculta):
                soma = sum(delta_saida[k] * pesos_saida[k][j] for k in range(num_saida))
                delta_oculta.append(soma * sigmoid_derivative(out_oculta[j]))
                
            # ATUALIZAR
            for k in range(num_saida):
                delta_b = taxa_aprendizagem * delta_saida[k] + fator_momentum * delta_b_saida_prev[k]
                bias_saida[k] += delta_b
                delta_b_saida_prev[k] = delta_b
                
                for j in range(num_oculta):
                    delta_w = taxa_aprendizagem * delta_saida[k] * out_oculta[j] + fator_momentum * delta_w_saida_prev[k][j]
                    pesos_saida[k][j] += delta_w
                    delta_w_saida_prev[k][j] = delta_w
                    
            for j in range(num_oculta):
                delta_b = taxa_aprendizagem * delta_oculta[j] + fator_momentum * delta_b_oculta_prev[j]
                bias_oculta[j] += delta_b
                delta_b_oculta_prev[j] = delta_b
                
                for i in range(num_entradas):
                    delta_w = taxa_aprendizagem * delta_oculta[j] * x[i] + fator_momentum * delta_w_oculta_prev[j][i]
                    pesos_oculta[j][i] += delta_w
                    delta_w_oculta_prev[j][i] = delta_w
                    
        # Calcular EQM da época
        eqm_epoch = 0.0
        for x, d, _ in dados_treino:
            out_o = [sigmoid(bias_oculta[j] + sum(pesos_oculta[j][i] * x[i] for i in range(num_entradas))) for j in range(num_oculta)]
            out_s = [sigmoid(bias_saida[k] + sum(pesos_saida[k][j] * out_o[j] for j in range(num_oculta))) for k in range(num_saida)]
            eqm_epoch += sum((d[k] - out_s[k])**2 for k in range(num_saida)) / num_saida
            
        eqm_atual = eqm_epoch / len(dados_treino)
        historico_eqm.append(eqm_atual)
        epoca += 1
        
        if abs(eqm_atual - eqm_anterior) <= precisao:
            break
        eqm_anterior = eqm_atual
        
    print(f" -> Concluído: {epoca} épocas, EQM = {eqm_atual:.6f}")
    return {
        'id': id_treino,
        'epocas': epoca,
        'eqm': eqm_atual,
        'historico_eqm': historico_eqm,
        'pesos_oculta': pesos_oculta,
        'bias_oculta': bias_oculta,
        'pesos_saida': pesos_saida,
        'bias_saida': bias_saida
    }

# Executar treinamentos
for topologia in topologias:
    nome = topologia['nome']
    p = topologia['p']
    N1 = topologia['N1']
    resultados_finais[nome] = []
    
    for id_t in range(1, 4):
        res = treinar_rede(nome, p, N1, f"T{id_t}")
        resultados_finais[nome].append(res)

print("\n--- VALIDAÇÃO (t=101..120) ---")
# Para cada rede e cada treino, calcular as previsões, Erro Relativo Médio e Variância
validacao_global = {} # t -> { 'f(t)': val, 'Rede 1': {'T1': val, 'T2': val, 'T3': val}, ... }
t_test = list(range(101, 121))

for t in t_test:
    validacao_global[t] = {'f_t': serie[t]}
    for topologia in topologias:
        validacao_global[t][topologia['nome']] = {}

estatisticas = {} # 'Rede 1': {'T1': {'erro': x, 'var': y}, ...}

for topologia in topologias:
    nome = topologia['nome']
    p = topologia['p']
    N1 = topologia['N1']
    dados_teste = constroi_janela(p, 101, 120)
    
    estatisticas[nome] = {}
    
    for idx_t, treino in enumerate(resultados_finais[nome]):
        id_t = treino['id']
        po = treino['pesos_oculta']
        bo = treino['bias_oculta']
        ps = treino['pesos_saida']
        bs = treino['bias_saida']
        
        erros_relativos = []
        
        for x, d, t in dados_teste:
            out_o = [sigmoid(bo[j] + sum(po[j][i] * x[i] for i in range(p))) for j in range(N1)]
            out_s = [sigmoid(bs[k] + sum(ps[k][j] * out_o[j] for j in range(N1))) for k in range(1)]
            
            y = out_s[0]
            validacao_global[t][nome][id_t] = y
            
            erro_rel = abs(d[0] - y) / d[0] if d[0] != 0 else 0
            erros_relativos.append(erro_rel * 100) # em %
            
        erro_medio = statistics.mean(erros_relativos)
        variancia = statistics.variance(erros_relativos)
        estatisticas[nome][id_t] = {
            'erro_medio': erro_medio,
            'variancia': variancia
        }
        print(f"{nome} {id_t}: Erro Rel. Médio = {erro_medio:.2f}%, Variância = {variancia:.2f}%")
        
# Encontrar melhor treinamento para cada rede
melhores = {}
for nome in estatisticas:
    melhor_t = min(estatisticas[nome].keys(), key=lambda t: estatisticas[nome][t]['erro_medio'])
    melhores[nome] = melhor_t
    print(f"Melhor para {nome}: {melhor_t}")

# Gráficos de EQM vs Épocas (Atividade 4)
fig, axs = plt.subplots(1, 3, figsize=(18, 5))
cores = ['blue', 'green', 'red']
for idx, topologia in enumerate(topologias):
    nome = topologia['nome']
    melhor_id = melhores[nome]
    # Recupera historico
    treino = next(t for t in resultados_finais[nome] if t['id'] == melhor_id)
    historico = treino['historico_eqm']
    
    axs[idx].plot(historico, color=cores[idx], label=f'{nome} ({melhor_id})')
    axs[idx].set_title(f'EQM vs Épocas - {nome}')
    axs[idx].set_xlabel('Épocas')
    axs[idx].set_ylabel('EQM')
    axs[idx].grid(True)
    axs[idx].legend()

plt.tight_layout()
plt.savefig('grafico_eqm_pmc3.png')
print("Salvo grafico_eqm_pmc3.png")

# Gráficos de Valores Desejados vs Estimados (Atividade 5)
fig, axs = plt.subplots(1, 3, figsize=(18, 5))
for idx, topologia in enumerate(topologias):
    nome = topologia['nome']
    melhor_id = melhores[nome]
    
    y_real = [validacao_global[t]['f_t'] for t in t_test]
    y_pred = [validacao_global[t][nome][melhor_id] for t in t_test]
    
    axs[idx].plot(t_test, y_real, color='black', label='Desejado', marker='o')
    axs[idx].plot(t_test, y_pred, color=cores[idx], label=f'Estimado ({melhor_id})', marker='x', linestyle='--')
    axs[idx].set_title(f'Validação - {nome}')
    axs[idx].set_xlabel('Tempo (t)')
    axs[idx].set_ylabel('Valor')
    axs[idx].grid(True)
    axs[idx].legend()

plt.tight_layout()
plt.savefig('grafico_validacao_pmc3.png')
print("Salvo grafico_validacao_pmc3.png")

# Exportar resultados finais para JSON (apenas métricas para o front)
export = {
    'treinamentos': {},
    'validacao': {},
    'estatisticas': estatisticas,
    'melhores': melhores
}

for nome in resultados_finais:
    export['treinamentos'][nome] = {}
    for t in resultados_finais[nome]:
        export['treinamentos'][nome][t['id']] = {
            'eqm': t['eqm'],
            'epocas': t['epocas']
        }

for t in t_test:
    export['validacao'][t] = validacao_global[t]

with open('resultados_pmc3.json', 'w') as f:
    json.dump(export, f, indent=4)
