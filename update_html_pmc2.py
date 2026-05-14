import json

with open('PMC/PMC_2/resultados_pmc2.json', 'r') as f:
    res = json.load(f)

t_padrao = res['treinamentos'][0]
t_momentum = res['treinamentos'][1]

tbody_validation = ""
for item in res['teste']:
    amostra = item['amostra']
    d1, d2, d3 = item['d']
    y1, y2, y3 = item['y_round']
    raw1, raw2, raw3 = item['y_raw']
    # Para economizar espaço visual, vamos omitir os raws da tabela e focar nos arredondados
    tbody_validation += f"                            <tr><td>{amostra}</td><td>{d1}</td><td>{d2}</td><td>{d3}</td><td style='border-left: 2px solid rgba(255,255,255,0.1);'>{y1}</td><td>{y2}</td><td>{y3}</td></tr>\n"

taxa_acerto = res['taxa_acerto']

pmc2_html = f"""
    <!-- TAB PMC 2 -->
    <div id="pmc2" class="tab-content">
        <div class="grid">
            <!-- Contexto do Problema PMC 2 -->
            <div class="card" style="grid-column: 1 / -1;">
                <h2>Contexto do Problema (Processamento de Bebidas)</h2>
                <p class="description">
                    Nesta atividade, a rede Perceptron Multicamadas (PMC) foi utilizada para classificar o tipo de conservante (A, B ou C) a ser aplicado em bebidas, baseado em 4 variáveis reais (Teor de Água, Grau de Acidez, Temperatura e Tensão Superficial).
                    A topologia tem 4 neurônios de entrada, 15 neurônios na camada oculta, e 3 neurônios de saída, com codificação *one-hot* para a classe.
                    <br><br>
                    O objetivo foi comparar o algoritmo de <strong>Backpropagation Padrão</strong> com o <strong>Backpropagation com Momentum</strong> (fator = 0.9), ambos partindo dos mesmos pesos iniciais e $\eta = 0.1$.
                </p>
                <div style="text-align: center; margin-top: 1rem;">
                    <div class="mermaid">
                        graph LR
                            X1(("x1")) --> H1(("h1"))
                            X2(("x2")) --> H1
                            X3(("x3")) --> H1
                            X4(("x4")) --> H1
                            H1 --> Y1(("y1 (A)"))
                            H1 --> Y2(("y2 (B)"))
                            H1 --> Y3(("y3 (C)"))
                            style Y1 fill:#10b981,stroke:#fff,stroke-width:2px,color:#fff
                            style Y2 fill:#3b82f6,stroke:#fff,stroke-width:2px,color:#fff
                            style Y3 fill:#8b5cf6,stroke:#fff,stroke-width:2px,color:#fff
                    </div>
                </div>
            </div>

            <!-- Treinamentos -->
            <div class="card" style="grid-column: 1 / -1;">
                <h2>1 e 2. Padrão vs Momentum</h2>
                <p class="description">Resultados de convergência para a precisão de $10^{{-6}}$ e o respectivo tempo de processamento.</p>
                <div class="table-container">
                    <table>
                        <thead>
                            <tr>
                                <th>Algoritmo</th>
                                <th>Épocas</th>
                                <th>Tempo de Processamento (s)</th>
                                <th>EQM Final</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr><td>Backpropagation Padrão</td><td>{t_padrao['epocas']}</td><td>{t_padrao['tempo']:.2f} s</td><td>{t_padrao['eqm']:.6f}</td></tr>
                            <tr><td>Backpropagation com Momentum</td><td style="color: var(--success); font-weight: bold;">{t_momentum['epocas']}</td><td style="color: var(--success); font-weight: bold;">{t_momentum['tempo']:.2f} s</td><td>{t_momentum['eqm']:.6f}</td></tr>
                        </tbody>
                    </table>
                </div>
            </div>

            <!-- Gráficos -->
            <div class="card" style="grid-column: 1 / -1;">
                <h2>Gráficos de EQM vs Épocas</h2>
                <p class="description">Comparativo não-superposto da evolução do Erro Quadrático Médio.</p>
                <div class="img-container">
                    <img src="PMC/PMC_2/grafico_eqm_pmc2.png" alt="Gráfico EQM vs Épocas (Padrão vs Momentum)">
                </div>
                <div class="answer-block" style="margin-top: 1rem;">
                    <h3>Análise de Desempenho</h3>
                    <p>
                        A inserção do termo de <i>Momentum</i> na regra de atualização dos pesos acelera dramaticamente o treinamento (reduzindo em quase 7 vezes o número de épocas e o tempo de execução neste caso). Ele atua como um filtro passa-baixa estabilizando a trajetória do gradiente, evitando que a rede fique presa em mínimos locais rasos ou oscile excessivamente em desfiladeiros da superfície de erro.
                    </p>
                </div>
            </div>

            <!-- Validação -->
            <div class="card" style="grid-column: 1 / -1;">
                <h2>3 e 4. Validação e Pós-Processamento</h2>
                <p class="description">
                    Aplicando o critério de arredondamento simétrico (pos-processamento), a rede foi exposta a 18 amostras de teste inéditas. Abaixo, a comparação entre a classe desejada (d) e a classe predita (y).
                </p>
                <div class="table-container">
                    <table>
                        <thead>
                            <tr>
                                <th>Amostra</th>
                                <th>d1</th><th>d2</th><th>d3</th>
                                <th style="border-left: 2px solid rgba(255,255,255,0.1);">y1</th><th>y2</th><th>y3</th>
                            </tr>
                        </thead>
                        <tbody>
{tbody_validation}                        </tbody>
                        <tfoot>
                            <tr style="background: rgba(255,255,255,0.05);">
                                <td colspan="7" style="font-weight:bold; text-align:center; color: var(--success); font-size: 1.2rem;">Taxa de Acerto Global: {taxa_acerto:.2f}%</td>
                            </tr>
                        </tfoot>
                    </table>
                </div>
            </div>
        </div>
    </div>
"""

with open('index.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

target_btn = '<button class="tab-btn" onclick="openTab(event, \'pmc1\')">PMC 1</button>'
replacement_btn = target_btn + '\n        <button class="tab-btn" onclick="openTab(event, \'pmc2\')">PMC 2</button>'

target_div = '</div>\n\n</body>\n</html>'
replacement_div = pmc2_html + '\n' + target_div

html_content = html_content.replace(target_btn, replacement_btn)
html_content = html_content.replace(target_div, replacement_div)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("index.html atualizado com PMC 2.")
