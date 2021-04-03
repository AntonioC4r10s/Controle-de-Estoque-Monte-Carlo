import tkinter as tk
from lib.gestorDeDados import geraDados
from lib.ferramentas import *

#Janela principal
janela = tk.Tk()
largura = 720
altura = 480
janela.title("Controle de Estoque")
janela.resizable(0, 0)
janela.geometry("%dx%d" % (largura, altura))
janela.config(bg="#C0C0C0")

#Containers
container1 = tk.Frame(master=janela, width=largura*0.95, height=altura*0.9, bg="white").pack()
container2 = tk.Frame(master=janela, bg="white", pady=2).pack()

numeroDeProdutos = 20
file = open('estoque.csv', 'w', newline='', encoding='utf-8')
#Funções:
def geraNovosDados(numeroDeProdutos, file):
    geraDados(numeroDeProdutos, file)


#Botões
botao1 = tk.Button(master=container2, text="Gerar", width=10, height=15, command=geraNovosDados(numeroDeProdutos, file)).pack(side=tk.LEFT, padx=largura*0.025, pady=2)
botao2 = tk.Button(master=container2, text="Grafico 1", width=10, height=15).pack(side=tk.LEFT, padx=largura/4 + largura*0.025, pady=2)
botao3 = tk.Button(master=container2, text="Grafico 2", width=10, height=15).pack(side=tk.RIGHT, padx=largura*0.025, pady=2)

tk.mainloop()
