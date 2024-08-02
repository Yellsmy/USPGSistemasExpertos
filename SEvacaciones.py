class SEvacaciones:
    def __init__(self):
        # Reglas definidas como una lista de tuplas
        self.reglas = [
            (("Playa", "Verano", "Alto"), ["Maldivas", "Hawái"]),
            (("Playa", "Verano", "Medio"), ["Cancún", "Miami"]),
            (("Playa", "Verano", "Bajo"), ["Monterrico", "Puerto San José"]),
            (("Montaña", "Invierno", "Alto"), ["Aspen", "Zermatt"]),
            (("Montaña", "Verano", "Bajo"), ["Hobbitenango", "Sierra de Lacandón"]),
            (("Aventura", "Primavera", "Alto"), ["Nueva Zelanda", "Costa Rica"]),
            (("Aventura", "Primavera", "Bajo"), ["Reserva Natural Privada Ram Tzul", "Cerro Tzankujil"])
        ]
    
    def inferir_recomendaciones(self, hechos):
        recomendaciones = []
        for regla_hechos, destinos in self.reglas:
            # Verificar si todos los hechos coinciden
            if all(hecho in hechos for hecho in regla_hechos):
                recomendaciones.extend(destinos)
        return recomendaciones
    
    def recomendar_destino(self, preferencia, temporada, presupuesto):
        # Hechos conocidos
        hechos = (preferencia, temporada, presupuesto)
        
        # Inferir recomendaciones
        recomendaciones = self.inferir_recomendaciones(hechos)
        return recomendaciones if recomendaciones else ["No hay recomendaciones disponibles"]

# Crear una instancia del sistema experto
sistema = SEvacaciones()

def obtener_opcion(opciones):
    for idx, opcion in enumerate(opciones, 1):
        print(f"{idx}. {opcion}")
    while True:
        try:
            seleccion = int(input("Ingresa el número de una opción: "))
            if 1 <= seleccion <= len(opciones):
                return opciones[seleccion - 1]
            else:
                print("Opción inválida. Intenta de nuevo.")
        except ValueError:
            print("Entrada inválida. Por favor ingresa un número.")

def validacionErrores(seleccion, opciones):
    if not seleccion.isnumeric():
        print("Error!! debe ingresar el número de la opción de su elección")
        return False
    elif int(seleccion) > len(opciones) or int(seleccion) < 1:
        print("Error!! la opción seleccionada es inválida")
        return False
    return True

# Ejemplo de uso
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

    recomendaciones = sistema.recomendar_destino(preferencia, temporada, presupuesto)
    print("Los destinos recomendados son:")
    if recomendaciones:
        for destino in recomendaciones:
            print(f"  - {destino}")
    else:
        print("  No hay recomendaciones disponibles.")

    print("\n")
    print("***************** | DISFRUTA TU VIAJE | *****************")

if __name__ == "__main__":
    main()

