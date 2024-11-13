import funcoes
import pandas as pds

intervalos = [(300, 400), (400, 500), (500, 600), (600, 700), (700, 800), (800, 900), (900, 1000), (1000, 1100), (1100, 1200)]
frequencias = [14, 46, 58, 76, 68, 62, 48, 22, 6]

dados = [{"Classes":"300|-400","Frequencia":"14"}
        ,{"Classes":"400|-500","Frequencia":"46"}
        ,{"Classes":"500|-600","Frequencia":"58"}
        ,{"Classes":"600|-700","Frequencia":"76"}
        ,{"Classes":"700|-800","Frequencia":"68"}
        ,{"Classes":"800|-900","Frequencia":"62"}
        ,{"Classes":"900|-1000","Frequencia":"48"}
        ,{"Classes":"1000|-1100","Frequencia":"22"}
        ,{"Classes":"1100|-1200","Frequencia":"6"}
]

print(f"\nIntervalos: {intervalos}")
print(f"Frequências: {frequencias}")
print("Tabela de distribuicao")
tabela = pds.DataFrame(dados)
print(tabela)
print(f"\nMédia: {funcoes.calcularMedia(intervalos, frequencias)}")
print(f"Moda: {funcoes.calcularModa(intervalos, frequencias)}")
print(f"Mediana: {funcoes.calcularMediana(intervalos, frequencias)}")
print(f"Desvio Padrão: {funcoes.calcularDP(intervalos, frequencias)}")
print(f"Quartil 1: {funcoes.calcularPencentil(intervalos, frequencias, 25)}")
print(f"Dercil 3 : {funcoes.calcularPencentil(intervalos, frequencias, 30)}")
print(f"Dercil 7: {funcoes.calcularPencentil(intervalos, frequencias, 70)}")
print(f"Percentil 15: {funcoes.calcularPencentil(intervalos, frequencias, 15)}")
print(f"Percentil 90: {funcoes.calcularPencentil(intervalos, frequencias, 90)}")
intervalosSeparados = funcoes.separaClasses(intervalos)
funcoes.gerarGrafico(intervalosSeparados, frequencias)
