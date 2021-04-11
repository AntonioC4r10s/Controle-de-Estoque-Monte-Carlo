from lib.gestorDeDados import *
import tkinter as tk
from tkinter import ttk

# Janela principal
janela = tk.Tk()
LARGURA = 645
ALTURA = 300
janela.title("Controle de Estoque")
janela.resizable(0, 0)
janela.geometry("%dx%d" % (LARGURA, ALTURA))
janela.config(bg="#ADD8E6")

lista = csv_para_lista()

# tabela.
my_tree = ttk.Treeview(janela)
my_tree['columns'] = (lista[0])
vsb = ttk.Scrollbar(janela, orient="vertical", command=my_tree.yview)
my_tree.configure(yscrollcommand=vsb.set)
vsb.place(x=LARGURA - 20, y=21, height=178 + 44)

# Passando os dados da lista para a Tree.
for i in range(0, len(lista[0])):
    if 0 < i < 7:
        my_tree.column(CONTADORES[i], width=40, minwidth=25)
        my_tree.heading(CONTADORES[i], text=lista[0][i], anchor=tk.W)
    else:
        if i > 11:
            break
        my_tree.column(CONTADORES[i], width=77, minwidth=25)
        my_tree.heading(CONTADORES[i], text=lista[0][i], anchor=tk.N)
# Adicionando intens na Tree.
for i in range(1, len(lista)):
    listaAux = []
    for j in range(1, len(lista[i])):
        listaAux.append(lista[i][j])
    my_tree.insert(parent="", index='end', iid=i, text=lista[i][0], values=listaAux)
my_tree.pack(pady=20)

# my_tree.item(1, values="0")

# Container para armazenar os botões.
container = tk.Frame(master=janela, bg="white", pady=2).pack()

# Botões.
botao1 = tk.Button(master=container, text="Grafico 2", width=10, height=15, command=lambda: grafico_2()).pack(
    side=tk.RIGHT)
botao2 = tk.Button(master=container, text="Grafico 1", width=10, height=15, command=lambda: grafico_3()).pack(
    side=tk.RIGHT, padx=2)
botao3 = tk.Button(master=container, text="Gerar", width=10, height=15,
                   command=lambda: gera_novos_dados(NUMERODEPRODUTOS, my_tree)).pack(side=tk.RIGHT)
labelQuantidadeDeProdutos = tk.Label(master=container, text=str(NUMERODEPRODUTOS) + " Produtos", bg='white').pack(
    side=tk.LEFT)

tk.mainloop()
