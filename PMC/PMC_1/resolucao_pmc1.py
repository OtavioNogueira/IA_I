import csv
import math
import random
import matplotlib.pyplot as plt

# Funções auxiliares
def sigmoid(v):
    # Clip v to avoid overflow
    v = max(-500, min(v, 500))
    return 1.0 / (1.0 + math.exp(-v))

def sigmoid_derivative_from_output(out):
    return out * (1.0 - out)

# 1. Carregar os dados
def load_data(filename):
    dados = []
    with open(filename, 'r') as f:
        leitor = csv.reader(f)
        next(leitor) # pular o cabeçalho
        for linha in leitor:
            amostra = int(linha[0])
            x1 = float(linha[1])
            x2 = float(linha[2])
            x3 = float(linha[3])
            d = float(linha[4])
            dados.append(([x1, x2, x3], d, amostra))
    return dados

dados_treino = load_data('dados_treinamento.csv')
dados_teste = load_data('dados_teste.csv')

# Parâmetros
num_entradas = 3
num_oculta = 5 # 5 neurônios na camada oculta
num_saida = 1
taxa_aprendizagem = 0.1
precisao = 1e-6
max_epocas = 50000 # Limite de segurança

num_treinamentos = 5
resultados = []

print("Iniciando treinamentos...")

for t in range(1, num_treinamentos + 1):
    print(f"Treinamento {t}...")
    random.seed(t * 100) # Seeds diferentes para cada treinamento
    
    # Inicialização de pesos entre 0 e 1
    # pesos_oculta[j][i] = peso da entrada i para o neurônio j na camada oculta
    pesos_oculta = [[random.random() for _ in range(num_entradas)] for _ in range(num_oculta)]
    bias_oculta = [random.random() for _ in range(num_oculta)]
    
    # pesos_saida[k][j] = peso do neurônio j da oculta para o neurônio k da saída
    pesos_saida = [[random.random() for _ in range(num_oculta)] for _ in range(num_saida)]
    bias_saida = [random.random() for _ in range(num_saida)]
    
    epoca = 0
    eqm_anterior = float('inf')
    historico_eqm = []
    
    while epoca < max_epocas:
        # Embaralhar os dados de treinamento a cada época (opcional, mas ajuda na convergência)
        # random.shuffle(dados_treino) # Omitindo embaralhamento para garantir rastreabilidade estrita, se preferir
        
        # O algoritmo backpropagation atualiza os pesos a cada padrão (online)
        for x, d, _ in dados_treino:
            # --- FORWARD PASS ---
            # Camada Oculta
            out_oculta = []
            for j in range(num_oculta):
                v_j = bias_oculta[j]
                for i in range(num_entradas):
                    v_j += pesos_oculta[j][i] * x[i]
                out_oculta.append(sigmoid(v_j))
                
            # Camada de Saída
            out_saida = []
            for k in range(num_saida):
                v_k = bias_saida[k]
                for j in range(num_oculta):
                    v_k += pesos_saida[k][j] * out_oculta[j]
                out_saida.append(sigmoid(v_k))
                
            # --- BACKWARD PASS ---
            # Gradientes na Camada de Saída
            delta_saida = []
            for k in range(num_saida):
                e_k = d - out_saida[k]
                derivada = sigmoid_derivative_from_output(out_saida[k])
                delta_saida.append(e_k * derivada)
                
            # Gradientes na Camada Oculta
            delta_oculta = []
            for j in range(num_oculta):
                soma_delta = 0.0
                for k in range(num_saida):
                    soma_delta += delta_saida[k] * pesos_saida[k][j]
                derivada = sigmoid_derivative_from_output(out_oculta[j])
                delta_oculta.append(soma_delta * derivada)
                
            # --- ATUALIZAÇÃO DOS PESOS ---
            # Camada de Saída
            for k in range(num_saida):
                bias_saida[k] += taxa_aprendizagem * delta_saida[k]
                for j in range(num_oculta):
                    pesos_saida[k][j] += taxa_aprendizagem * delta_saida[k] * out_oculta[j]
                    
            # Camada Oculta
            for j in range(num_oculta):
                bias_oculta[j] += taxa_aprendizagem * delta_oculta[j]
                for i in range(num_entradas):
                    pesos_oculta[j][i] += taxa_aprendizagem * delta_oculta[j] * x[i]
                    
        # Calcular EQM da época
        eqm_atual = 0.0
        for x, d, _ in dados_treino:
            # Forward
            out_oculta = [sigmoid(bias_oculta[j] + sum(pesos_oculta[j][i] * x[i] for i in range(num_entradas))) for j in range(num_oculta)]
            out_saida = [sigmoid(bias_saida[k] + sum(pesos_saida[k][j] * out_oculta[j] for j in range(num_oculta))) for k in range(num_saida)]
            e_k = d - out_saida[0]
            eqm_atual += e_k ** 2
        eqm_atual /= len(dados_treino)
        
        historico_eqm.append(eqm_atual)
        epoca += 1
        
        # Condição de parada
        if abs(eqm_atual - eqm_anterior) <= precisao:
            break
            
        eqm_anterior = eqm_atual

    resultados.append({
        'treinamento': t,
        'epocas': epoca,
        'eqm': eqm_atual,
        'historico_eqm': historico_eqm,
        'pesos_oculta': pesos_oculta,
        'bias_oculta': bias_oculta,
        'pesos_saida': pesos_saida,
        'bias_saida': bias_saida
    })
    print(f"  -> Concluído em {epoca} épocas. EQM = {eqm_atual:.6f}")

# 2. Registre os resultados em tabela (Console)
print("\n--- RESULTADOS FINAIS ---")
print("Treinamento\tErro Quadrático Médio\tNúmero de Épocas")
for res in resultados:
    print(f"{res['treinamento']}o (T{res['treinamento']})\t{res['eqm']:.6f}\t\t{res['epocas']}")

# 3. Gráficos para os dois com maiores números de épocas
resultados_ordenados = sorted(resultados, key=lambda x: x['epocas'], reverse=True)
top2 = resultados_ordenados[:2]

plt.figure(figsize=(10, 6))
plt.plot(top2[0]['historico_eqm'], label=f"Treinamento {top2[0]['treinamento']} ({top2[0]['epocas']} épocas)")
plt.plot(top2[1]['historico_eqm'], label=f"Treinamento {top2[1]['treinamento']} ({top2[1]['epocas']} épocas)")
plt.title('Erro Quadrático Médio (EQM) vs Épocas (Piores Casos)')
plt.xlabel('Épocas')
plt.ylabel('EQM')
plt.legend()
plt.grid(True)
plt.savefig('grafico_eqm_pmc1.png')
print(f"\n[!] Gráfico gerado para T{top2[0]['treinamento']} e T{top2[1]['treinamento']} salvo em 'grafico_eqm_pmc1.png'.")

# 5. Validação com conjunto de teste
print("\n--- VALIDAÇÃO COM CONJUNTO DE TESTE ---")
# Preparar estrutura para erros relativos
erros_relativos_rede = {t: [] for t in range(1, 6)}
y_redes = {t: [] for t in range(1, 6)}

for x, d, amostra in dados_teste:
    for t in range(1, 6):
        res = resultados[t-1]
        po = res['pesos_oculta']
        bo = res['bias_oculta']
        ps = res['pesos_saida']
        bs = res['bias_saida']
        
        # Forward
        out_oculta = [sigmoid(bo[j] + sum(po[j][i] * x[i] for i in range(num_entradas))) for j in range(num_oculta)]
        out_saida = [sigmoid(bs[k] + sum(ps[k][j] * out_oculta[j] for j in range(num_oculta))) for k in range(num_saida)]
        y_pred = out_saida[0]
        
        y_redes[t].append(y_pred)
        
        erro_relativo = abs((d - y_pred) / d) * 100 if d != 0 else 0
        erros_relativos_rede[t].append(erro_relativo)

# Cálculo da média e variância do erro relativo para cada treinamento
estatisticas_teste = {}
for t in range(1, 6):
    media_erro = sum(erros_relativos_rede[t]) / len(erros_relativos_rede[t])
    variancia = sum((e - media_erro)**2 for e in erros_relativos_rede[t]) / len(erros_relativos_rede[t])
    estatisticas_teste[t] = {'media': media_erro, 'variancia': variancia}
    
print("Amostra\ty(T1)\ty(T2)\ty(T3)\ty(T4)\ty(T5)")
for i, (_, _, amostra) in enumerate(dados_teste):
    s_t1 = f"{y_redes[1][i]:.4f}"
    s_t2 = f"{y_redes[2][i]:.4f}"
    s_t3 = f"{y_redes[3][i]:.4f}"
    s_t4 = f"{y_redes[4][i]:.4f}"
    s_t5 = f"{y_redes[5][i]:.4f}"
    print(f"{amostra}\t{s_t1}\t{s_t2}\t{s_t3}\t{s_t4}\t{s_t5}")

print("\nErro Relativo Médio (%):")
for t in range(1, 6):
    print(f"T{t}: {estatisticas_teste[t]['media']:.4f}%", end="\t")
print("\nVariância (%):")
for t in range(1, 6):
    print(f"T{t}: {estatisticas_teste[t]['variancia']:.4f}", end="\t")
print()

# Salvar estatísticas em JSON para facilitar incorporação no HTML
import json
with open('resultados_pmc1.json', 'w') as f:
    json.dump({
        'treinamentos': [{
            'treinamento': r['treinamento'],
            'eqm': r['eqm'],
            'epocas': r['epocas'],
            'erro_relativo': estatisticas_teste[r['treinamento']]['media'],
            'variancia': estatisticas_teste[r['treinamento']]['variancia']
        } for r in resultados],
        'predicoes': {t: y_redes[t] for t in range(1, 6)},
        'piores_treinos': [top2[0]['treinamento'], top2[1]['treinamento']]
    }, f, indent=4)
