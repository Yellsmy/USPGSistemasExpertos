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
