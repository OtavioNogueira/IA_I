import json
import csv

# Ler os resultados do JSON
with open('PMC/PMC_1/resultados_pmc1.json', 'r') as f:
    res_json = json.load(f)

# Ler os dados de teste para pegar o d original
dados_teste = []
with open('PMC/PMC_1/dados_teste.csv', 'r') as f:
    leitor = csv.reader(f)
    next(leitor)
    for linha in leitor:
        amostra = int(linha[0])
        d = float(linha[4])
        dados_teste.append((amostra, d))

# Construir as linhas da tabela de validação
tbody_validation = ""
for i, (amostra, d) in enumerate(dados_teste):
    y_t1 = res_json['predicoes']["1"][i]
    y_t2 = res_json['predicoes']["2"][i]
    y_t3 = res_json['predicoes']["3"][i]
    y_t4 = res_json['predicoes']["4"][i]
    y_t5 = res_json['predicoes']["5"][i]
    
    tbody_validation += f"                            <tr><td>{amostra}</td><td>{d:.4f}</td><td>{y_t1:.4f}</td><td>{y_t2:.4f}</td><td>{y_t3:.4f}</td><td>{y_t4:.4f}</td><td>{y_t5:.4f}</td></tr>\n"

# Construir o HTML da nova aba
pmc1_tab_html = f"""
    <!-- TAB PMC 1 -->
    <div id="pmc1" class="tab-content">
        <div class="grid">
            <!-- Contexto do Problema PMC 1 -->
            <div class="card" style="grid-column: 1 / -1;">
                <h2>Contexto do Problema (Ressonância Magnética)</h2>
                <p class="description">
                    Estimar a energia absorvida (y) a partir de três grandezas (x1, x2, x3) para um processador de imagens de ressonância magnética utilizando um <strong>Perceptron Multicamadas (PMC)</strong>. 
                    Topologia utilizada: 3 entradas, 5 neurônios na camada oculta, 1 neurônio na camada de saída. Função de ativação logística em todas as camadas, $\eta = 0.1$, e precisão de $10^{{-6}}$.
                </p>
                <div style="text-align: center; margin-top: 1rem;">
                    <div class="mermaid">
                        graph LR
                            X1(("x1")) --> H1(("h1"))
                            X2(("x2")) --> H1
                            X3(("x3")) --> H1
                            X1 --> H2(("h2"))
                            X2 --> H2
                            X3 --> H2
                            X1 --> H3(("..."))
                            X2 --> H3
                            X3 --> H3
                            H1 --> Y(("y"))
                            H2 --> Y
                            H3 --> Y
                            style Y fill:#10b981,stroke:#fff,stroke-width:2px,color:#fff
                    </div>
                </div>
            </div>

            <!-- Treinamentos -->
            <div class="card" style="grid-column: 1 / -1;">
                <h2>1 e 2. Treinamentos Realizados</h2>
                <p class="description">Foram executados 5 treinamentos com pesos iniciais aleatórios. Abaixo estão os resultados de erro e épocas.</p>
                <div class="table-container">
                    <table>
                        <thead>
                            <tr>
                                <th>Treinamento</th>
                                <th>Erro Quadrático Médio</th>
                                <th>Número de Épocas</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr><td>1º (T1)</td><td>{res_json['treinamentos'][0]['eqm']:.6f}</td><td>{res_json['treinamentos'][0]['epocas']}</td></tr>
                            <tr><td>2º (T2)</td><td>{res_json['treinamentos'][1]['eqm']:.6f}</td><td>{res_json['treinamentos'][1]['epocas']}</td></tr>
                            <tr><td>3º (T3)</td><td>{res_json['treinamentos'][2]['eqm']:.6f}</td><td>{res_json['treinamentos'][2]['epocas']}</td></tr>
                            <tr><td>4º (T4)</td><td>{res_json['treinamentos'][3]['eqm']:.6f}</td><td>{res_json['treinamentos'][3]['epocas']}</td></tr>
                            <tr><td>5º (T5)</td><td>{res_json['treinamentos'][4]['eqm']:.6f}</td><td>{res_json['treinamentos'][4]['epocas']}</td></tr>
                        </tbody>
                    </table>
                </div>
            </div>

            <!-- Gráficos -->
            <div class="card" style="grid-column: 1 / -1;">
                <h2>3. Gráfico do EQM em Função da Época (Piores Casos)</h2>
                <p class="description">Gráfico dos valores de EQM ao longo do treinamento para os dois casos que exigiram mais épocas para convergir (T{res_json['piores_treinos'][0]} e T{res_json['piores_treinos'][1]}).</p>
                <div class="img-container">
                    <img src="PMC/PMC_1/grafico_eqm_pmc1.png" alt="Gráfico EQM vs Épocas para T{res_json['piores_treinos'][0]} e T{res_json['piores_treinos'][1]}">
                </div>
            </div>

            <!-- Discursiva -->
            <div class="card" style="grid-column: 1 / -1;">
                <h2>4. Análise de Variação</h2>
                <div class="answer-block">
                    <h3>Por que o EQM e o número de épocas variam entre os treinamentos?</h3>
                    <p>
                        A variação decorre da <strong>inicialização aleatória dos pesos sinápticos</strong>. Diferente do modelo ADALINE de camada única, cuja superfície de erro é convexa (possuindo apenas um mínimo global), as redes Perceptron Multicamadas (PMC) formam uma superfície de erro complexa, cheia de vales, planaltos e múltiplos <strong>mínimos locais</strong>.
                        <br><br>
                        Dependendo do ponto de partida (pesos iniciais), o algoritmo de <i>backpropagation</i> (descida do gradiente) percorre um caminho diferente através desse espaço de peso, atingindo diferentes pontos de convergência na superfície de erro, resultando em diferentes valores de EQM final e exigindo um número distinto de épocas para satisfazer o critério de parada.
                    </p>
                </div>
            </div>

            <!-- Validação -->
            <div class="card" style="grid-column: 1 / -1;">
                <h2>5 e 6. Validação com Conjunto de Teste</h2>
                <p class="description">Os 5 modelos foram avaliados em 20 amostras de teste não vistas no treinamento. O Erro Relativo (%) e a Variância foram calculados em relação à saída desejada (d).</p>
                <div class="table-container">
                    <table>
                        <thead>
                            <tr>
                                <th>Amostra</th><th>d</th>
                                <th>y(T1)</th><th>y(T2)</th><th>y(T3)</th><th>y(T4)</th><th>y(T5)</th>
                            </tr>
                        </thead>
                        <tbody>
{tbody_validation}                        </tbody>
                        <tfoot>
                            <tr style="background: rgba(255,255,255,0.05);">
                                <td colspan="2" style="font-weight:bold; text-align:right;">Erro Relativo Médio (%)</td>
                                <td>{res_json['treinamentos'][0]['erro_relativo']:.4f}</td><td>{res_json['treinamentos'][1]['erro_relativo']:.4f}</td><td>{res_json['treinamentos'][2]['erro_relativo']:.4f}</td><td>{res_json['treinamentos'][3]['erro_relativo']:.4f}</td><td>{res_json['treinamentos'][4]['erro_relativo']:.4f}</td>
                            </tr>
                            <tr style="background: rgba(255,255,255,0.05);">
                                <td colspan="2" style="font-weight:bold; text-align:right;">Variância (%)</td>
                                <td>{res_json['treinamentos'][0]['variancia']:.4f}</td><td>{res_json['treinamentos'][1]['variancia']:.4f}</td><td>{res_json['treinamentos'][2]['variancia']:.4f}</td><td>{res_json['treinamentos'][3]['variancia']:.4f}</td><td>{res_json['treinamentos'][4]['variancia']:.4f}</td>
                            </tr>
                        </tfoot>
                    </table>
                </div>
                
                <div class="answer-block" style="margin-top: 2rem;">
                    <h3>6. Configuração Mais Adequada</h3>
                    <p>
                        A configuração mais adequada é o <strong>Treinamento 1 (T1)</strong>. Embora o T5 tenha convergido em menos épocas durante o treinamento, o <strong>T1</strong> apresentou o <strong>menor Erro Relativo Médio ({res_json['treinamentos'][0]['erro_relativo']:.4f}%)</strong> quando exposto a dados inéditos (conjunto de teste), demonstrando a melhor capacidade de <strong>generalização</strong> para o sistema de ressonância magnética.
                    </p>
                </div>
            </div>
        </div>
    </div>
"""

with open('index.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# Inserir o novo botão
target_btn = '<button class="tab-btn" onclick="openTab(event, \'adaline\')">ADALINE</button>'
replacement_btn = target_btn + '\n        <button class="tab-btn" onclick="openTab(event, \'pmc1\')">PMC 1</button>'

# Inserir o novo tab-content antes de fechar o container
target_div = '</div>\n\n</body>\n</html>'
replacement_div = pmc1_tab_html + '\n' + target_div

html_content = html_content.replace(target_btn, replacement_btn)
html_content = html_content.replace(target_div, replacement_div)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("index.html atualizado com sucesso!")
