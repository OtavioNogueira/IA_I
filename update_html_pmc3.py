import json

with open('PMC/PMC_3/resultados_pmc3.json', 'r') as f:
    res = json.load(f)

# Build Training Table
t_rows = ""
for id_t in ['T1', 'T2', 'T3']:
    row = f"<tr><td>{id_t}</td>"
    for rede in ['Rede 1', 'Rede 2', 'Rede 3']:
        eqm = res['treinamentos'][rede][id_t]['eqm']
        ep = res['treinamentos'][rede][id_t]['epocas']
        row += f"<td>{eqm:.6f}</td><td>{ep}</td>"
    row += "</tr>\n"
    t_rows += row

# Build Validation Table
v_rows = ""
for t in range(101, 121):
    t_str = str(t)
    f_t = res['validacao'][t_str]['f_t']
    row = f"<tr><td>t = {t}</td><td>{f_t:.4f}</td>"
    for rede in ['Rede 1', 'Rede 2', 'Rede 3']:
        for id_t in ['T1', 'T2', 'T3']:
            y = res['validacao'][t_str][rede][id_t]
            row += f"<td>{y:.4f}</td>"
    row += "</tr>\n"
    v_rows += row

err_row = "<tr><td colspan='2' style='font-weight:bold; text-align:right;'>Erro Relativo Médio (%)</td>"
var_row = "<tr><td colspan='2' style='font-weight:bold; text-align:right;'>Variância (%)</td>"

for rede in ['Rede 1', 'Rede 2', 'Rede 3']:
    for id_t in ['T1', 'T2', 'T3']:
        err = res['estatisticas'][rede][id_t]['erro_medio']
        vari = res['estatisticas'][rede][id_t]['variancia']
        err_row += f"<td>{err:.2f}</td>"
        var_row += f"<td>{vari:.2f}</td>"
err_row += "</tr>\n"
var_row += "</tr>\n"

melhor_r1 = res['melhores']['Rede 1']
melhor_r2 = res['melhores']['Rede 2']
melhor_r3 = res['melhores']['Rede 3']

pmc3_html = f"""
    <!-- TAB PMC 3 -->
    <div id="pmc3" class="tab-content">
        <div class="grid">
            <!-- Contexto PMC 3 -->
            <div class="card" style="grid-column: 1 / -1;">
                <h2>Contexto do Problema (Time Delay Neural Network)</h2>
                <p class="description">
                    Previsão do preço de uma mercadoria no mercado de ações utilizando um Perceptron Multicamadas configurado como <strong>TDNN (Time Delay)</strong>. Para prever a amostra no instante <i>t</i>, a rede utiliza as amostras dos <i>p</i> instantes anteriores: $x(t-1), x(t-2), \dots, x(t-p)$.
                    <br><br>
                    <strong>Três topologias avaliadas:</strong><br>
                    - <strong>Rede 1:</strong> 5 entradas (p=5), 10 neurônios ocultos.<br>
                    - <strong>Rede 2:</strong> 10 entradas (p=10), 15 neurônios ocultos.<br>
                    - <strong>Rede 3:</strong> 15 entradas (p=15), 25 neurônios ocultos.<br><br>
                    Algoritmo de treinamento: <strong>Backpropagation com Momentum</strong> ($\eta = 0.1$, $\alpha = 0.8$, $precisão = 0.5 \\times 10^{{-6}}$). Foram realizados 3 treinamentos (T1, T2, T3) para cada topologia, com pesos iniciais aleatórios entre 0 e 1.
                </p>
            </div>

            <!-- Treinamentos -->
            <div class="card" style="grid-column: 1 / -1; overflow-x: auto;">
                <h2>1 e 2. Resultados dos Treinamentos</h2>
                <p class="description">Tabela comparativa do número de épocas e Erro Quadrático Médio final para todas as 9 execuções.</p>
                <div class="table-container">
                    <table>
                        <thead>
                            <tr>
                                <th rowspan="2">Treinamento</th>
                                <th colspan="2" style="text-align:center;">Rede 1</th>
                                <th colspan="2" style="text-align:center;">Rede 2</th>
                                <th colspan="2" style="text-align:center;">Rede 3</th>
                            </tr>
                            <tr>
                                <th>EQM</th><th>Épocas</th>
                                <th>EQM</th><th>Épocas</th>
                                <th>EQM</th><th>Épocas</th>
                            </tr>
                        </thead>
                        <tbody>
{t_rows}                        </tbody>
                    </table>
                </div>
            </div>

            <!-- Validação -->
            <div class="card" style="grid-column: 1 / -1; overflow-x: auto;">
                <h2>3. Validação da Rede (t=101 a 120)</h2>
                <p class="description">Desempenho da rede em dados inéditos. O conjunto de teste utiliza as amostras históricas exatas para preencher as janelas de delay.</p>
                <div class="table-container">
                    <table style="font-size: 0.9em;">
                        <thead>
                            <tr>
                                <th rowspan="2">Amostra</th>
                                <th rowspan="2">f(t)</th>
                                <th colspan="3" style="text-align:center;">Rede 1</th>
                                <th colspan="3" style="text-align:center;">Rede 2</th>
                                <th colspan="3" style="text-align:center;">Rede 3</th>
                            </tr>
                            <tr>
                                <th>T1</th><th>T2</th><th>T3</th>
                                <th>T1</th><th>T2</th><th>T3</th>
                                <th>T1</th><th>T2</th><th>T3</th>
                            </tr>
                        </thead>
                        <tbody>
{v_rows}                        </tbody>
                        <tfoot>
{err_row}{var_row}                        </tfoot>
                    </table>
                </div>
            </div>

            <!-- Gráficos -->
            <div class="card" style="grid-column: 1 / -1;">
                <h2>4. Gráfico do EQM em Função da Época</h2>
                <p class="description">Evolução do Erro Quadrático Médio ao longo do treinamento para o melhor caso de cada topologia.</p>
                <div class="img-container">
                    <img src="PMC/PMC_3/grafico_eqm_pmc3.png" alt="Gráfico EQM vs Épocas PMC 3">
                </div>
            </div>

            <div class="card" style="grid-column: 1 / -1;">
                <h2>5. Previsões (Valores Desejados vs Estimados)</h2>
                <p class="description">Comparação visual entre o valor histórico real f(t) e a previsão y(t) gerada pela rede no domínio de estimação para o melhor treinamento.</p>
                <div class="img-container">
                    <img src="PMC/PMC_3/grafico_validacao_pmc3.png" alt="Gráfico Validação PMC 3">
                </div>
            </div>

            <!-- Discursivas -->
            <div class="card" style="grid-column: 1 / -1;">
                <h2>6. Configuração Mais Adequada</h2>
                <div class="answer-block">
                    <p>
                        A configuração mais adequada para realizar previsões neste processo é a <strong>Rede 2 (p=10, N1=15) com o treinamento {melhor_r2}</strong>.
                        <br><br>
                        <strong>Justificativa:</strong> A <strong>Rede 1</strong> apresentou um erro relativo na casa dos 20%, o que indica um underfitting (baixa capacidade de mapear a complexidade temporal com apenas 5 entradas). A <strong>Rede 3</strong> sofreu um colapso drástico (convergindo prematuramente em 2 épocas e apresentando um erro relativo de mais de 1000%). Isso ocorre porque, ao possuir 15 entradas e 25 neurônios ocultos com pesos iniciais positivos (0 a 1), as combinações lineares explodiram, saturando os neurônios sigmoides. Quando um neurônio sigmoide satura (saída próxima a 1), a sua derivada se aproxima de 0, causando o fenômeno do <i>Vanishing Gradient</i> (Gradiente Desvanescente) e impedindo qualquer aprendizado.
                        <br><br>
                        A <strong>Rede 2</strong> foi o balanço ideal: evitou a saturação severa presente na Rede 3 e teve memória temporal suficiente (p=10) para modelar a série de maneira superior à Rede 1, atingindo o menor erro relativo médio ($\sim 8.89\%$).
                    </p>
                </div>
            </div>

            <div class="card" style="grid-column: 1 / -1;">
                <h2>7. Variantes do Algoritmo Backpropagation</h2>
                <div class="answer-block">
                    <h3>a. Algoritmo Resilient-Propagation (RProp)</h3>
                    <p>
                        O RProp é um algoritmo adaptativo focado em superar o principal gargalo do Backpropagation padrão com funções logísticas: o achatamento do gradiente (como observado na Rede 3). Em vez de usar a magnitude da derivada para atualizar o peso, o RProp utiliza <strong>apenas o sinal (direção) do gradiente</strong>. Cada peso possui uma taxa de atualização individual ($\Delta_{{ij}}$). Se o gradiente mantiver o mesmo sinal por duas épocas seguidas, $\Delta_{{ij}}$ aumenta (acelerando em superfícies planas). Se o sinal inverter, ele diminui (evitando pular o mínimo).
                        <strong>Vantagem:</strong> Convergência consideravelmente mais rápida e robusta contra gradientes desvanescentes, pois atualiza ativamente os pesos mesmo nas extremidades saturadas da função sigmoide.
                    </p>
                    
                    <h3 style="margin-top: 1.5rem;">b. Algoritmo Levenberg-Marquardt (LM)</h3>
                    <p>
                        O Levenberg-Marquardt atua misturando o método do Gradiente Descendente e o método de Gauss-Newton. Em vez de calcular derivadas segundas complexas (Matriz Hessiana), ele as aproxima utilizando a Matriz Jacobiana ($H \approx J^T J$). A regra de atualização possui um parâmetro de amortecimento ($\mu$) que regula entre se comportar como Gradiente Descendente (quando longe do mínimo) e Gauss-Newton (quando muito próximo ao mínimo).
                        <strong>Vantagem:</strong> É indiscutivelmente o algoritmo de treinamento mais rápido que existe para redes neurais de pequeno a médio porte (como a maioria das PMCs). Sua convergência é extremamente acelerada perto da solução ótima. A principal desvantagem é o alto custo de memória para armazenar e inverter a matriz Jacobiana em redes muito grandes.
                    </p>
                </div>
            </div>
        </div>
    </div>
"""

with open('index.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

target_btn = '<button class="tab-btn" onclick="openTab(event, \'pmc2\')">PMC 2</button>'
replacement_btn = target_btn + '\n        <button class="tab-btn" onclick="openTab(event, \'pmc3\')">PMC 3</button>'

target_div = '</div>\n\n</body>\n</html>'
replacement_div = pmc3_html + '\n' + target_div

html_content = html_content.replace(target_btn, replacement_btn)
html_content = html_content.replace(target_div, replacement_div)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("index.html atualizado com PMC 3.")
