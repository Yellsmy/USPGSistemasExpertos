import mysql.connector
import networkx as nx
import matplotlib.pyplot as plt

class Nodo:
    def __init__(self, etiqueta):
        self.etiqueta = etiqueta
        self.arcos = []

    def agregar_arco(self, destino, etiqueta_arco):
        self.arcos.append(Arco(self, destino, etiqueta_arco))

class Arco:
    def __init__(self, origen, destino, etiqueta):
        self.origen = origen
        self.destino = destino
        self.etiqueta = etiqueta

class RedSemantica:
    def __init__(self, db_config):
        self.db_config = db_config
        self.nodos = []
        self.conectar_db()
        self.cargar_desde_db()

    def conectar_db(self):
        self.conn = mysql.connector.connect(**self.db_config)
        self.cursor = self.conn.cursor()

    def crear_nodo(self, etiqueta):
        nodo = Nodo(etiqueta)
        self.nodos.append(nodo)
        self.cursor.execute("INSERT IGNORE INTO nodos (etiqueta) VALUES (%s)", (etiqueta,))
        self.conn.commit()
        return nodo

    def agregar_arco(self, origen, destino, etiqueta):
        origen.agregar_arco(destino, etiqueta)
        self.cursor.execute("INSERT INTO arcos (origen, destino, etiqueta) VALUES (%s, %s, %s)", (origen.etiqueta, destino.etiqueta, etiqueta))
        self.conn.commit()

    def cargar_desde_db(self):
        self.cursor.execute("SELECT etiqueta FROM nodos")
        nodos_db = {row[0]: Nodo(row[0]) for row in self.cursor.fetchall()}
        self.nodos = list(nodos_db.values())

        self.cursor.execute("SELECT origen, destino, etiqueta FROM arcos")
        for origen, destino, etiqueta in self.cursor.fetchall():
            nodos_db[origen].agregar_arco(nodos_db[destino], etiqueta)

    def generar_grafico(self):
        G = nx.DiGraph()

        # Añadir nodos y arcos al grafo de NetworkX
        for nodo in self.nodos:
            G.add_node(nodo.etiqueta)
            for arco in nodo.arcos:
                G.add_edge(nodo.etiqueta, arco.destino.etiqueta, label=arco.etiqueta)

        # Posiciones manuales para los nodos
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

        # Configuración del dibujo
        options = {
            "node_color": "lightblue",
            "node_size": 3000,
            "edge_color": "black",
            "width": 2,
            "font_size": 10,
            "font_weight": "bold",
        }

        # Dibujar nodos y arcos
        nx.draw(G, pos, with_labels=True, **options)

        # Dibujar etiquetas en las aristas
        edge_labels = nx.get_edge_attributes(G, 'label')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='black')

        # Cambiar fondo a blanco
        plt.gca().set_facecolor('white')

        # Mostrar gráfico
        plt.show()

if __name__ == "__main__":
    # Conexión con la base de datos
    db_config = {
        'user': 'root',
        'password': 'yltojg123*',
        'host': 'localhost',
        'database': 'sistema_experto'
    }

    red = RedSemantica(db_config)

    # Crear nodos y relaciones en la base de datos
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

    # Agregar relaciones (arcos)
    red.agregar_arco(tigre, carne, "come")
    red.agregar_arco(tigre, mamifero, "tipo de")

    red.agregar_arco(ballena, piel, "tiene")
    red.agregar_arco(ballena, mar, "vive_en")
    red.agregar_arco(ballena, mamifero, "tipo de")

    red.agregar_arco(mamifero, leche, "da")
    red.agregar_arco(mamifero, pelo, "tiene")
    red.agregar_arco(mamifero, animal, "tipo_de")

    red.agregar_arco(avestruz, patas_largas, "patas")
    red.agregar_arco(avestruz, no_puede, "vuela")
    red.agregar_arco(avestruz, ave, "tipo_de")

    red.agregar_arco(albatros, muy_bien, "vuela")
    red.agregar_arco(albatros, ave, "tipo_de")

    red.agregar_arco(ave, bien, "vuela")
    red.agregar_arco(ave, plumas, "tiene")
    red.agregar_arco(ave, huevos, "pone")
    red.agregar_arco(ave, animal, "tipo_de")

    red.agregar_arco(animal, vida, "tiene")
    red.agregar_arco(animal, sentir, "puede")
    red.agregar_arco(animal, moverse, "puede")

    # Generar y mostrar el gráfico
    red.generar_grafico()

