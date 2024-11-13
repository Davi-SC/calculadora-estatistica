import math

# Dados da questão
intervalos = [(10, 20), (20, 30), (30, 40), (40, 50)]
frequencias = [4, 6, 8, 2]

def calcularModa(intervalos, frequencias):
    maiorFrequencia  = 0
    moda = None

    for i in range(len(frequencias)):
        if (frequencias[i] > maiorFrequencia):
            maiorFrequencia = frequencias[i]
            moda = (intervalos[i][0]+intervalos[i][1])/2
    return moda

def calcularMediana(intervalos, frequencias):
    totalFreq = 0
    for f in frequencias:
        totalFreq += f
    
    freqAcumulada = 0
    mediana = 0
    for i in range(len(frequencias)):
        freqAcumulada += frequencias[i]
        if freqAcumulada >= totalFreq/2:
            a, b = intervalos[i]
            mediana = a+b/2
            break

    return mediana

def calcularMedia(intervalos, frequencias):
    soma = 0 #somatorio dos pontomedios vezes suas frequencias
    somaFreq = 0 #somatorio das frequencias

    for i in range(len(frequencias)):
        a, b = intervalos[i]
        pontoMedio = (a+b)/2
        freq = frequencias[i]
        soma += pontoMedio * freq
        somaFreq += freq
    
    if(somaFreq != 0):
        media = soma/somaFreq
    else: media = 0

    return media


def calcularDP(intervalos, frequencias):
    media = calcularMedia(intervalos,frequencias)
    soma = 0 #essa soma vai ser dada pelo somatorio das frequencias vezes (ponto medio - media)elevado a 2
    somaFreq = 0 #soma das frequencias
    for i in range(len(intervalos)):
        a, b = intervalos[i]
        frequencia = frequencias[i]
        ponto_medio = (a + b) / 2
        soma += frequencia * (ponto_medio - media) ** 2
        somaFreq += frequencia
    
    if(somaFreq != 0):
        variancia = soma/ somaFreq
    else: variancia = 0
    desvioPadrao = math.sqrt(variancia)
    return media

def calcularPencentil(intervalos, frequencias, percentil):
    totalFreq = 0
    for f in frequencias:
        totalFreq += f

    posicaoPct = (percentil / 100) * totalFreq
    freqAcumulada = 0
    valorPct = 0
    for i in range(len(frequencias)):
        freqAcumulada += frequencias[i]
        if freqAcumulada >= posicaoPct:
            a, b = intervalos[i]
            valorPct = (a + b) / 2
            break
    return valorPct  

def gerar_grafico(intervalos, frequencias):
    print("\nGráfico de Frequências:")

# Cálculos e resultados
print("")
print(f"Intervalos: {intervalos}")
print(f"Frequências: {frequencias}")
print(f"Média: {calcularMedia(intervalos, frequencias)}")
print(f"Moda: {calcularModa(intervalos, frequencias)}")
print(f"Mediana: {calcularMediana(intervalos, frequencias)}")
print(f"Desvio Padrão: {calcularDP(intervalos, frequencias)}")
print(f"Percentil 25: {calcularPencentil(intervalos, frequencias, 25)}")
print(f"Percentil 50 (Mediana): {calcularPencentil(intervalos, frequencias, 50)}")
print(f"Percentil 75: {calcularPencentil(intervalos, frequencias, 75)}")
gerar_grafico(intervalos, frequencias)

