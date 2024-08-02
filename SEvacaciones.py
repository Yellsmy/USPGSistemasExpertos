class SEvacaciones:
    def __init__(self):
        # Tupla con las reglas que se han definido
        self.reglas = [
            (("Playa", "Verano", "Alto"), ["Maldivas", "Hawái"]),
            (("Playa", "Verano", "Medio"), ["Cancún", "Miami"]),
            (("Playa", "Verano", "Bajo"), ["Monterrico", "Puerto San José"]),
            (("Montaña", "Invierno", "Alto"), ["Aspen", "Zermatt"]),
            (("Montaña", "Verano", "Bajo"), ["Hobbitenango", "Sierra de Lacandón"]),
            (("Aventura", "Primavera", "Alto"), ["Nueva Zelanda", "Costa Rica"]),
            (("Aventura", "Primavera", "Bajo"), ["Reserva Natural Privada Ram Tzul", "Cerro Tzankujil"])
        ]
    
    # Método para sacar las recomendaciones de acuerdo a las preferencias del usuario
    def inferir_recomendaciones(self, hechos):
        recomendaciones = []

        # Recorre cada regla en el conjunto de reglas
        for regla_hechos, destinos in self.reglas:
          
            todos_coinciden = True

            # Recorre cada hecho en la regla y si algún hecho de la regla no se cumple
            # la bandera se marca como False y termina el bucle
            for hecho in regla_hechos:
                if hecho not in hechos:
                    todos_coinciden = False
                    break

            # Si todos los hechos coinciden con los hechos se agrega los destinos asociados
            if todos_coinciden:
                recomendaciones.extend(destinos)

        return recomendaciones


    # Método para retornar las recomendaciones inferidas
    def recomendar_destino(self, preferencia, temporada, presupuesto):
        hechos = (preferencia, temporada, presupuesto)
        
        # Llama al método para inferir recomendaciones
        recomendaciones = self.inferir_recomendaciones(hechos)
        return recomendaciones


# Se crea una instancia del sistema experto
sistema = SEvacaciones()

# Método para obtener la entrada del usuario
def obtener_opcion(opciones):

    # Muestra las opciones de preferencias, temporadas y presupuestos
    for i, opcion in enumerate(opciones, 1):
        print(f"{i}. {opcion}")

    # Bucle para que el usuario ingrese la opción que desee
    while True:
        seleccion = input("Ingresa el número de una opción: ")
        errores = validacionErrores(seleccion, opciones)
        if errores is False: 
            return opciones[int(seleccion) - 1]


# Método para controlar errores
def validacionErrores(seleccion, opciones):
    if not seleccion.isdigit():
        print("Error!! debe ingresar el número de la opción de su elección")
        return True
    seleccion = int(seleccion)
    if seleccion < 1 or seleccion > len(opciones):
        print("Error!! la opción seleccionada es inválida")
        return True
    return False


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

