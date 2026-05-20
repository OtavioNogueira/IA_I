+---------+---+--------------+----------+-------------------+----+-------+
| ![Lo    |   | **Centro     |          |                   |    |       |
| gotipo, |   | Federal de   |          |                   |    |       |
| nome da |   | Educação     |          |                   |    |       |
| empresa |   | Tecnológica  |          |                   |    |       |
| De      |   | de Minas     |          |                   |    |       |
| scrição |   | Gerais**     |          |                   |    |       |
| gerada  |   |              |          |                   |    |       |
| a       |   | ***Campus    |          |                   |    |       |
| utomati |   | VIII --      |          |                   |    |       |
| camente |   | Varginha***  |          |                   |    |       |
| ](media |   |              |          |                   |    |       |
| /image1 |   | *            |          |                   |    |       |
| .jpeg){ |   | *Bacharelado |          |                   |    |       |
| width=" |   | em Sistemas  |          |                   |    |       |
| 0.77152 |   | de           |          |                   |    |       |
| 7777777 |   | Informação** |          |                   |    |       |
| 7778in" |   |              |          |                   |    |       |
| he      |   |              |          |                   |    |       |
| ight="0 |   |              |          |                   |    |       |
| .484722 |   |              |          |                   |    |       |
| 2222222 |   |              |          |                   |    |       |
| 222in"} |   |              |          |                   |    |       |
+---------+---+--------------+----------+-------------------+----+-------+
| **      |   |              | **TR     | ***Professor***   | *  | ***No |
| *Discip |   |              | ABALHO** |                   | ** | ta*** |
| lina*** |   |              |          | Lázaro Eduardo da | Va |       |
|         |   |              |          | Silva             | lo |       |
| Lab.    |   |              |          |                   | r* |       |
| Intel   |   |              |          |                   | ** |       |
| igência |   |              |          |                   |    |       |
| Art     |   |              |          |                   | 10 |       |
| ificial |   |              |          |                   | 0% |       |
+---------+---+--------------+----------+-------------------+----+-------+
| ***D    | * |              |          |                   |    |       |
| ata:*** | * |              |          |                   |    |       |
|         | * |              |          |                   |    |       |
| 20/     | A |              |          |                   |    |       |
| 05/2026 | l |              |          |                   |    |       |
|         | u |              |          |                   |    |       |
|         | n |              |          |                   |    |       |
|         | o |              |          |                   |    |       |
|         | ( |              |          |                   |    |       |
|         | a |              |          |                   |    |       |
|         | ) |              |          |                   |    |       |
|         | : |              |          |                   |    |       |
|         | * |              |          |                   |    |       |
|         | * |              |          |                   |    |       |
|         | * |              |          |                   |    |       |
+---------+---+--------------+----------+-------------------+----+-------+

A quantidade de gasolina {*y*} a ser injetada por um sistema de injeção
eletrônica de combustível para veículos automotores pode ser computada
em tempo-real em função de três grandezas {*x*~1~ , *x*~2~ , *x*~3~}.
Devido à complexidade inerente do processo, configurado como um sistema
não-linear, pretende-se utilizar uma rede neural artificial para o
mapeamento entre as entradas e a saída do processo.

Sabe-se que para efetuar o respectivo mapeamento, o qual se configura
como um problema de aproximação funcional, duas potenciais arquiteturas
podem ser aplicadas, a saber, o perceptron multicamadas ou a RBF. Dado
que a equipe de engenheiros e cientistas já realizaram o mapeamento do
problema através do perceptron multicamadas, o objetivo agora é treinar
uma RBF a fim de que os resultados fornecidos por ambas as arquiteturas
possam ser contrastados.

Assim, efetue o treinamento de uma RBF com o objetivo de computar a
quantidade de gasolina {*y*} a ser injetada pelo sistema de injeção
eletrônica em função das variáveis {*x*~1~ , *x*~2~ , *x*~3~}. A
topologia da rede RBF está ilustrada na figura abaixo.

As topologias candidatas de RBF para serem aplicadas no mapeamento do
problema acima são especificadas como se segue:

**Rede 1** RBF com N1 = 05

**Rede 2** RBF com N1 = 10

**Rede 3** RBF com N1 = 15

Utilizando os dados de treinamento apresentados no Anexo, execute o
treinamento das redes RBF conforme as topologias definidas acima. Para
tanto, faça as seguintes atividades:

1.  Execute 3 treinamentos para cada topologia de rede RBF definida
    anteriormente, inicializando a matriz de pesos da camada de saída
    com valores aleatórios entre 0 e 1. Se for o caso, reinicie o
    gerador de números aleatórios em cada treinamento de tal forma que
    os elementos das matrizes de pesos iniciais não sejam os mesmos.
    Utilize uma taxa de aprendizado η = 0.01 e precisão ε = 10^-7^.

2.  Registre os resultados finais desses 3 treinamentos para cada uma
    das três topologias de rede na tabela a seguir:

  ------------- ----------- -------- ---------- -------- -------- ----------
  Treinamento   **Rede 1**           **Rede 2**          **Rede   
                                                         3**      

                EQM         Épocas   EQM        Épocas   EQM      Épocas

  1^o^ (T1)                                                       

  2^o^ (T2)                                                       

  3^o^ (T3)                                                       
  ------------- ----------- -------- ---------- -------- -------- ----------

3.  Para todos os treinamentos efetuados no item 2, faça a validação da
    rede em relação aos valores desejados apresentados na tabela abaixo.
    Forneça para cada treinamento o erro relativo médio (%) entre os
    valores desejados e os valores fornecidos pela rede em relação a
    todos os padrões de teste. Obtenha também a respectiva variância
    (%).

  ----------- -------- -------- -------- -------- -------- ------ ------ -------- ------ ------ -------- ------ ------
                                                  **Rede                 **Rede                 **Rede          
                                                  1**                    2**                    3**             

  Amostra     *x*~1~   *x*~2~   *x*~3~   *d*      *y* (T1) *y*    *y*    *y* (T1) *y*    *y*    *y* (T1) *y*    *y*
                                                           (T2)   (T3)            (T2)   (T3)            (T2)   (T3)

  01          0.5102   0.7464   0.0860   0.5965                                                                 

  02          0.8401   0.4490   0.2719   0.6790                                                                 

  03          0.1283   0.1882   0.7253   0.4662                                                                 

  04          0.2299   0.1524   0.7353   0.5012                                                                 

  05          0.3209   0.6229   0.5233   0.6810                                                                 

  06          0.8203   0.0682   0.4260   0.5643                                                                 

  07          0.3471   0.8889   0.1564   0.5875                                                                 

  08          0.5762   0.8292   0.4116   0.7853                                                                 

  09          0.9053   0.6245   0.5264   0.8506                                                                 

  10          0.8149   0.0396   0.6227   0.6165                                                                 

  11          0.1016   0.6382   0.3173   0.4957                                                                 

  12          0.9108   0.2139   0.4641   0.6625                                                                 

  13          0.2245   0.0971   0.6136   0.4402                                                                 

  14          0.6423   0.3229   0.8567   0.7663                                                                 

  15          0.5252   0.6529   0.5729   0.7893                                                                 

  Erro                                                                                                          
  Relativo                                                                                                      
  Médio (%):                                                                                                    

  Variância                                                                                                     
  (%):                                                                                                          
  ----------- -------- -------- -------- -------- -------- ------ ------ -------- ------ ------ -------- ------ ------

4.  Para cada uma das topologias apresentadas na tabela acima,
    considerando ainda o melhor treinamento {T1, T2 ou T3} realizado em
    cada uma delas, trace o gráfico dos valores de erro quadrático médio
    (EQM) em função de cada época de treinamento. Imprima os três
    gráficos numa mesma folha de modo não superpostos.

5.  Baseado nas análises dos itens acima, indique qual das topologias
    candidatas {Rede 1, Rede 2 ou Rede 3} e com que qual configuração
    final de treinamento {T1 , T2 ou T3} seria a mais adequada para este
    problema.

## ANEXO

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 5%" />
<col style="width: 6%" />
<col style="width: 5%" />
<col style="width: 6%" />
<col style="width: 8%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 8%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 5%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h4 id="amostra">Amostra</h4></td>
<td><em>x</em><sub>1</sub></td>
<td><em>x</em><sub>2</sub></td>
<td><em>x</em><sub>3</sub></td>
<td><em>d</em></td>
<td><h3 id="amostra-1">Amostra</h3></td>
<td><em>x</em><sub>1</sub></td>
<td><em>x</em><sub>2</sub></td>
<td><em>x</em><sub>3</sub></td>
<td><em>d</em></td>
<td><h3 id="amostra-2">Amostra</h3></td>
<td><em>x</em><sub>1</sub></td>
<td><em>x</em><sub>2</sub></td>
<td><em>x</em><sub>3</sub></td>
<td><em>d</em></td>
</tr>
<tr class="even">
<td><strong>1</strong></td>
<td>0.9532</td>
<td>0.6949</td>
<td>0.4451</td>
<td>0.8426</td>
<td><strong>51</strong></td>
<td>0.7408</td>
<td>0.5351</td>
<td>0.2732</td>
<td>0.6949</td>
<td><strong>101</strong></td>
<td>0.5497</td>
<td>0.6319</td>
<td>0.8382</td>
<td>0.8521</td>
</tr>
<tr class="odd">
<td><strong>2</strong></td>
<td>0.7954</td>
<td>0.8346</td>
<td>0.0449</td>
<td>0.6676</td>
<td><strong>52</strong></td>
<td>0.6843</td>
<td>0.3737</td>
<td>0.1562</td>
<td>0.5625</td>
<td><strong>102</strong></td>
<td>0.7072</td>
<td>0.1721</td>
<td>0.3812</td>
<td>0.5772</td>
</tr>
<tr class="even">
<td><strong>3</strong></td>
<td>0.1427</td>
<td>0.048</td>
<td>0.6267</td>
<td>0.3780</td>
<td><strong>53</strong></td>
<td>0.8799</td>
<td>0.7998</td>
<td>0.3972</td>
<td>0.8399</td>
<td><strong>103</strong></td>
<td>0.1185</td>
<td>0.5084</td>
<td>0.8376</td>
<td>0.6211</td>
</tr>
<tr class="odd">
<td><strong>4</strong></td>
<td>0.1516</td>
<td>0.9824</td>
<td>0.0827</td>
<td>0.4627</td>
<td><strong>54</strong></td>
<td>0.5700</td>
<td>0.5111</td>
<td>0.2418</td>
<td>0.6258</td>
<td><strong>104</strong></td>
<td>0.6365</td>
<td>0.5562</td>
<td>0.4965</td>
<td>0.7693</td>
</tr>
<tr class="even">
<td><strong>5</strong></td>
<td>0.4868</td>
<td>0.6223</td>
<td>0.7462</td>
<td>0.8116</td>
<td><strong>55</strong></td>
<td>0.6796</td>
<td>0.4117</td>
<td>0.3370</td>
<td>0.6622</td>
<td><strong>105</strong></td>
<td>0.4145</td>
<td>0.5797</td>
<td>0.8599</td>
<td>0.7878</td>
</tr>
<tr class="odd">
<td><strong>6</strong></td>
<td>0.3408</td>
<td>0.5115</td>
<td>0.0783</td>
<td>0.4559</td>
<td><strong>56</strong></td>
<td>0.3567</td>
<td>0.2967</td>
<td>0.6037</td>
<td>0.5969</td>
<td><strong>106</strong></td>
<td>0.2575</td>
<td>0.5358</td>
<td>0.4028</td>
<td>0.5777</td>
</tr>
<tr class="even">
<td><strong>7</strong></td>
<td>0.8146</td>
<td>0.6378</td>
<td>0.5837</td>
<td>0.8628</td>
<td><strong>57</strong></td>
<td>0.3866</td>
<td>0.8390</td>
<td>0.0232</td>
<td>0.5316</td>
<td><strong>107</strong></td>
<td>0.2026</td>
<td>0.3300</td>
<td>0.3054</td>
<td>0.4261</td>
</tr>
<tr class="odd">
<td><strong>8</strong></td>
<td>0.2820</td>
<td>0.5409</td>
<td>0.7256</td>
<td>0.6939</td>
<td><strong>58</strong></td>
<td>0.0271</td>
<td>0.7788</td>
<td>0.7445</td>
<td>0.6335</td>
<td><strong>108</strong></td>
<td>0.3385</td>
<td>0.0476</td>
<td>0.5941</td>
<td>0.4625</td>
</tr>
<tr class="even">
<td><strong>9</strong></td>
<td>0.5716</td>
<td>0.2958</td>
<td>0.5477</td>
<td>0.6619</td>
<td><strong>59</strong></td>
<td>0.8174</td>
<td>0.8422</td>
<td>0.3229</td>
<td>0.8068</td>
<td><strong>109</strong></td>
<td>0.4094</td>
<td>0.1726</td>
<td>0.7803</td>
<td>0.6015</td>
</tr>
<tr class="odd">
<td><strong>10</strong></td>
<td>0.9323</td>
<td>0.0229</td>
<td>0.4797</td>
<td>0.5731</td>
<td><strong>60</strong></td>
<td>0.6027</td>
<td>0.1468</td>
<td>0.3759</td>
<td>0.5342</td>
<td><strong>110</strong></td>
<td>0.1261</td>
<td>0.6181</td>
<td>0.4927</td>
<td>0.5739</td>
</tr>
<tr class="even">
<td><strong>11</strong></td>
<td>0.2907</td>
<td>0.7245</td>
<td>0.5165</td>
<td>0.6911</td>
<td><strong>61</strong></td>
<td>0.1203</td>
<td>0.3260</td>
<td>0.5419</td>
<td>0.4768</td>
<td><strong>111</strong></td>
<td>0.1224</td>
<td>0.4662</td>
<td>0.2146</td>
<td>0.4007</td>
</tr>
<tr class="odd">
<td><strong>12</strong></td>
<td>0.0068</td>
<td>0.0545</td>
<td>0.0861</td>
<td>0.0851</td>
<td><strong>62</strong></td>
<td>0.1325</td>
<td>0.2082</td>
<td>0.4934</td>
<td>0.4105</td>
<td><strong>112</strong></td>
<td>0.6793</td>
<td>0.6774</td>
<td>1.0000</td>
<td>0.9141</td>
</tr>
<tr class="even">
<td><strong>13</strong></td>
<td>0.2636</td>
<td>0.9885</td>
<td>0.2175</td>
<td>0.5847</td>
<td><strong>63</strong></td>
<td>0.6950</td>
<td>1.0000</td>
<td>0.4321</td>
<td>0.8404</td>
<td><strong>113</strong></td>
<td>0.8176</td>
<td>0.0358</td>
<td>0.2506</td>
<td>0.4707</td>
</tr>
<tr class="odd">
<td><strong>14</strong></td>
<td>0.035</td>
<td>0.3653</td>
<td>0.7801</td>
<td>0.5117</td>
<td><strong>64</strong></td>
<td>0.0036</td>
<td>0.1940</td>
<td>0.3274</td>
<td>0.2697</td>
<td><strong>114</strong></td>
<td>0.6937</td>
<td>0.6685</td>
<td>0.5075</td>
<td>0.8220</td>
</tr>
<tr class="even">
<td><strong>15</strong></td>
<td>0.967</td>
<td>0.3031</td>
<td>0.7127</td>
<td>0.7836</td>
<td><strong>65</strong></td>
<td>0.2650</td>
<td>0.0161</td>
<td>0.5947</td>
<td>0.4125</td>
<td><strong>115</strong></td>
<td>0.2404</td>
<td>0.5411</td>
<td>0.8754</td>
<td>0.6980</td>
</tr>
<tr class="odd">
<td><strong>16</strong></td>
<td>0.0000</td>
<td>0.7763</td>
<td>0.8735</td>
<td>0.6388</td>
<td><strong>66</strong></td>
<td>0.5849</td>
<td>0.6019</td>
<td>0.4376</td>
<td>0.7464</td>
<td><strong>116</strong></td>
<td>0.6553</td>
<td>0.2609</td>
<td>0.1188</td>
<td>0.4851</td>
</tr>
<tr class="even">
<td><strong>17</strong></td>
<td>0.4395</td>
<td>0.0501</td>
<td>0.9761</td>
<td>0.5712</td>
<td><strong>67</strong></td>
<td>0.0108</td>
<td>0.3538</td>
<td>0.1810</td>
<td>0.2800</td>
<td><strong>117</strong></td>
<td>0.8886</td>
<td>0.0288</td>
<td>0.2604</td>
<td>0.4802</td>
</tr>
<tr class="odd">
<td><strong>18</strong></td>
<td>0.9359</td>
<td>0.0366</td>
<td>0.9514</td>
<td>0.6826</td>
<td><strong>68</strong></td>
<td>0.9008</td>
<td>0.7264</td>
<td>0.9184</td>
<td>0.9602</td>
<td><strong>118</strong></td>
<td>0.3974</td>
<td>0.5275</td>
<td>0.6457</td>
<td>0.7215</td>
</tr>
<tr class="even">
<td><strong>19</strong></td>
<td>0.0173</td>
<td>0.9548</td>
<td>0.4289</td>
<td>0.5527</td>
<td><strong>69</strong></td>
<td>0.0023</td>
<td>0.9659</td>
<td>0.3182</td>
<td>0.4986</td>
<td><strong>119</strong></td>
<td>0.2108</td>
<td>0.4910</td>
<td>0.5432</td>
<td>0.5913</td>
</tr>
<tr class="odd">
<td><strong>20</strong></td>
<td>0.6112</td>
<td>0.907</td>
<td>0.6286</td>
<td>0.8803</td>
<td><strong>70</strong></td>
<td>0.1366</td>
<td>0.6357</td>
<td>0.6967</td>
<td>0.6459</td>
<td><strong>120</strong></td>
<td>0.8675</td>
<td>0.5571</td>
<td>0.1849</td>
<td>0.6805</td>
</tr>
<tr class="even">
<td><strong>21</strong></td>
<td>0.2010</td>
<td>0.9573</td>
<td>0.6791</td>
<td>0.7283</td>
<td><strong>71</strong></td>
<td>0.8621</td>
<td>0.7353</td>
<td>0.2742</td>
<td>0.7718</td>
<td><strong>121</strong></td>
<td>0.5693</td>
<td>0.0242</td>
<td>0.9293</td>
<td>0.6033</td>
</tr>
<tr class="odd">
<td><strong>22</strong></td>
<td>0.8914</td>
<td>0.9144</td>
<td>0.2641</td>
<td>0.7966</td>
<td><strong>72</strong></td>
<td>0.0682</td>
<td>0.9624</td>
<td>0.4211</td>
<td>0.5764</td>
<td><strong>122</strong></td>
<td>0.8439</td>
<td>0.4631</td>
<td>0.6345</td>
<td>0.8226</td>
</tr>
<tr class="even">
<td><strong>23</strong></td>
<td>0.0061</td>
<td>0.0802</td>
<td>0.8621</td>
<td>0.3711</td>
<td><strong>73</strong></td>
<td>0.6112</td>
<td>0.6014</td>
<td>0.5254</td>
<td>0.7868</td>
<td><strong>123</strong></td>
<td>0.3644</td>
<td>0.2948</td>
<td>0.3937</td>
<td>0.5240</td>
</tr>
<tr class="odd">
<td><strong>24</strong></td>
<td>0.2212</td>
<td>0.4664</td>
<td>0.3821</td>
<td>0.5260</td>
<td><strong>74</strong></td>
<td>0.0030</td>
<td>0.7585</td>
<td>0.8928</td>
<td>0.6388</td>
<td><strong>124</strong></td>
<td>0.2014</td>
<td>0.6326</td>
<td>0.9782</td>
<td>0.7143</td>
</tr>
<tr class="even">
<td><strong>25</strong></td>
<td>0.2401</td>
<td>0.6964</td>
<td>0.0751</td>
<td>0.4637</td>
<td><strong>75</strong></td>
<td>0.7644</td>
<td>0.5964</td>
<td>0.0407</td>
<td>0.6055</td>
<td><strong>125</strong></td>
<td>0.4039</td>
<td>0.0645</td>
<td>0.4629</td>
<td>0.4547</td>
</tr>
<tr class="odd">
<td><strong>26</strong></td>
<td>0.7881</td>
<td>0.9833</td>
<td>0.3038</td>
<td>0.8049</td>
<td><strong>76</strong></td>
<td>0.6441</td>
<td>0.2097</td>
<td>0.5847</td>
<td>0.6545</td>
<td><strong>126</strong></td>
<td>0.7137</td>
<td>0.0670</td>
<td>0.2359</td>
<td>0.4602</td>
</tr>
<tr class="even">
<td><strong>27</strong></td>
<td>0.2435</td>
<td>0.0794</td>
<td>0.5551</td>
<td>0.4223</td>
<td><strong>77</strong></td>
<td>0.0803</td>
<td>0.3799</td>
<td>0.6020</td>
<td>0.4991</td>
<td><strong>127</strong></td>
<td>0.4277</td>
<td>0.9555</td>
<td>0.0000</td>
<td>0.5477</td>
</tr>
<tr class="odd">
<td><strong>28</strong></td>
<td>0.2752</td>
<td>0.8414</td>
<td>0.2797</td>
<td>0.6079</td>
<td><strong>78</strong></td>
<td>0.1908</td>
<td>0.8046</td>
<td>0.5402</td>
<td>0.6665</td>
<td><strong>128</strong></td>
<td>0.0259</td>
<td>0.7634</td>
<td>0.2889</td>
<td>0.4738</td>
</tr>
<tr class="even">
<td><strong>29</strong></td>
<td>0.7616</td>
<td>0.4698</td>
<td>0.5337</td>
<td>0.7809</td>
<td><strong>79</strong></td>
<td>0.6937</td>
<td>0.3967</td>
<td>0.6055</td>
<td>0.7595</td>
<td><strong>129</strong></td>
<td>0.1871</td>
<td>0.7682</td>
<td>0.9697</td>
<td>0.7397</td>
</tr>
<tr class="odd">
<td><strong>30</strong></td>
<td>0.3395</td>
<td>0.0022</td>
<td>0.0087</td>
<td>0.1836</td>
<td><strong>80</strong></td>
<td>0.2591</td>
<td>0.0582</td>
<td>0.3978</td>
<td>0.3604</td>
<td><strong>130</strong></td>
<td>0.3216</td>
<td>0.5420</td>
<td>0.0677</td>
<td>0.4526</td>
</tr>
<tr class="even">
<td><strong>31</strong></td>
<td>0.7849</td>
<td>0.9981</td>
<td>0.4449</td>
<td>0.8641</td>
<td><strong>81</strong></td>
<td>0.4241</td>
<td>0.1850</td>
<td>0.9066</td>
<td>0.6298</td>
<td><strong>131</strong></td>
<td>0.2524</td>
<td>0.7688</td>
<td>0.9523</td>
<td>0.7711</td>
</tr>
<tr class="odd">
<td><strong>32</strong></td>
<td>0.8312</td>
<td>0.0961</td>
<td>0.2129</td>
<td>0.4857</td>
<td><strong>82</strong></td>
<td>0.3332</td>
<td>0.9303</td>
<td>0.2475</td>
<td>0.6287</td>
<td><strong>132</strong></td>
<td>0.3621</td>
<td>0.5295</td>
<td>0.2521</td>
<td>0.5571</td>
</tr>
<tr class="even">
<td><strong>33</strong></td>
<td>0.9763</td>
<td>0.1102</td>
<td>0.6227</td>
<td>0.6667</td>
<td><strong>83</strong></td>
<td>0.3625</td>
<td>0.1592</td>
<td>0.9981</td>
<td>0.5948</td>
<td><strong>133</strong></td>
<td>0.2942</td>
<td>0.1625</td>
<td>0.2745</td>
<td>0.3759</td>
</tr>
<tr class="odd">
<td><strong>34</strong></td>
<td>0.8597</td>
<td>0.3284</td>
<td>0.6932</td>
<td>0.7829</td>
<td><strong>84</strong></td>
<td>0.9259</td>
<td>0.0960</td>
<td>0.1645</td>
<td>0.4716</td>
<td><strong>134</strong></td>
<td>0.8180</td>
<td>0.0023</td>
<td>0.1439</td>
<td>0.4018</td>
</tr>
<tr class="even">
<td><strong>35</strong></td>
<td>0.9295</td>
<td>0.3275</td>
<td>0.7536</td>
<td>0.8016</td>
<td><strong>85</strong></td>
<td>0.8606</td>
<td>0.6779</td>
<td>0.0033</td>
<td>0.6242</td>
<td><strong>135</strong></td>
<td>0.8429</td>
<td>0.1704</td>
<td>0.5251</td>
<td>0.6563</td>
</tr>
<tr class="odd">
<td><strong>36</strong></td>
<td>0.2435</td>
<td>0.2163</td>
<td>0.7625</td>
<td>0.5449</td>
<td><strong>86</strong></td>
<td>0.0838</td>
<td>0.5472</td>
<td>0.3758</td>
<td>0.4835</td>
<td><strong>136</strong></td>
<td>0.9612</td>
<td>0.6898</td>
<td>0.6630</td>
<td>0.9128</td>
</tr>
<tr class="even">
<td><strong>37</strong></td>
<td>0.9281</td>
<td>0.8356</td>
<td>0.5285</td>
<td>0.8991</td>
<td><strong>87</strong></td>
<td>0.0303</td>
<td>0.9191</td>
<td>0.7233</td>
<td>0.6491</td>
<td><strong>137</strong></td>
<td>0.1009</td>
<td>0.419</td>
<td>0.0826</td>
<td>0.3055</td>
</tr>
<tr class="odd">
<td><strong>38</strong></td>
<td>0.8313</td>
<td>0.7566</td>
<td>0.6192</td>
<td>0.9047</td>
<td><strong>88</strong></td>
<td>0.9293</td>
<td>0.8319</td>
<td>0.9664</td>
<td>0.9840</td>
<td><strong>138</strong></td>
<td>0.7071</td>
<td>0.7704</td>
<td>0.8328</td>
<td>0.9298</td>
</tr>
<tr class="even">
<td><strong>39</strong></td>
<td>0.1712</td>
<td>0.0545</td>
<td>0.5033</td>
<td>0.3561</td>
<td><strong>89</strong></td>
<td>0.7268</td>
<td>0.1440</td>
<td>0.9753</td>
<td>0.7096</td>
<td><strong>139</strong></td>
<td>0.3371</td>
<td>0.7819</td>
<td>0.0959</td>
<td>0.5377</td>
</tr>
<tr class="odd">
<td><strong>40</strong></td>
<td>0.0609</td>
<td>0.1702</td>
<td>0.4306</td>
<td>0.3310</td>
<td><strong>90</strong></td>
<td>0.2888</td>
<td>0.6593</td>
<td>0.4078</td>
<td>0.6328</td>
<td><strong>140</strong></td>
<td>0.9931</td>
<td>0.6727</td>
<td>0.3139</td>
<td>0.7829</td>
</tr>
<tr class="even">
<td><strong>41</strong></td>
<td>0.5899</td>
<td>0.9408</td>
<td>0.0369</td>
<td>0.6245</td>
<td><strong>91</strong></td>
<td>0.5515</td>
<td>0.1364</td>
<td>0.2894</td>
<td>0.4745</td>
<td><strong>141</strong></td>
<td>0.9123</td>
<td>0.0000</td>
<td>0.1106</td>
<td>0.3944</td>
</tr>
<tr class="odd">
<td><strong>42</strong></td>
<td>0.7858</td>
<td>0.5115</td>
<td>0.0916</td>
<td>0.6066</td>
<td><strong>92</strong></td>
<td>0.7683</td>
<td>0.0067</td>
<td>0.5546</td>
<td>0.5708</td>
<td><strong>142</strong></td>
<td>0.2858</td>
<td>0.9688</td>
<td>0.2262</td>
<td>0.5988</td>
</tr>
<tr class="even">
<td><strong>43</strong></td>
<td>1.0000</td>
<td>0.1653</td>
<td>0.7103</td>
<td>0.7172</td>
<td><strong>93</strong></td>
<td>0.6462</td>
<td>0.6761</td>
<td>0.8340</td>
<td>0.8933</td>
<td><strong>143</strong></td>
<td>0.7931</td>
<td>0.8993</td>
<td>0.9028</td>
<td>0.9728</td>
</tr>
<tr class="odd">
<td><strong>44</strong></td>
<td>0.2007</td>
<td>0.1163</td>
<td>0.3431</td>
<td>0.3385</td>
<td><strong>94</strong></td>
<td>0.3694</td>
<td>0.2212</td>
<td>0.1233</td>
<td>0.3658</td>
<td><strong>144</strong></td>
<td>0.7841</td>
<td>0.0778</td>
<td>0.9012</td>
<td>0.6832</td>
</tr>
<tr class="even">
<td><strong>45</strong></td>
<td>0.2306</td>
<td>0.033</td>
<td>0.0293</td>
<td>0.1590</td>
<td><strong>95</strong></td>
<td>0.2706</td>
<td>0.3222</td>
<td>0.9996</td>
<td>0.6310</td>
<td><strong>145</strong></td>
<td>0.1380</td>
<td>0.5881</td>
<td>0.2367</td>
<td>0.4622</td>
</tr>
<tr class="odd">
<td><strong>46</strong></td>
<td>0.8477</td>
<td>0.6378</td>
<td>0.4623</td>
<td>0.8254</td>
<td><strong>96</strong></td>
<td>0.6282</td>
<td>0.1404</td>
<td>0.8474</td>
<td>0.6733</td>
<td><strong>146</strong></td>
<td>0.6345</td>
<td>0.5165</td>
<td>0.7139</td>
<td>0.8191</td>
</tr>
<tr class="even">
<td><strong>47</strong></td>
<td>0.9677</td>
<td>0.7895</td>
<td>0.9467</td>
<td>0.9782</td>
<td><strong>97</strong></td>
<td>0.5861</td>
<td>0.6693</td>
<td>0.3818</td>
<td>0.7433</td>
<td><strong>147</strong></td>
<td>0.2453</td>
<td>0.5888</td>
<td>0.1559</td>
<td>0.4765</td>
</tr>
<tr class="odd">
<td><strong>48</strong></td>
<td>0.0339</td>
<td>0.4669</td>
<td>0.1526</td>
<td>0.3250</td>
<td><strong>98</strong></td>
<td>0.6057</td>
<td>0.9901</td>
<td>0.5141</td>
<td>0.8466</td>
<td><strong>148</strong></td>
<td>0.1174</td>
<td>0.5436</td>
<td>0.3657</td>
<td>0.4953</td>
</tr>
<tr class="even">
<td><strong>49</strong></td>
<td>0.008</td>
<td>0.8988</td>
<td>0.4201</td>
<td>0.5404</td>
<td><strong>99</strong></td>
<td>0.5915</td>
<td>0.5588</td>
<td>0.3055</td>
<td>0.6787</td>
<td><strong>149</strong></td>
<td>0.3667</td>
<td>0.3228</td>
<td>0.6952</td>
<td>0.6376</td>
</tr>
<tr class="odd">
<td><strong>50</strong></td>
<td>0.9955</td>
<td>0.8897</td>
<td>0.6175</td>
<td>0.9360</td>
<td><strong>100</strong></td>
<td>0.8359</td>
<td>0.4145</td>
<td>0.5016</td>
<td>0.7597</td>
<td><strong>150</strong></td>
<td>0.2204</td>
<td>0.1785</td>
<td>0.4607</td>
<td>0.4276</td>
</tr>
</tbody>
</table>
