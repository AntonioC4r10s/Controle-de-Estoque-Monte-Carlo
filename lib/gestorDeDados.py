import csv
import random
from matplotlib import pyplot as plt

NUMERODEMESES = 6
NUMERODEPRODUTOS = 10


# Gerar um numero aleatorio entre a e b.
def num_aleatorio(a, b):
    return random.randint(a, b)


# Gerar uma planilha de dados de estoque
def gera_dados(numerodeprodutos):
    file = open('../src/estoque.csv', 'w', newline='', encoding='utf-8')

    # cria o objeto de gravação
    w = csv.writer(file)

    w.writerow(['Produto', '1', '2', '3', '4', '5', '6', 'Total', 'Classificacao', 'Media Dia',
                'Estoque Ideal'])

    numeroDeProdutosMax = 40

    for i in range(numerodeprodutos):
        ID: int = i + 1
        mes_1 = num_aleatorio(0, numeroDeProdutosMax)
        mes_2 = num_aleatorio(0, numeroDeProdutosMax)
        mes_3 = num_aleatorio(0, numeroDeProdutosMax)
        mes_4 = num_aleatorio(0, numeroDeProdutosMax)
        mes_5 = num_aleatorio(0, numeroDeProdutosMax)
        mes_6 = num_aleatorio(0, numeroDeProdutosMax)
        total = (mes_1 + mes_2 + mes_3 + mes_4 + mes_5 + mes_6)
        numParaClassif = random.random()

        if numParaClassif < 0.25:
            classificacao = 'A'
        elif numParaClassif < 0.6:
            classificacao = 'B'
        else:
            classificacao = 'C'

        mediaDianum = total / 180
        mediaDia = ("{0:.2f}".format(mediaDianum))

        if classificacao == 'A':
            estoqueIdeal = mediaDianum * 30
        elif classificacao == 'B':
            estoqueIdeal = mediaDianum * 20
        else:
            estoqueIdeal = mediaDianum * 10
        estoqueIdeal = ("{0:.2f}".format(estoqueIdeal))

        w.writerow([ID, mes_1, mes_2, mes_3, mes_4, mes_5, mes_6, total, classificacao, mediaDia, estoqueIdeal])
    file.close()
    # restart_program()


def csv_para_lista():
    file = open('../src/estoque.csv', 'r')
    reader = csv.reader(file)
    lista = []

    for linha in reader:
        lista.append(linha)
    file.close()
    return lista


# Funções:
def gera_novos_dados(numerodeprodutos, my_tree):
    gera_dados(numerodeprodutos)
    lista = csv_para_lista()

    # Adicionando intens na Tree.
    for i in range(1, numerodeprodutos):
        listaAux = []
        for j in range(1, len(lista[i])):
            listaAux.append(lista[i][j])
        my_tree.item(i, text=lista[i][0], values=listaAux)


# Gerar grafico de Tradicional x MC
def grafico_1():
    lista = csv_para_lista()

    mes_1 = 0
    mes_2 = 0
    mes_3 = 0
    mes_4 = 0
    mes_5 = 0
    mes_6 = 0
    meses = [0, 30, 60, 90, 120, 150]
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
        somaMC += float(lista[i][10])

    for i in range(0, len(meses)):
        distMC.append(somaMC)

    plt.plot(meses, distNormal, color="red")
    plt.plot(meses, distMC, color="blue")
    plt.xlabel("Tempo - (mês)")
    plt.ylabel("Nº de Produtos")
    plt.title("Tradicional x MC")
    plt.show()


def grafico_1_2():
    lista = csv_para_lista()
    dias = []
    dia = 0
    produtosPorDia = []
    mediaMensal = []
    mediaDiaTotal = 0
    estoqueIdealTotal = 0
    numeroDeProdutosNoEstoque = []

    for i in range(1, 7):
        mediaDeProdutos = 0
        for j in range(1, len(lista)):
            mediaDeProdutos += int(lista[j][i])
        mediaMensal.append(mediaDeProdutos)

    for i in range(0, NUMERODEMESES):
        mediaDeProdutos = mediaMensal[i] / 30
        numeroDeProdutosDia = mediaMensal[i]
        for j in range(0, 30):
            dias.append(dia)
            dia += 1
            produtosPorDia.append(numeroDeProdutosDia)
            numeroDeProdutosDia -= mediaDeProdutos

    for i in range(1, NUMERODEPRODUTOS + 1):
        mediaDiaTotal += float(lista[i][9])
        estoqueIdealTotal += float(lista[i][10])

    numeroEstoqueAtual = estoqueIdealTotal
    for i in range(0, (NUMERODEMESES * 30)):
        valorAdicional = 0
        if i == 0:
            numeroDeProdutosNoEstoque.append(numeroEstoqueAtual)
        else:
            if i % 8 == 0:
                for j in range(1, NUMERODEPRODUTOS):
                    if lista[j][8] == "C":
                        valorAdicional += float(lista[j][10])
            if i % 18 == 0:
                for j in range(1, NUMERODEPRODUTOS):
                    if lista[j][8] == "B":
                        valorAdicional += float(lista[j][10])
            if i % 28 == 0:
                for j in range(1, NUMERODEPRODUTOS):
                    if lista[j][8] == "A":
                        valorAdicional += float(lista[j][10])
            numeroEstoqueAtual = numeroEstoqueAtual - mediaDiaTotal + valorAdicional
            numeroDeProdutosNoEstoque.append(numeroEstoqueAtual)

    plt.plot(dias, produtosPorDia, "r")
    plt.plot(dias, numeroDeProdutosNoEstoque, "blue")
    plt.show()


# Gerar grafico de proporção de produtos tipo A, B e C.
def grafico_2():
    grupos = ["A", "B", "C"]
    A = 0
    B = 0
    C = 0

    lista = csv_para_lista()

    for i in range(1, len(lista)):
        if lista[i][8] == "A":
            A += 1
        elif lista[i][8] == "B":
            B += 1
        else:
            C += 1
    valores = [A, B, C]
    # print(valores)
    plt.bar(grupos, valores)
    plt.xlabel("Classificação")
    plt.ylabel("Proporção")
    plt.show()


CONTADORES = ["#0", "#1", "#2", "#3", "#4", "#5", "#6", "#7", "#8", "#9", "#10", "#11", "#12", "#13", "#14", "#15",
              "#16",
              "#17", "#18", "#19", "#20"]
