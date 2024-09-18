class RedBayesianaViajes:
    def __init__(self):

        self.probabilidadDestino = {
            "Maldivas": 0.05,
            "Cancún": 0.1,
            "Monterrico": 0.1,
            "Aspen": 0.05,
            "Zermatt": 0.05,
            "Hobbitenango": 0.05
        }

        self.probabilidadPreferenciaDadoDestino = {
            "Playa": {"Maldivas": 0.9, "Cancún": 0.8, "Monterrico": 0.7, "Aspen": 0.1, "Zermatt": 0.1, "Hobbitenango": 0.2},
            "Montaña": {"Maldivas": 0.1, "Cancún": 0.1, "Monterrico": 0.2, "Aspen": 0.9, "Zermatt": 0.8, "Hobbitenango": 0.9},
            "Aventura": {"Maldivas": 0.5, "Cancún": 0.6, "Monterrico": 0.4, "Aspen": 0.5, "Zermatt": 0.4, "Hobbitenango": 0.6}
        }

        self.probabilidadTemporadaDadoDestino = {
            "Verano": {"Maldivas": 0.8, "Cancún": 0.9, "Monterrico": 0.7, "Aspen": 0.3, "Zermatt": 0.2, "Hobbitenango": 0.6},
            "Invierno": {"Maldivas": 0.2, "Cancún": 0.3, "Monterrico": 0.4, "Aspen": 0.9, "Zermatt": 0.8, "Hobbitenango": 0.4},
            "Primavera": {"Maldivas": 0.6, "Cancún": 0.7, "Monterrico": 0.5, "Aspen": 0.5, "Zermatt": 0.6, "Hobbitenango": 0.8},
            "Otoño": {"Maldivas": 0.4, "Cancún": 0.5, "Monterrico": 0.6, "Aspen": 0.6, "Zermatt": 0.4, "Hobbitenango": 0.7}
        }

        self.probabilidadPresupuestoDadoDestino = {
            "Alto": {"Maldivas": 0.9, "Cancún": 0.7, "Monterrico": 0.3, "Aspen": 0.9, "Zermatt": 0.9, "Hobbitenango": 0.4},
            "Medio": {"Maldivas": 0.4, "Cancún": 0.6, "Monterrico": 0.5, "Aspen": 0.3, "Zermatt": 0.3, "Hobbitenango": 0.6},
            "Bajo": {"Maldivas": 0.1, "Cancún": 0.2, "Monterrico": 0.8, "Aspen": 0.1, "Zermatt": 0.1, "Hobbitenango": 0.8}
        }

    def inferir_probabilidad_destino(self, destino, preferencia, temporada, presupuesto):
        prob_destino = self.probabilidadDestino[destino]
        prob_preferencia = self.probabilidadPreferenciaDadoDestino[preferencia][destino]
        prob_temporada = self.probabilidadTemporadaDadoDestino[temporada][destino]
        prob_presupuesto = self.probabilidadPresupuestoDadoDestino[presupuesto][destino]

        # Probabilidad combinada
        prob_total = prob_destino * prob_preferencia * prob_temporada * prob_presupuesto
        return prob_total

    def recomendar_destino(self, preferencia, temporada, presupuesto):
        destinos = list(self.probabilidadDestino.keys())
        probabilidades = {}

        for destino in destinos:
            probabilidades[destino] = self.inferir_probabilidad_destino(destino, preferencia, temporada, presupuesto)

        total_probabilidad = sum(probabilidades.values())
        for destino in probabilidades:
            probabilidades[destino] /= total_probabilidad

        recomendaciones = []
        for destino, probabilidad in probabilidades.items():
            if probabilidad > 0:
                recomendaciones.append((destino, probabilidad * 100))

        return recomendaciones

def obtener_opcion(opciones):
    for i, opcion in enumerate(opciones, 1):
        print(f"{i}. {opcion}")
    
    while True:
        seleccion = input("Ingresa el número de una opción: ")
        if not seleccion.isdigit():
            print("Error: Por favor, ingresa un número válido.")
        else:
            seleccion = int(seleccion)
            if 1 <= seleccion <= len(opciones):
                return opciones[seleccion - 1]
            else:
                print("Error: Selección fuera de rango. Intenta de nuevo.")

# Main
def main():
    preferencias = ["Playa", "Montaña", "Aventura"]
    temporadas = ["Verano", "Invierno", "Primavera", "Otoño"]
    presupuestos = ["Alto", "Medio", "Bajo"]

    print("          ╔══════════════════════════════════════════╗")
    print("          ║     Sistema de Recomendaciones de Viaje  ║")
    print("          ╚══════════════════════════════════════════╝")
    print("Bienvenido al sistema de recomendaciones de destinos de viaje")
    print("Para darte una mejor recomendación necesitaremos algunos datos")
    print("\n")

    print("Selecciona tu preferencia de destino:")
    preferencia = obtener_opcion(preferencias)
    print("\n")

    print("Selecciona la temporada en la que quieres viajar:")
    temporada = obtener_opcion(temporadas)
    print("\n")
    
    print("Selecciona tu presupuesto:")
    presupuesto = obtener_opcion(presupuestos)
    print("\n")
    
    print("╔══════════════════════════════════════════╗")
    print("║         Recomendaciones de Destinos      ║")
    print("╚══════════════════════════════════════════╝")
    print("\n")

    sistema = RedBayesianaViajes()
    recomendaciones = sistema.recomendar_destino(preferencia, temporada, presupuesto)

    if recomendaciones:
        print("Los destinos recomendados son:")
        for destino, probabilidad in recomendaciones:
            print(f"  - {destino} con una probabilidad del {probabilidad:.2f}%")
    else:
        print("  No hay recomendaciones disponibles.")
    
    print("\n")
    print("***************** | DISFRUTA TU VIAJE | *****************")
    print("\n")

if __name__ == "__main__":
    main()