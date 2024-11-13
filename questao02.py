import funcoes

dados = [61,65,43,53,55,51,58,55,59,56,52,53,62,49,68,51,50,67,62,64,53,56,48,50,61,44,64,53,54,55,48,54,57,41,54,71,57,53,46,48,55,46,57,54,48,63,49,55,52,51]

dados.sort()
intervalos = []
frequencias = []
amplitude = 5 
numClasses = 6

minimo = min(dados)
maximo = max(dados)

intervalos = []

for i in range(numClasses):
    inferior = minimo + i * amplitude
    superior = inferior + amplitude
    intervalos.append((inferior, superior))

frequencias = [0,0,0,0,0,0]

for dado in dados:
    for i, intervalo in enumerate(intervalos):
        if intervalo[0] <= dado < intervalo[1]:  
            frequencias[i] += 1
            break  


print(f"\nIntervalos: {intervalos}")
print(f"Frequências: {frequencias}")
print
print(f"Média: {funcoes.calcularMedia(intervalos, frequencias)}")
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

