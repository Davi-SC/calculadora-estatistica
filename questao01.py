import funcoes
import pandas as pds

intervalos = [(300, 400), (400, 500), (500, 600), (600, 700), (700, 800), (800, 900), (900, 1000), (1000, 1100), (1100, 1200)]
frequencias = [14, 46, 58, 76, 68, 62, 48, 22, 6]

dados_dicionario = funcoes.converterDicionarios(intervalos, frequencias)

print("\nTabela de distribuicao\n")
print(pds.DataFrame(dados_dicionario))

print(f"\nMédia: {funcoes.calcularMedia(intervalos, frequencias)}")
print(f"Moda: {funcoes.calcularModa(intervalos, frequencias)}")
print(f"Mediana: {funcoes.calcularMediana(intervalos, frequencias)}")
print(f"Desvio Padrão: {funcoes.calcularDP(intervalos, frequencias)}")
print(f"Quartil 1: {funcoes.calcularPercentil(intervalos, frequencias, 25)}")
print(f"Dercil 3 : {funcoes.calcularPercentil(intervalos, frequencias, 30)}")
print(f"Dercil 7: {funcoes.calcularPercentil(intervalos, frequencias, 70)}")
print(f"Percentil 15: {funcoes.calcularPercentil(intervalos, frequencias, 15)}")
print(f"Percentil 90: {funcoes.calcularPercentil(intervalos, frequencias, 90)}")

funcoes.gerarGrafico(funcoes.separaClasses(intervalos), frequencias)
