import csv
import math
import random
import time
import matplotlib.pyplot as plt
import json

def sigmoid(v):
    v = max(-500, min(v, 500))
    return 1.0 / (1.0 + math.exp(-v))

def sigmoid_derivative(out):
    return out * (1.0 - out)

def load_data(filename):
    dados = []
    with open(filename, 'r') as f:
        leitor = csv.reader(f)
        next(leitor)
        for linha in leitor:
            amostra = int(linha[0])
            x = [float(val) for val in linha[1:5]]
            d = [float(val) for val in linha[5:8]]
            dados.append((x, d, amostra))
    return dados

dados_treino = load_data('dados_treinamento.csv')
dados_teste = load_data('dados_teste.csv')

num_entradas = 4
num_oculta = 15
num_saida = 3

taxa_aprendizagem = 0.1
fator_momentum = 0.9
precisao = 1e-6
max_epocas = 50000

# Inicialização comum de pesos para garantir a mesma condição inicial
random.seed(42)
pesos_oculta_init = [[random.random() for _ in range(num_entradas)] for _ in range(num_oculta)]
bias_oculta_init = [random.random() for _ in range(num_oculta)]
pesos_saida_init = [[random.random() for _ in range(num_oculta)] for _ in range(num_saida)]
bias_saida_init = [random.random() for _ in range(num_saida)]

resultados = []

def treinar_rede(usar_momentum):
    nome = "Momentum" if usar_momentum else "Padrão"
    print(f"\nIniciando treinamento com Backpropagation {nome}...")
    
    # Copiar os pesos iniciais
    pesos_oculta = [linha[:] for linha in pesos_oculta_init]
    bias_oculta = bias_oculta_init[:]
    pesos_saida = [linha[:] for linha in pesos_saida_init]
    bias_saida = bias_saida_init[:]
    
    # Variáveis para armazenar o delta anterior (para o momentum)
    delta_w_oculta_prev = [[0.0 for _ in range(num_entradas)] for _ in range(num_oculta)]
    delta_b_oculta_prev = [0.0 for _ in range(num_oculta)]
    delta_w_saida_prev = [[0.0 for _ in range(num_oculta)] for _ in range(num_saida)]
    delta_b_saida_prev = [0.0 for _ in range(num_saida)]
    
    epoca = 0
    eqm_anterior = float('inf')
    historico_eqm = []
    
    start_time = time.time()
    
    while epoca < max_epocas:
        eqm_atual = 0.0
        
        # Padrão a padrão
        for x, d, _ in dados_treino:
            # --- FORWARD PASS ---
            out_oculta = []
            for j in range(num_oculta):
                v_j = bias_oculta[j]
                for i in range(num_entradas):
                    v_j += pesos_oculta[j][i] * x[i]
                out_oculta.append(sigmoid(v_j))
                
            out_saida = []
            for k in range(num_saida):
                v_k = bias_saida[k]
                for j in range(num_oculta):
                    v_k += pesos_saida[k][j] * out_oculta[j]
                out_saida.append(sigmoid(v_k))
                
            # --- BACKWARD PASS ---
            delta_saida = []
            for k in range(num_saida):
                e_k = d[k] - out_saida[k]
                delta_saida.append(e_k * sigmoid_derivative(out_saida[k]))
                
            delta_oculta = []
            for j in range(num_oculta):
                soma_delta = sum(delta_saida[k] * pesos_saida[k][j] for k in range(num_saida))
                delta_oculta.append(soma_delta * sigmoid_derivative(out_oculta[j]))
                
            # --- ATUALIZAÇÃO DOS PESOS ---
            for k in range(num_saida):
                # Bias Saída
                delta_b = taxa_aprendizagem * delta_saida[k]
                if usar_momentum:
                    delta_b += fator_momentum * delta_b_saida_prev[k]
                bias_saida[k] += delta_b
                delta_b_saida_prev[k] = delta_b
                
                # Pesos Saída
                for j in range(num_oculta):
                    delta_w = taxa_aprendizagem * delta_saida[k] * out_oculta[j]
                    if usar_momentum:
                        delta_w += fator_momentum * delta_w_saida_prev[k][j]
                    pesos_saida[k][j] += delta_w
                    delta_w_saida_prev[k][j] = delta_w
                    
            for j in range(num_oculta):
                # Bias Oculta
                delta_b = taxa_aprendizagem * delta_oculta[j]
                if usar_momentum:
                    delta_b += fator_momentum * delta_b_oculta_prev[j]
                bias_oculta[j] += delta_b
                delta_b_oculta_prev[j] = delta_b
                
                # Pesos Oculta
                for i in range(num_entradas):
                    delta_w = taxa_aprendizagem * delta_oculta[j] * x[i]
                    if usar_momentum:
                        delta_w += fator_momentum * delta_w_oculta_prev[j][i]
                    pesos_oculta[j][i] += delta_w
                    delta_w_oculta_prev[j][i] = delta_w
                    
        # Calcular EQM da época
        for x, d, _ in dados_treino:
            out_oculta = [sigmoid(bias_oculta[j] + sum(pesos_oculta[j][i] * x[i] for i in range(num_entradas))) for j in range(num_oculta)]
            out_saida = [sigmoid(bias_saida[k] + sum(pesos_saida[k][j] * out_oculta[j] for j in range(num_oculta))) for k in range(num_saida)]
            erro_padrao = sum((d[k] - out_saida[k])**2 for k in range(num_saida)) / num_saida
            eqm_atual += erro_padrao
            
        eqm_atual /= len(dados_treino)
        historico_eqm.append(eqm_atual)
        epoca += 1
        
        if abs(eqm_atual - eqm_anterior) <= precisao:
            break
        eqm_anterior = eqm_atual

    end_time = time.time()
    tempo_processamento = end_time - start_time
    print(f"Concluído em {epoca} épocas. EQM = {eqm_atual:.6f}. Tempo: {tempo_processamento:.2f}s")
    
    return {
        'tipo': nome,
        'epocas': epoca,
        'eqm': eqm_atual,
        'tempo': tempo_processamento,
        'historico_eqm': historico_eqm,
        'pesos_oculta': pesos_oculta,
        'bias_oculta': bias_oculta,
        'pesos_saida': pesos_saida,
        'bias_saida': bias_saida
    }

res_padrao = treinar_rede(usar_momentum=False)
res_momentum = treinar_rede(usar_momentum=True)

# Gerar gráfico (Subplots)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

ax1.plot(res_padrao['historico_eqm'], color='blue', label='BP Padrão')
ax1.set_title('Erro Quadrático Médio - BP Padrão')
ax1.set_xlabel('Épocas')
ax1.set_ylabel('EQM')
ax1.grid(True)
ax1.legend()

ax2.plot(res_momentum['historico_eqm'], color='orange', label='BP Momentum')
ax2.set_title('Erro Quadrático Médio - BP com Momentum')
ax2.set_xlabel('Épocas')
ax2.set_ylabel('EQM')
ax2.grid(True)
ax2.legend()

plt.tight_layout()
plt.savefig('grafico_eqm_pmc2.png')
print("Gráfico comparativo salvo como 'grafico_eqm_pmc2.png'.")

# 3. Pós-processamento e 4. Validação
print("\n--- VALIDAÇÃO COM CONJUNTO DE TESTE ---")

def pos_processamento(y_real):
    return [round(y) for y in y_real]

acertos = 0
resultados_teste = []

for x, d, amostra in dados_teste:
    # Usaremos o modelo Momentum (geralmente mais rápido/robusto, ou o Padrão. O exercício não especifica qual modelo validar, então usaremos o Momentum como o modelo final ou calcularemos para ambos. Vamos validar o Momentum.)
    # O enunciado diz "Faça a validação da rede aplicando o conjunto de teste". Farei com o Padrão e Momentum, ou escolherei Momentum.
    # Vamos avaliar o modelo Momentum.
    po = res_momentum['pesos_oculta']
    bo = res_momentum['bias_oculta']
    ps = res_momentum['pesos_saida']
    bs = res_momentum['bias_saida']
    
    out_oculta = [sigmoid(bo[j] + sum(po[j][i] * x[i] for i in range(num_entradas))) for j in range(num_oculta)]
    out_saida = [sigmoid(bs[k] + sum(ps[k][j] * out_oculta[j] for j in range(num_oculta))) for k in range(num_saida)]
    
    y_arredondado = pos_processamento(out_saida)
    
    d_int = [int(v) for v in d]
    if y_arredondado == d_int:
        acertos += 1
        
    resultados_teste.append({
        'amostra': amostra,
        'd': d_int,
        'y_raw': out_saida,
        'y_round': y_arredondado
    })

taxa_acerto = (acertos / len(dados_teste)) * 100
print(f"Taxa de Acerto: {taxa_acerto:.2f}%")

with open('resultados_pmc2.json', 'w') as f:
    json.dump({
        'treinamentos': [
            {
                'tipo': res_padrao['tipo'],
                'epocas': res_padrao['epocas'],
                'eqm': res_padrao['eqm'],
                'tempo': res_padrao['tempo']
            },
            {
                'tipo': res_momentum['tipo'],
                'epocas': res_momentum['epocas'],
                'eqm': res_momentum['eqm'],
                'tempo': res_momentum['tempo']
            }
        ],
        'teste': resultados_teste,
        'taxa_acerto': taxa_acerto
    }, f, indent=4)
