import math
import matplotlib.pyplot as plt

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

def separaClasses(intervalos):
    classesSeparadas = []
    for intervalo in intervalos:
        classesSeparadas.append(str(intervalo[0]) + " a " + str(intervalo[1]))
    return classesSeparadas


def gerarGrafico(intervalos, frequencias):
    print("\nGráfico de Frequências:")


    plt.bar(intervalos, frequencias)
    plt.xlabel('Intervalos')
    plt.ylabel('Frequencias')
    plt.title('Gráfico de Barras')
    plt.show()


