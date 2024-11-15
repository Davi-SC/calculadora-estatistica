# este arquivo é apenas para testar as funções com questões que ja tenho o gabarito

import funcoes
import pandas as pds

intervalos = [(10, 14), (14, 1), (18, 22), (22, 26), (26, 30), (30, 34), (34, 38), (38, 42)]
frequencias = [15, 28, 40, 30, 20, 15, 10, 5]

dados_dicionario = funcoes.converterDicionarios(intervalos, frequencias)

print("\nTabela de distribuicao\n")
print(pds.DataFrame(dados_dicionario))

print(f"\nMédia: {funcoes.calcularMedia(intervalos, frequencias)}")
print(f"Moda: {funcoes.calcularModa(intervalos, frequencias)}")
print(f"Mediana: {funcoes.calcularMediana(intervalos, frequencias)}")
print(f"Desvio Padrão: {funcoes.calcularDP(intervalos, frequencias)}")
print(f"Quartil 2: {funcoes.calcularPercentil(intervalos, frequencias, 50)}")
print(f"Dercil 3 : {funcoes.calcularPercentil(intervalos, frequencias, 30)}")
print(f"Dercil 9: {funcoes.calcularPercentil(intervalos, frequencias, 90)}")
print(f"Percentil 60: {funcoes.calcularPercentil(intervalos, frequencias, 60)}")
print(f"Percentil 85: {funcoes.calcularPercentil(intervalos, frequencias, 85)}")

funcoes.gerarGrafico(funcoes.separaClasses(intervalos), frequencias)
