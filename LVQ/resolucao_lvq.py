import csv
import math

def load_data_train(filename):
    dados = []
    with open(filename, 'r') as f:
        leitor = csv.reader(f)
        next(leitor)
        for linha in leitor:
            x = [float(val) for val in linha[1:7]]
            c = int(linha[7])
            amostra = int(linha[0])
            dados.append((x, c, amostra))
    return dados

def load_data_test(filename):
    dados = []
    with open(filename, 'r') as f:
        leitor = csv.reader(f)
        next(leitor)
        for linha in leitor:
            x = [float(val) for val in linha[1:7]]
            amostra = int(linha[0])
            dados.append((x, amostra))
    return dados

def euclidean_distance(v1, v2):
    return math.sqrt(sum((a - b)**2 for a, b in zip(v1, v2)))

def train_lvq1(dados_treino, alpha_init=0.05, epochs=200):
    # Initialize prototypes as the first sample of each class
    prototypes = {}
    classes = sorted(list(set(item[1] for item in dados_treino)))
    
    for c in classes:
        for x, classe, amostra in dados_treino:
            if classe == c:
                prototypes[c] = x.copy()
                break
                
    initial_prototypes = {c: val.copy() for c, val in prototypes.items()}
    
    alpha = alpha_init
    for epoch in range(1, epochs + 1):
        # We can decay learning rate linearly:
        alpha = alpha_init * (1 - (epoch - 1) / epochs)
        
        for x, classe, amostra in dados_treino:
            # Find the closest prototype
            min_dist = float('inf')
            winning_class = None
            
            for c, w in prototypes.items():
                dist = euclidean_distance(x, w)
                if dist < min_dist:
                    min_dist = dist
                    winning_class = c
            
            # Update the winning prototype
            w_win = prototypes[winning_class]
            if winning_class == classe:
                # Move closer
                for i in range(len(w_win)):
                    w_win[i] += alpha * (x[i] - w_win[i])
            else:
                # Move away
                for i in range(len(w_win)):
                    w_win[i] -= alpha * (x[i] - w_win[i])
                    
    return prototypes, initial_prototypes

if __name__ == "__main__":
    dados_treino = load_data_train("dados_treinamento.csv")
    dados_teste = load_data_test("dados_teste.csv")
    
    epochs = 200
    final_prototypes, initial_prototypes = train_lvq1(dados_treino, alpha_init=0.05, epochs=epochs)
    
    print("=== PESOS INICIAIS DOS PROTÓTIPOS (VETORES DE CÓDIGO) ===")
    for c, w in initial_prototypes.items():
        w_str = ", ".join(f"{val:.4f}" for val in w)
        print(f"Classe {c}: [{w_str}]")
        
    print(f"\n=== PESOS FINAIS DOS PROTÓTIPOS APÓS {epochs} ÉPOCAS ===")
    for c, w in final_prototypes.items():
        w_str = ", ".join(f"{val:.4f}" for val in w)
        print(f"Classe {c}: [{w_str}]")
        
    print("\n=== CLASSIFICAÇÃO DAS AMOSTRAS DE TESTE ===")
    print("Dia\tValores de Potência (7h às 12h)\t\t\t\tClasse Predita")
    print("-" * 80)
    
    resultados_teste = []
    for x, amostra in dados_teste:
        min_dist = float('inf')
        pred_class = None
        for c, w in final_prototypes.items():
            dist = euclidean_distance(x, w)
            if dist < min_dist:
                min_dist = dist
                pred_class = c
        
        x_str = ", ".join(f"{val:.4f}" for val in x)
        print(f"Dia {amostra}\t[{x_str}]\tClasse {pred_class}")
        resultados_teste.append((amostra, x, pred_class))
        
    # Generate JSON results for the UI integration
    import json
    with open("resultados_lvq.json", "w") as f:
        json.dump({
            "prototypes_initial": {c: w for c, w in initial_prototypes.items()},
            "prototypes_final": {c: w for c, w in final_prototypes.items()},
            "test_classification": [
                {"dia": item[0], "x": item[1], "classe": item[2]}
                for item in resultados_teste
            ]
        }, f, indent=4)

    # Gerar gráfico e salvar
    try:
        import matplotlib.pyplot as plt
        plt.figure(figsize=(10, 6))
        
        hours = ['7h', '8h', '9h', '10h', '11h', '12h']
        colors = {1: '#3b82f6', 2: '#f59e0b', 3: '#a78bfa', 4: '#10b981'}
        names = {
            1: 'Classe 1 (Baixa Demanda)',
            2: 'Classe 2 (Pico no Almoço)',
            3: 'Classe 3 (Pico no Fim do Dia)',
            4: 'Classe 4 (Alta Demanda Contínua)'
        }
        
        for c, w in final_prototypes.items():
            plt.plot(hours, w, marker='o', linewidth=3, color=colors[c], label=names[c])
            
        plt.title('LVQ-1: Perfis de Demanda de Potência Elétrica (Protótipos Finais)', fontsize=12, fontweight='bold', pad=15)
        plt.xlabel('Horário', fontsize=10, labelpad=10)
        plt.ylabel('Potência (kW)', fontsize=10, labelpad=10)
        plt.grid(True, linestyle='--', alpha=0.3)
        plt.legend(fontsize=10, loc='best')
        
        plt.tight_layout()
        plt.savefig('grafico_perfis_lvq.png')
        print("\n[!] Gráfico salvo como 'grafico_perfis_lvq.png'.")
    except Exception as e:
        print(f"\n[!] Não foi possível gerar o gráfico: {e}")
