import csv

def load_data(filename):
    dados = []
    with open(filename, 'r') as f:
        leitor = csv.reader(f)
        next(leitor)
        for linha in leitor:
            x = [int(val) for val in linha[1:]]
            amostra = int(linha[0])
            dados.append((x, amostra))
    return dados

def train_art1(dados, rho, L=2.0):
    N = 16  # dimension of input
    M = len(dados)  # max categories
    
    # Initialize weights
    # Bottom-up weights
    b = [[1.0 / (1.0 + N) for _ in range(M)] for _ in range(N)]
    # Top-down weights
    t = [[1.0 for _ in range(N)] for _ in range(M)]
    
    committed = [False] * M
    
    epochs = 0
    max_epochs = 100
    
    while epochs < max_epochs:
        changed = False
        for x, amostra in dados:
            inhibited = [False] * M
            while True:
                # Calculate activations y_j
                y = []
                for j in range(M):
                    if inhibited[j]:
                        y.append(-1.0)
                    else:
                        val = sum(b[i][j] * x[i] for i in range(N))
                        y.append(val)
                
                max_y = max(y)
                if max_y < 0:
                    break
                
                J = y.index(max_y)
                
                # Test for resonance
                x_star = [x[i] * t[J][i] for i in range(N)]
                sum_x_star = sum(x_star)
                sum_x = sum(x)
                ratio = sum_x_star / sum_x if sum_x > 0 else 1.0
                
                if ratio >= rho:
                    # Resonance!
                    old_t = t[J].copy()
                    old_b = [b[i][J] for i in range(N)]
                    
                    # Update weights for winning category J
                    for i in range(N):
                        t[J][i] = x_star[i]
                        b[i][J] = (L * x_star[i]) / (L - 1.0 + sum_x_star)
                    
                    committed[J] = True
                    
                    if old_t != t[J] or any(old_b[i] != b[i][J] for i in range(N)):
                        changed = True
                    break
                else:
                    # Reset
                    inhibited[J] = True
        
        epochs += 1
        if not changed:
            break
            
    # Group the patterns using the final weights
    groupings = {}
    for x, amostra in dados:
        inhibited = [False] * M
        while True:
            y = []
            for j in range(M):
                if inhibited[j] or not committed[j]:
                    y.append(-1.0)
                else:
                    val = sum(b[i][j] * x[i] for i in range(N))
                    y.append(val)
            
            max_y = max(y)
            if max_y < 0:
                # If no committed category matches or resonances, it would go to a new one
                # but since it's testing, let's see which category it fits.
                J = -1
                break
            
            J = y.index(max_y)
            
            # Verify resonance
            x_star = [x[i] * t[J][i] for i in range(N)]
            sum_x_star = sum(x_star)
            sum_x = sum(x)
            ratio = sum_x_star / sum_x if sum_x > 0 else 1.0
            
            if ratio >= rho:
                break
            else:
                inhibited[J] = True
                
        if J == -1:
            # If it doesn't fit any trained category, it remains unclassified or forms its own
            J = "Novo / Nao classificado"
            
        if J not in groupings:
            groupings[J] = []
        groupings[J].append(amostra)
        
    return groupings, epochs

if __name__ == "__main__":
    dados = load_data("dados.csv")
    vigilance_values = [0.5, 0.8, 0.9, 0.99]
    
    classes_ativas = []
    print("=== RESULTADOS SIMULAÇÕES ART-1 ===")
    for rho in vigilance_values:
        groupings, epochs = train_art1(dados, rho)
        classes_ativas.append(len(groupings))
        # Rename categories for readability (e.g. C1, C2...)
        sorted_keys = sorted([k for k in groupings.keys() if isinstance(k, int)])
        cat_map = {old: f"Classe {i+1}" for i, old in enumerate(sorted_keys)}
        if "Novo / Nao classificado" in groupings:
            cat_map["Novo / Nao classificado"] = "Não classificado"
            
        print(f"\nGrau de Vigilância (rho) = {rho}")
        print(f"Número de épocas para convergência: {epochs}")
        print(f"Classes ativas: {len(groupings)}")
        for k, v in groupings.items():
            class_name = cat_map.get(k, str(k))
            print(f"  {class_name}: Situações {v}")

    # Gerar gráfico e salvar
    try:
        import matplotlib.pyplot as plt
        plt.figure(figsize=(8, 5))
        bars = plt.bar([str(r) for r in vigilance_values], classes_ativas, color=['#3b82f6', '#10b981', '#f59e0b', '#ef4444'], width=0.5)
        plt.title('ART-1: Número de Classes Ativas vs. Limiar de Vigilância (rho)', fontsize=12, fontweight='bold', pad=15)
        plt.xlabel('Grau de Vigilância (rho)', fontsize=10, labelpad=10)
        plt.ylabel('Classes Ativas', fontsize=10, labelpad=10)
        plt.grid(axis='y', linestyle='--', alpha=0.3)
        plt.ylim(0, 10)
        
        # Add values on top of bars
        for bar in bars:
            yval = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2.0, yval + 0.3, str(yval), ha='center', va='bottom', fontweight='bold')
            
        plt.tight_layout()
        plt.savefig('grafico_classes_art1.png')
        print("\n[!] Gráfico salvo como 'grafico_classes_art1.png'.")
    except Exception as e:
        print(f"\n[!] Não foi possível gerar o gráfico: {e}")
