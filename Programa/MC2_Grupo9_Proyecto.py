import networkx as nx 
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 
from matplotlib.figure import Figure

G = nx.Graph()
root = tk.Tk();
root.title("Algoritmos de Busqueda en Anchura y Profundidad")
root.configure(bg = "#b3f2fc")

anadir_vertice = tk.Entry(root)
anadir_vertice.pack()

labelV = tk.Label()
labelV.pack()


anadir_vertice_bt = tk.Button(root, text="Agregar Vertice", cursor="hand2", command= lambda:G.add_node(anadir_vertice.get()))
anadir_vertice_bt["command"] = lambda: informacion(labelV)

anadir_vertice_bt.pack()

anadir_arista1 = tk.Entry(root)
anadir_arista1.pack()
anadir_arista2 = tk.Entry(root)
anadir_arista2.pack()

anadir_aristas_bt = tk.Button(root, text="Agregar Aristas", cursor= "hand2", command=lambda:G.add_edge(anadir_arista1.get(),anadir_arista2.get()))
anadir_aristas_bt.pack()

def informacion(infoV):
    infoV = anadir_vertice.get()
    labelV["text"] = "Vertice Inicial: " + infoV



grafica = Figure(figsize=(4, 4))
grafica.set_facecolor(color= "#b3f2fc")
axes = grafica.add_subplot(111)
canvas = FigureCanvasTkAgg(grafica, root)
canvas.get_tk_widget().pack()

def dibujar_grafo(algoritmo=None):
    axes.clear()

    if algoritmo:
        pos = nx.spring_layout(G)
        nx.draw(G, pos=pos, ax=axes, with_labels=True)
        nx.draw_networkx_edges(G, pos=pos, edgelist=algoritmo, edge_color= "#5FCA42", ax=axes)
        nx.draw_networkx_nodes(G, pos=pos, nodelist=[anadir_vertice.get()]+[v for u, v in algoritmo], node_color="#628d96", edgecolors="#000000", ax=axes)
    else:
        nx.draw(G, ax=axes, with_labels=True)
        canvas.draw()

dibujar_grafo_bt = tk.Button(root, text="Dibujar Grafo", cursor="hand2", command=dibujar_grafo)
dibujar_grafo_bt.pack()

def busqueda_ancho():
    busqueda_ancho_recorrido=list(nx.bfs_edges(G,source=anadir_vertice.get()))
    dibujar_grafo(busqueda_ancho_recorrido)
    canvas.draw()

def busqueda_largo():
    busqueda_largo_recorrido = list(nx.dfs_edges(G,source=anadir_vertice.get()))
    dibujar_grafo(busqueda_largo_recorrido)
    canvas.draw()

bfs_button = tk.Button(root, text="Busqueda en Anchura", cursor="hand2", command=busqueda_ancho)
bfs_button.pack()
dfs_button = tk.Button(root, text="Busqueda en Profundidad", cursor="hand2", command=busqueda_largo)
dfs_button.pack()

root.mainloop()
