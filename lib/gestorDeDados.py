import csv
import random

def numAleatorio(a, b):
    return random.randint(a, b)

def geraDados(numeroDeProdutos):
    # abre ou cria o arquivo
    file = open('estoque.csv', 'w', newline='', encoding='utf-8')
    # cria o objeto de gravação
    w = csv.writer(file)

    w.writerow(['produto', '1', '2', '3', '4', '5', '6', 'total', 'relativo', 'acumulado', 'classificacao', 'mediaDia',
                'estoqueIdeal'])

    for i in range(numeroDeProdutos):
        id = i+1
        mes_1 = numAleatorio(0, 10)
        mes_2 = numAleatorio(0, 10)
        mes_3 = numAleatorio(0, 10)
        mes_4 = numAleatorio(0, 10)
        mes_5 = numAleatorio(0, 10)
        mes_6 = numAleatorio(0, 10)
        total = (mes_1 + mes_2 + mes_3 + mes_4 +mes_5 + mes_6)



        numParaClassif = random.random()

        if (numParaClassif < 0.2):
            classificacao = 'A'
        elif (numParaClassif < 0.5):
            classificacao = 'B'
        else:
            classificacao = 'C'

        w.writerow([id, mes_1, mes_2, mes_3, mes_4, mes_5, mes_6, total, classificacao])
    file.close()

def calculaDados(file):
    pass