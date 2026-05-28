import os
import numpy as np
import random
import json

# Definindo caminhos
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DOCX_PATH = os.path.join(BASE_DIR, "Kohonen.docx")
JSON_PATH = os.path.join(BASE_DIR, "resultados_kohonen.json")

# 1. Obter e organizar os dados de treino a partir de leitura do docx ou dados estáticos
# Para garantir que o script de resolução funcione de forma totalmente independente,
# vamos embutir o parser nativo do docx diretamente aqui.
import zipfile
import xml.etree.ElementTree as ET

def extrair_dados_docx(docx_path):
    with zipfile.ZipFile(docx_path) as z:
        xml_content = z.read('word/document.xml')
        root = ET.fromstring(xml_content)
        
        namespaces = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
        
        paragraphs = []
        for para in root.findall('.//w:p', namespaces):
            texts = [node.text for node in para.findall('.//w:t', namespaces) if node.text]
            if texts:
                paragraphs.append(''.join(texts))
        
        text = '\n'.join(paragraphs)
        
        # Achar seção de dados
        idx = text.find("Apêndice")
        if idx == -1:
            idx = text.find("Ap\u00eandice") # Fallback unicode
        data_text = text[idx:] if idx != -1 else text
        
        # Extrair números
        all_nums = []
        for word in data_text.split():
            # Limpar caracteres e tentar extrair números
            cleaned = "".join([c for c in word if c.isdigit() or c in '.-'])
            if cleaned:
                try:
                    all_nums.append(float(cleaned))
                except ValueError:
                    pass
        
        # Filtrar apenas inteiros e floats que pareçam IDs e coordenadas
        # O Apêndice contém repetição dos nomes de colunas, removemos lixo inicial
        # Sabendo que a amostra 1 começa com 1, 0.2417, 0.2857, 0.2397, 61, 0.4856, 0.6600, 0.4798
        # Vamos encontrar onde a sequência de números começa com 1 e os próximos floats menores que 1
        start_idx = 0
        for i in range(len(all_nums) - 4):
            if all_nums[i] == 1.0 and all_nums[i+1] < 1.0 and all_nums[i+2] < 1.0 and all_nums[i+3] < 1.0:
                start_idx = i
                break
        
        nums = all_nums[start_idx:]
        
        # Parsear a tabela de duas colunas intercaladas
        amostras = {}
        for i in range(0, len(nums), 8):
            if i + 7 < len(nums):
                # Coluna 1: Amostra A
                id_a = int(nums[i])
                x_a = [nums[i+1], nums[i+2], nums[i+3]]
                amostras[id_a] = x_a
                
                # Coluna 2: Amostra B
                id_b = int(nums[i+4])
                x_b = [nums[i+5], nums[i+6], nums[i+7]]
                amostras[id_b] = x_b
                
        X = np.zeros((120, 3))
        for key in range(1, 121):
            X[key-1] = amostras[key]
        return X

# Extrair os dados
try:
    X_train = extrair_dados_docx(DOCX_PATH)
except Exception as e:
    print(f"Erro ao extrair automaticamente os dados do docx: {e}")
    print("Usando dados de fallback para execução do script...")
    # Caso o script seja rodado fora da pasta ou sem o docx, usamos fallback parcial para compilar
    X_train = np.random.rand(120, 3)

# 2. Configurações do SOM de Kohonen
np.random.seed(42)
random.seed(42)

W = np.random.uniform(0.1, 0.9, (4, 4, 3))
eta = 0.001
epochs = 5000

print("Treinando a Rede de Kohonen (5000 épocas)...")
for epoch in range(epochs):
    indices = np.arange(120)
    np.random.shuffle(indices)
    
    for idx in indices:
        x = X_train[idx]
        dists = np.sum((W - x) ** 2, axis=2)
        winner_idx = np.unravel_index(np.argmin(dists), dists.shape)
        
        # Atualização Chebyshev (raio = 1)
        for r in range(4):
            for c in range(4):
                dist_grid = max(abs(r - winner_idx[0]), abs(c - winner_idx[1]))
                if dist_grid <= 1:
                    W[r, c] += eta * (x - W[r, c])

# 3. Mapear as ativações das amostras de treinamento
activation_map = { (r, c): {"A": 0, "B": 0, "C": 0} for r in range(4) for c in range(4) }
for idx in range(120):
    x = X_train[idx]
    dists = np.sum((W - x) ** 2, axis=2)
    winner_idx = np.unravel_index(np.argmin(dists), dists.shape)
    
    samp_id = idx + 1
    if 1 <= samp_id <= 20:
        c_name = "A"
    elif 21 <= samp_id <= 60:
        c_name = "B"
    else:
        c_name = "C"
    activation_map[winner_idx][c_name] += 1

# Determinar classe majoritária de cada neurônio
neuron_class = {}
for r in range(4):
    for c in range(4):
        counts = activation_map[(r, c)]
        tot = sum(counts.values())
        if tot > 0:
            major_class = max(counts, key=counts.get)
        else:
            major_class = "Vazio"
        neuron_class[(r, c)] = major_class

# Agrupamento de neurônios
neurônios_A = [r*4 + c + 1 for (r, c), cl in neuron_class.items() if cl == "A"]
neurônios_B = [r*4 + c + 1 for (r, c), cl in neuron_class.items() if cl == "B"]
neurônios_C = [r*4 + c + 1 for (r, c), cl in neuron_class.items() if cl == "C"]

print("\n==============================================")
print("MAPEAMENTO DOS NEURÔNIOS NO GRID (1-16):")
print(f"Classe A (Amostras 1-20):   Neurônios {neurônios_A}")
print(f"Classe B (Amostras 21-60):  Neurônios {neurônios_B}")
print(f"Classe C (Amostras 61-120): Neurônios {neurônios_C}")
print("==============================================")

# 4. Classificação das novas amostras de teste
amostras_teste = [
    [0.2471, 0.1778, 0.2905], # 1
    [0.8240, 0.2223, 0.7041], # 2
    [0.4960, 0.7231, 0.5866], # 3
    [0.2923, 0.2041, 0.2234], # 4
    [0.8118, 0.2668, 0.7484], # 5
    [0.4837, 0.8200, 0.4792], # 6
    [0.3248, 0.2629, 0.2375], # 7
    [0.7209, 0.2116, 0.7821], # 8
    [0.5259, 0.6522, 0.5957], # 9
    [0.2075, 0.1669, 0.1745], # 10
    [0.7830, 0.3171, 0.7888], # 11
    [0.5393, 0.7510, 0.5682]  # 12
]

print("\nCLASSIFICAÇÃO DAS AMOSTRAS DE TESTE:")
print(f"{'Amostra':<8} | {'x1':<8} | {'x2':<8} | {'x3':<8} | {'Neurônio BMU':<12} | {'Classe':<6}")
print("-" * 60)
resultados_teste = []
for idx, x_t in enumerate(amostras_teste):
    dists = np.sum((W - x_t) ** 2, axis=2)
    winner_idx = np.unravel_index(np.argmin(dists), dists.shape)
    pred_class = neuron_class[winner_idx]
    
    # Se o neurônio estiver inativo/vazio, pega a classe mais próxima por centroide
    if pred_class == "Vazio":
        dist_classes = {}
        for c_name in ["A", "B", "C"]:
            c_weights = [W[r, c] for (r, c), cl in neuron_class.items() if cl == c_name]
            if c_weights:
                dist_classes[c_name] = np.mean([np.sum((w - x_t) ** 2) for w in c_weights])
        pred_class = min(dist_classes, key=dist_classes.get)
        
    num_neuron = int(winner_idx[0]*4 + winner_idx[1] + 1)
    print(f"{idx+1:<8} | {x_t[0]:<8.4f} | {x_t[1]:<8.4f} | {x_t[2]:<8.4f} | {num_neuron:<12} | {pred_class:<6}")
    
    resultados_teste.append({
        "amostra": idx + 1,
        "x": x_t,
        "winner_neuron": num_neuron,
        "winner_coords": [int(winner_idx[0]), int(winner_idx[1])],
        "classe": pred_class
    })

# Salvar o JSON para a interface gráfica
js_data = {
    "weights": W.tolist(),
    "neuron_classes": {f"{r},{c}": cl for (r, c), cl in neuron_class.items()},
    "simulations": resultados_teste
}

with open(JSON_PATH, "w", encoding='utf-8') as f:
    json.dump(js_data, f, indent=4)

print(f"\nResultados salvos com sucesso em: {JSON_PATH}")
