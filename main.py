import pandas as pd
import matplotlib.pyplot as plt

# IMPORTANDO DATAFRAME

servDf = pd.read_csv(r'Arquivos\BaseServiçosPrestados.csv', encoding='latin1')
cliDf = pd.read_csv(r'Arquivos\CadastroClientes.csv')
funcDf = pd.read_csv(r'Arquivos\CadastroFuncionarios.csv', sep=';', decimal=',')

# 1 - Qual o valor total da folha salarial da empresa ?
# Analizando e Calculando os dados de funcionários
fSalarial = funcDf['Salario Base'] + funcDf['Impostos'] + funcDf['Beneficios'] + funcDf['VT'] + funcDf['VR']
fSalarial = fSalarial.sum()

resultado = 'R$ {:_.2f}'.format(fSalarial)
resultado = resultado.replace('.', ',').replace('_', '.')
titulo = '< FOLHA SALARIAL >'
print('{:═^50}\nTOTAL.: {}\n'.format(titulo, resultado))

# 2 - Qual foi o faturamento da empresa ?

# Puxando o DATAFRAME
fatDf = servDf

# Mesclando o DATAFRAME
fatDf = fatDf.merge(cliDf, on='ID Cliente')

# Calculando os Valores de cada cliente
fatDf['Total Faturamento por Cliente'] = fatDf['Tempo Total de Contrato (Meses)'] * fatDf['Valor Contrato Mensal']

# Somando o faturamento
vContratoTt = fatDf['Total Faturamento por Cliente'].sum()

# Formatação
fatTt = 'R$ {:_.2f}'.format(int(vContratoTt))
fatTt = fatTt.replace('.', ',').replace('_', '.')
titulo = '< FATURALMENTO DA EMPRESA >'

# Exibindo o Resultado
print('{:═^50}\nTOTAL.: {}\n'.format(titulo, fatTt))

# 3 - Qual a % de funcionários que fechou contratos ?

# Calculando quantos funcionários existem registrados
ttFunc = len(funcDf['ID Funcionário'])

# Calculando quantos contratos foram fechados
contratosFuncTt = fatDf['ID Funcionário'].value_counts()
contratosFuncTt = len(contratosFuncTt)
perFuncContratos = contratosFuncTt / ttFunc

# Exibindo os resultados da Analise
titulo = '< % DE FUNCIONÁRIO COM CONTRATOS REALIZADOS >'
print('{:═^70}\nVALOR.: {:.2%}\n'.format(titulo, perFuncContratos))

# 4 - Total de Controtos realizado por Setor
# Puxando o DATAFRAME
contArea = servDf

# Criando um novo DATAFRAME apenas com os dados relevantes
nFuncDf = funcDf[['ID Funcionário', 'Area']]

# Mesclando os DATAFRAMES
contArea = contArea.merge(nFuncDf, on='ID Funcionário')

# Realizando o calculo de contratos por Área
areaCount = contArea['Area'].value_counts()

# Exibindo os dados da Analise (Valor e Gráfico)
titulo = '< TOTAL DE CONTRATOS REALIZADOS POR SETOR >'
print('{:═^70}\n{}\n'.format(titulo,areaCount))

# 5 - Quantidade de Funcionários por Setor

# Criando um novo DATAFRAME
qntdFunc = funcDf

# Calculando a quantidade de funcionário por Área
qntdFunc = qntdFunc['Area'].value_counts()

# Exibindo os dados Analisados (Tabela e Gráfico)
titulo = '< QUANTIDADE DE FUNCIONÁRIOS POR SETOR >'

print('{:═^70}\n{}\n'.format(titulo, qntdFunc))

# 6 Qual o ticket médio da empresa mensal ?

# Calculando o ticket médio mensal
ticketMedio = cliDf['Valor Contrato Mensal'].mean()

# FORMATANDO O RESULTADO DA MÉDIA DE VALORES DOS CONTRATOS
ticketMedio = 'R$ {:_.2f}'.format(ticketMedio)
ticketMedio = ticketMedio.replace('.', ',').replace('_', '.')

# IMMPRIMINDO RESULTADO
titulo = '< TICKET MÉDIO DA EMPRESA (MENSAL)>'
print('{:═^50}\nTOTAL.: {}'.format(titulo, ticketMedio))
