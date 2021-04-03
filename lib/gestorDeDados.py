import csv
import random

def numAleatorio(a, b):
    return random.randint(a, b)

def geraDados(numeroDeProdutos):
    # abre ou cria o arquivo
    file = open('estoque.csv', 'w', newline='', encoding='utf-8')
    # cria o objeto de gravação
    w = csv.writer(file)

    w.writerow(['produto', '1', '2', '3', '4', '5', '6', 'total', 'classificacao', 'mediaDia',
                'estoqueIdeal'])

    numeroDeProdutosMax = 20

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

#geraDados(10)