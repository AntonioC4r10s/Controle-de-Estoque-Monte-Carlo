import csv
import random
from matplotlib import pyplot as plt
import tkinter as tk
from tkinter import ttk

NUMERODEMESES = 6

#Gerar um unmero aleatorio entre a e b.
def numAleatorio(a, b):
    return random.randint(a, b)

#Geraar uma planilha de dados de estoque
def geraDados(numeroDeProdutos):
    file = open('../src/estoque.csv', 'w', newline='', encoding='utf-8')

    # cria o objeto de gravação
    w = csv.writer(file)

    w.writerow(['Produto', '1', '2', '3', '4', '5', '6', 'Total', 'Classificacao', 'Media Dia',
                'Estoque Ideal'])

    numeroDeProdutosMax = 40

    for i in range(numeroDeProdutos):
        id = i+1
        mes_1 = numAleatorio(0, numeroDeProdutosMax)
        mes_2 = numAleatorio(0, numeroDeProdutosMax)
        mes_3 = numAleatorio(0, numeroDeProdutosMax)
        mes_4 = numAleatorio(0, numeroDeProdutosMax)
        mes_5 = numAleatorio(0, numeroDeProdutosMax)
        mes_6 = numAleatorio(0, numeroDeProdutosMax)
        total = (mes_1 + mes_2 + mes_3 + mes_4 +mes_5 + mes_6)
        numParaClassif = random.random()

        if (numParaClassif < 0.2):
            classificacao = 'A'
        elif (numParaClassif < 0.5):
            classificacao = 'B'
        else:
            classificacao = 'C'

        mediaDianum = total/180
        mediaDia = ("{0:.2f}" .format(mediaDianum))

        if (classificacao == 'A'):
            estoqueIdeal = mediaDianum * 30
        elif (classificacao == 'B'):
            estoqueIdeal = mediaDianum * 20
        else:
            estoqueIdeal = mediaDianum * 10
        estoqueIdeal = ("{0:.2f}".format(estoqueIdeal))

        w.writerow([id, mes_1, mes_2, mes_3, mes_4, mes_5, mes_6, total, classificacao, mediaDia, estoqueIdeal])
    file.close()
    #restart_program()


def csvParaLista():
    file = open('../src/estoque.csv', 'r')
    reader = csv.reader(file)
    lista = []

    for linha in reader:
        lista.append(linha)
    return lista

#Gerar grafico de proporção de produtos tipo A, B e C.
def grafico2():
    grupos = ["A", "B", "C"]
    A = 0
    B = 0
    C = 0

    lista = csvParaLista()

    for i in range(1, len(lista)):
        if(lista[i][8] == "A"):
            A += 1
        elif (lista[i][8] == "B"):
            B += 1
        else:
            C += 1
    valores = [A, B, C]
    #print(valores)
    plt.bar(grupos, valores)
    plt.xlabel("Classificação")
    plt.ylabel("Proporção")
    plt.show()

#Funções:
def geraNovosDados(numeroDeProdutos, my_tree):
    geraDados(numeroDeProdutos)
    lista = csvParaLista()

    # Adicionando intens na Tree.
    for i in range(1, len(lista)):
        listaAux = []
        for j in range(1, len(lista[i])):
            listaAux.append(lista[i][j])
        my_tree.item(i, text=lista[i][0], values=listaAux)

#Gerar grafico de Tradicional x MC
def grafico1():
    lista = csvParaLista()

    mes_1 = 0
    mes_2 = 0
    mes_3 = 0
    mes_4 = 0
    mes_5 = 0
    mes_6 = 0
    meses =  [0,30,60,90,120,150]
    distNormal = [mes_1, mes_2, mes_3, mes_4, mes_5, mes_6]
    distMC = []
    somaMC = 0
    for i in range(1, len(lista)):
        distNormal[0] += int(lista[i][1])
        distNormal[1] += int(lista[i][2])
        distNormal[2] += int(lista[i][3])
        distNormal[3] += int(lista[i][4])
        distNormal[4] += int(lista[i][5])
        distNormal[5] += int(lista[i][6])
        somaMC += (float)(lista[i][10])

    for i in range(0, len(meses)):
        distMC.append(somaMC)

    plt.plot(meses, distNormal, color="red")
    plt.plot(meses, distMC, color="blue")
    plt.xlabel("Tempo - (mês)")
    plt.ylabel("Nº de Produtos")
    plt.title("Tradicional x MC")
    plt.show()

def grafico1_2():
    lista = csvParaLista()
    dias = []
    dia = 0
    produtosPorDia = []
    mediaMensal = []

    for i in range(1, 7):
        mediaDeProdutos = 0
        for j in range(1, len(lista)):
            mediaDeProdutos += int(lista[j][i])
        mediaMensal.append(mediaDeProdutos)

    for i in range(0, NUMERODEMESES):
        mediaDeProdutos = mediaMensal[i]/30
        numeroDeProdutosDia = mediaMensal[i]
        for j in range(0, 30):
            dias.append(dia)
            dia += 1
            produtosPorDia.append(numeroDeProdutosDia)
            numeroDeProdutosDia -= mediaDeProdutos
    #print(mediaMensal)
    #print(dias)
    #print(produtosPorDia)

    plt.plot(dias, produtosPorDia, "r")
    plt.show()

cont = ["#0", "#1", "#2", "#3", "#4", "#5", "#6", "#7", "#8", "#9", "#10", "#11", "#12", "#13", "#14", "#15", "#16", "#17", "#18", "#19", "#20"]
#print(csvParaLista()[0])

#grafico1_2()