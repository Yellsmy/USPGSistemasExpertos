"""
class Nodo:
    def __init__(self, etiqueta):
        self.etiqueta = etiqueta
        self.arcos = []

    def agregar_arco(self, destino, etiqueta_arco):
        arco = Arco(self, destino, etiqueta_arco)
        self.arcos.append(arco)


class Arco:
    def __init__(self, origen, destino, etiqueta):
        self.origen = origen
        self.destino = destino
        self.etiqueta = etiqueta

    def __str__(self):
        return f'{self.origen.etiqueta} -- {self.etiqueta} --> {self.destino.etiqueta}'


class RedSemantica:
    def __init__(self):
        self.nodos = []

    def crear_nodo(self, etiqueta):
        nodo = Nodo(etiqueta)
        self.nodos.append(nodo)
        return nodo

    def mostrar_red(self):
        for nodo in self.nodos:
            for arco in nodo.arcos:
                print(arco)


if __name__ == "__main__":
    red = RedSemantica()

    bien = red.crear_nodo("bien")
    plumas = red.crear_nodo("plumas")
    huevos = red.crear_nodo("huevos")
    patas_largas = red.crear_nodo("largas")
    no_puede = red.crear_nodo("no_puede")
    muy_bien = red.crear_nodo("muy bien")
    piel = red.crear_nodo("piel")
    mar = red.crear_nodo("mar")
    leche = red.crear_nodo("leche")
    pelo = red.crear_nodo("pelo")
    carne = red.crear_nodo("carne")
    animal = red.crear_nodo("ANIMAL")
    vida = red.crear_nodo("vida")
    sentir = red.crear_nodo("sentir")
    moverse = red.crear_nodo("moverse")
    avestruz = red.crear_nodo("AVESTRUZ")
    albatros = red.crear_nodo("ALBATROS")
    ballena = red.crear_nodo("BALLENA")
    tigre = red.crear_nodo("TIGRE")
    ave = red.crear_nodo("AVE")
    mamifero = red.crear_nodo("MAMIFERO")

    # Lado derecho
    tigre.agregar_arco(carne, "come")
    tigre.agregar_arco(mamifero, "tipo de")

    ballena.agregar_arco(piel, "tiene")
    ballena.agregar_arco(mar, "vive_en")
    ballena.agregar_arco(mamifero, "tipo de")

    mamifero.agregar_arco(leche, "da")
    mamifero.agregar_arco(pelo, "tiene")
    mamifero.agregar_arco(animal, "tipo_de")
    
    
    #Lado izquierdo
    avestruz.agregar_arco(patas_largas, "patas")
    avestruz.agregar_arco(no_puede, "vuela")
    avestruz.agregar_arco(ave, "tipo_de")

    albatros.agregar_arco(muy_bien, "vuela")
    albatros.agregar_arco(ave, "tipo_de")
    
    ave.agregar_arco(bien, "vuela")
    ave.agregar_arco(plumas, "tiene")
    ave.agregar_arco(huevos, "pone")
    ave.agregar_arco(animal, "tipo_de")
    
    #Centro
    animal.agregar_arco(vida, "tiene")
    animal.agregar_arco(sentir, "puede")
    animal.agregar_arco(moverse, "puede")
    
    red.mostrar_red()
"""

import networkx as nx # type: ignore
import matplotlib.pyplot as plt # type: ignore

# Creación del grafo
G = nx.DiGraph()

# Listas de nodos y aristas
nodos = ["ANIMAL", "vida", "sentir", "moverse", "AVE", "plumas", "huevos", "bien",
         "AVESTRUZ", "largas", "no_puede", "ALBATROS", "muy_bien", "MAMIFERO", 
         "piel", "mar", "leche", "pelo", "TIGRE", "carne", "BALLENA"]

aristas = [
    ("ANIMAL", "vida", "tiene"),
    ("ANIMAL", "sentir", "puede"),
    ("ANIMAL", "moverse", "puede"),
    ("ANIMAL", "AVE", "tipo_de"),
    ("ANIMAL", "MAMIFERO", "tipo_de"),
    ("AVE", "plumas", "tiene"),
    ("AVE", "huevos", "pone"),
    ("AVE", "bien", "vuela"),
    ("AVE", "AVESTRUZ", "tipo_de"),
    ("AVE", "ALBATROS", "tipo_de"),
    ("AVESTRUZ", "largas", "patas"),
    ("AVESTRUZ", "no_puede", "vuela"),
    ("ALBATROS", "muy_bien", "vuela"),
    ("MAMIFERO", "piel", "tiene"),
    ("MAMIFERO", "leche", "da"),
    ("MAMIFERO", "pelo", "tiene"),
    ("MAMIFERO", "BALLENA", "tipo_de"),
    ("MAMIFERO", "TIGRE", "tipo_de"),
    ("BALLENA", "piel", "tiene"),
    ("BALLENA", "mar", "vive_en"),
    ("TIGRE", "carne", "come")
]

# Añadiendo nodos
G.add_nodes_from(nodos)

# Añadiendo aristas
for origen, destino, etiqueta in aristas:
    G.add_edge(origen, destino, label=etiqueta)

# Posicionamiento de los nodos manualmente para asemejarse a la imagen
pos = {
    "ANIMAL": (0, 0),
    "vida": (0, 1),
    "sentir": (1, 1),
    "moverse": (-1, 1),
    "AVE": (-2, 0),
    "plumas": (-3, 1),
    "huevos": (-3, 0.5),
    "bien": (-3, 0),
    "AVESTRUZ": (-4, 0),
    "largas": (-5, 0.5),
    "no_puede": (-5, 0),
    "ALBATROS": (-2, -1),
    "muy_bien": (-3, -1),
    "MAMIFERO": (2, 0),
    "piel": (3, 0.5),
    "mar": (3, 0),
    "leche": (3, -0.5),
    "pelo": (3, -1),
    "TIGRE": (2, -1),
    "carne": (3, -1.5),
    "BALLENA": (2, 0.5)
}

# Dibujando nodos y aristas
nx.draw(G, pos, with_labels=True, node_size=3000, node_color="lightgrey", font_size=10, font_weight="bold", edge_color="black")

# Dibujando etiquetas en las aristas
edge_labels = nx.get_edge_attributes(G, 'label')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='black')

# Ajustes adicionales de visualización para que se parezca más a la imagen
plt.gca().set_facecolor('white')  # Cambia el fondo a blanco
plt.show()
