import tkinter as tk
from  tkinter import ttk
from lib.gestorDeDados import geraDados

#Funções:
def geraNovosDados(numeroDeProdutos):
    geraDados(numeroDeProdutos)
    #restart_program()

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

#Botões
botao1 = tk.Button(master=container2, text="Gerar", width=10, height=15, command=lambda: geraNovosDados(numeroDeProdutos)).pack(side=tk.LEFT, padx=largura*0.025, pady=2)
botao2 = tk.Button(master=container2, text="Grafico 1", width=10, height=15).pack(side=tk.LEFT, padx=largura/4 + largura*0.025, pady=2)
botao3 = tk.Button(master=container2, text="Grafico 2", width=10, height=15).pack(side=tk.RIGHT, padx=largura*0.025, pady=2)

#tabela
tree = ttk.Treeview(container1, selectmode="browse", column=["column1","column2","column3","column4","column5",
                                                             "column6","column7","column8","column9","column10","column11"])

tk.mainloop()
