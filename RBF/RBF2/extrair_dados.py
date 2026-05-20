import re

with open('/home/alunos/Desktop/ubuntu/RBF/RBF2/RBF2_extracted.md', 'r') as f:
    text = f.read()

# Dados de Teste
# Amostra | x1 | x2 | x3 | d
teste_str = """
01 0.5102 0.7464 0.0860 0.5965
02 0.8401 0.4490 0.2719 0.6790
03 0.1283 0.1882 0.7253 0.4662
04 0.2299 0.1524 0.7353 0.5012
05 0.3209 0.6229 0.5233 0.6810
06 0.8203 0.0682 0.4260 0.5643
07 0.3471 0.8889 0.1564 0.5875
08 0.5762 0.8292 0.4116 0.7853
09 0.9053 0.6245 0.5264 0.8506
10 0.8149 0.0396 0.6227 0.6165
11 0.1016 0.6382 0.3173 0.4957
12 0.9108 0.2139 0.4641 0.6625
13 0.2245 0.0971 0.6136 0.4402
14 0.6423 0.3229 0.8567 0.7663
15 0.5252 0.6529 0.5729 0.7893
"""

teste_data = []
for line in teste_str.strip().split('\n'):
    parts = line.split()
    teste_data.append([float(x) for x in parts[1:5]]) # ignorando o índice

# Dados de Treinamento
# Estão abaixo de "## ANEXO"
anexo_part = text.split('## ANEXO')[1]

# Encontrar tds os números com regex
nums = re.findall(r'\b\d+\.\d+\b|\b\d+\b', anexo_part)

treino_data_temp = []
for n in nums:
    treino_data_temp.append(float(n))

# Organizar: [ID, x1, x2, x3, d]
# Como a tabela é (ID, x1, x2, x3, d, ID, x1, x2, x3, d, ID, x1, x2, x3, d)
treino_data = []
i = 0
while i + 4 < len(treino_data_temp):
    try:
        if treino_data_temp[i] <= 150: # É o ID
            treino_data.append([treino_data_temp[i+1], treino_data_temp[i+2], treino_data_temp[i+3], treino_data_temp[i+4]])
            i += 5
        else:
            i += 1
    except IndexError:
        break

print(f"Total Teste: {len(teste_data)}")
print(f"Total Treino: {len(treino_data)}")
import json
with open('/home/alunos/Desktop/ubuntu/RBF/RBF2/teste.json', 'w') as f:
    json.dump(teste_data, f)
with open('/home/alunos/Desktop/ubuntu/RBF/RBF2/treino.json', 'w') as f:
    json.dump(treino_data, f)

