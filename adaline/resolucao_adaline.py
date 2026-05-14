import random
import matplotlib.pyplot as plt

# Dados de treinamentoj
dados_treino = [
    [0.4329, -1.3719, 0.7022, -0.8535, 1.0000],
    [0.3024, 0.2286, 0.8630, 2.7909, -1.0000],
    [0.1349, -0.6445, 1.0530, 0.5687, -1.0000],
    [0.3374, -1.7163, 0.3670, -0.6283, -1.0000],
    [1.1434, -0.0485, 0.6637, 1.2606, 1.0000],
    [1.3749, -0.5071, 0.4464, 1.3009, 1.0000],
    [0.7221, -0.7587, 0.7681, -0.5592, 1.0000],
    [0.4403, -0.8072, 0.5154, -0.3129, 1.0000],
    [-0.5231, 0.3548, 0.2538, 1.5776, -1.0000],
    [0.3255, -2.0000, 0.7112, -1.1209, 1.0000],
    [0.5824, 1.3915, -0.2291, 4.1735, -1.0000],
    [0.1340, 0.6081, 0.4450, 3.2230, -1.0000],
    [0.1480, -0.2988, 0.4778, 0.8649, 1.0000],
    [0.7359, 0.1869, -0.0872, 2.3584, 1.0000],
    [0.7115, -1.1469, 0.3394, 0.9573, -1.0000],
    [0.8251, -1.2840, 0.8452, 1.2382, -1.0000],
    [0.1569, 0.3712, 0.8825, 1.7633, 1.0000],
    [0.0033, 0.6835, 0.5389, 2.8249, -1.0000],
    [0.4243, 0.8313, 0.2634, 3.5855, -1.0000],
    [1.0490, 0.1326, 0.9138, 1.9792, 1.0000],
    [1.4276, 0.5331, -0.0145, 3.7286, 1.0000],
    [0.5971, 1.4865, 0.2904, 4.6069, -1.0000],
    [0.8475, 2.1479, 0.3179, 5.8235, -1.0000],
    [1.3967, -0.4171, 0.6443, 1.3927, 1.0000],
    [0.0044, 1.5378, 0.6099, 4.7755, -1.0000],
    [0.2201, -0.5668, 0.0515, 0.7829, 1.0000],
    [0.6300, -1.2480, 0.8591, 0.8093, -1.0000],
    [-0.2479, 0.8960, 0.0547, 1.7381, 1.0000],
    [-0.3088, -0.0929, 0.8659, 1.5483, -1.0000],
    [-0.5180, 1.4974, 0.5453, 2.3993, 1.0000],
    [0.6833, 0.8266, 0.0829, 2.8864, 1.0000],
    [0.4353, -1.4066, 0.4207, -0.4879, 1.0000],
    [-0.1069, -3.2329, 0.1856, -2.4572, -1.0000],
    [0.4662, 0.6261, 0.7304, 3.4370, -1.0000],
    [0.8298, -1.4089, 0.3119, 1.3235, -1.0000]
]

# Amostras de teste
amostras_teste = [
    [0.9694, 0.6909, 0.4334, 3.4965],
    [0.5427, 1.3832, 0.6390, 4.0352],
    [0.6081, -0.9196, 0.5925, 0.1016],
    [-0.1618, 0.4694, 0.2030, 3.0117],
    [0.1870, -0.2578, 0.6124, 1.7749],
    [0.4891, -0.5276, 0.4378, 0.6439],
    [0.3777, 2.0149, 0.7423, 3.3932],
    [1.1498, -0.4067, 0.2469, 1.5866],
    [0.9325, 1.0950, 1.0359, 3.3591],
    [0.5060, 1.3317, 0.9222, 3.7174],
    [0.0497, -2.0656, 0.6124, -0.6585],
    [0.4004, 3.5369, 0.9766, 5.3532],
    [-0.1874, 1.3343, 0.5374, 3.2189],
    [0.5060, 1.3317, 0.9222, 3.7174],
    [1.6375, -0.7911, 0.7537, 0.5515]
]

def funcao_ativacao(v):
    return 1.0 if v >= 0 else -1.0

taxa_aprendizagem = 0.0025
precisao = 1e-6
max_epocas = 100000
num_treinamentos = 5

resultados_treinamento = []

for t in range(1, num_treinamentos + 1):
    random.seed(t) # Semente para reproduzibilidade mas gerando pesos iniciais diferentes
    pesos_iniciais = [random.random() for _ in range(5)] # w0, w1, w2, w3, w4
    pesos = pesos_iniciais.copy()
    
    epoca = 0
    eqm_anterior = float('inf')
    historico_eqm = []
    
    while epoca < max_epocas:
        eqm_atual = 0.0
        
        for dado in dados_treino:
            x = dado[:4]
            d = dado[4]
            entradas = [1.0, x[0], x[1], x[2], x[3]]
            v = sum(w * e for w, e in zip(pesos, entradas))
            
            erro = d - v
            
            for i in range(len(pesos)):
                pesos[i] += taxa_aprendizagem * erro * entradas[i]
                
        # Recalcular EQM
        for dado in dados_treino:
            x = dado[:4]
            d = dado[4]
            entradas = [1.0, x[0], x[1], x[2], x[3]]
            v = sum(w * e for w, e in zip(pesos, entradas))
            erro = d - v
            eqm_atual += erro ** 2
            
        eqm_atual /= len(dados_treino)
        historico_eqm.append(eqm_atual)
        
        epoca += 1
        
        if abs(eqm_atual - eqm_anterior) <= precisao:
            break
            
        eqm_anterior = eqm_atual
            
    resultados_treinamento.append({
        'treinamento': t,
        'epocas': epoca,
        'pesos_iniciais': pesos_iniciais,
        'pesos_finais': pesos.copy(),
        'historico_eqm': historico_eqm
    })

print("="*100)
print("1 e 2. TABELA DE RESULTADOS DOS TREINAMENTOS")
print("="*100)
print(f"{'Treino':<8} | {'Pesos Iniciais (w0...w4)':<45} | {'Pesos Finais (w0...w4)':<45} | {'Épocas':<8}")
print("-" * 108)
for res in resultados_treinamento:
    pi = res['pesos_iniciais']
    pf = res['pesos_finais']
    pi_str = f"{pi[0]:.4f} {pi[1]:.4f} {pi[2]:.4f} {pi[3]:.4f} {pi[4]:.4f}"
    pf_str = f"{pf[0]:.4f} {pf[1]:.4f} {pf[2]:.4f} {pf[3]:.4f} {pf[4]:.4f}"
    print(f"T{res['treinamento']:<6} | {pi_str:<45} | {pf_str:<45} | {res['epocas']:<8}")

# 3. Gráfico do EQM para T1 e T2
plt.figure(figsize=(10, 6))
plt.plot(resultados_treinamento[0]['historico_eqm'], label='Treinamento 1 (T1)')
plt.plot(resultados_treinamento[1]['historico_eqm'], label='Treinamento 2 (T2)')
plt.title('Erro Quadrático Médio (EQM) vs Épocas')
plt.xlabel('Épocas')
plt.ylabel('EQM')
plt.legend()
plt.grid(True)
plt.savefig('grafico_eqm.png')
print("\n[!] Gráfico do EQM para T1 e T2 foi salvo como 'grafico_eqm.png'")

print("\n" + "="*80)
print("4. CLASSIFICAÇÃO DAS AMOSTRAS DE TESTE")
print("="*80)
print(f"{'Amostra':<8} | {'y(T1)':<8} | {'y(T2)':<8} | {'y(T3)':<8} | {'y(T4)':<8} | {'y(T5)':<8}")
print("-" * 80)

for i, amostra in enumerate(amostras_teste, 1):
    saidas = []
    for res in resultados_treinamento:
        pesos = res['pesos_finais']
        entradas = [1.0, amostra[0], amostra[1], amostra[2], amostra[3]]
        v = sum(w * e for w, e in zip(pesos, entradas))
        y = funcao_ativacao(v)
        saidas.append(f"{int(y):>6}")
        
    print(f"{i:<8} | {saidas[0]:<8} | {saidas[1]:<8} | {saidas[2]:<8} | {saidas[3]:<8} | {saidas[4]:<8}")

print("\n" + "="*80)
print("5. EXPLICAÇÃO: Por que os pesos convergem para o mesmo lugar?")
print("="*80)
print("Embora o número de épocas varie devido à inicialização diferente dos pesos,")
print("o modelo ADALINE busca minimizar o Erro Quadrático Médio (EQM). Como a função")
print("de custo (EQM) para uma rede de camada única com saída linear é uma superfície")
print("quadrática convexa (um paraboloide multidimensional), ela possui um único")
print("ponto de mínimo global. Assim, independentemente do ponto de partida, o")
print("algoritmo do gradiente descendente (Regra Delta) levará os pesos")
print("inevitavelmente em direção a esse mesmo mínimo global, resultando em")
print("pesos finais praticamente inalterados.")
