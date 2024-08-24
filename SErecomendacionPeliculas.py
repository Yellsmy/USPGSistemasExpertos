class SEpeliculas:
    def __init__(self):
        # Para el presente sistema se han definido estas reglas
        self.reglas = [
            (("Acción", "Corta", "Intensa"), ["Mad Max: Fury Road", "John Wick"]),
            (("Acción", "Larga", "Intensa"), ["The Dark Knight", "Inception"]),
            (("Drama", "Corta", "Tranquila"), ["The Pursuit of Happyness", "Moonlight"]),
            (("Drama", "Larga", "Tranquila"), ["Forrest Gump", "The Shawshank Redemption"]),
            (("Comedia", "Corta", "Ligera"), ["Superbad", "Zombieland"]),
            (("Comedia", "Larga", "Ligera"), ["The Hangover", "Dumb and Dumber"]),
            (("Ciencia Ficción", "Corta", "Intensa"), ["District 9", "Looper"]),
            (("Ciencia Ficción", "Larga", "Intensa"), ["Interstellar", "Blade Runner 2049"]),
        ]
    
    # Método para sacar las recomendaciones de acuerdo a las preferencias del usuario
    def inferir_recomendaciones(self, hechos):
        recomendaciones = []

        # Recorre cada regla en el conjunto de reglas
        for regla_hechos, peliculas in self.reglas:
          
            todos_coinciden = True

            # Recorre cada hecho en la regla y si algún hecho de la regla no se cumple
            # la bandera se marca como False y termina el bucle
            for hecho in regla_hechos:
                if hecho not in hechos:
                    todos_coinciden = False
                    break

            # Si todos los hechos coinciden con los hechos se agregan las películas asociadas
            if todos_coinciden:
                recomendaciones.extend(peliculas)

        return recomendaciones


    # Método para retornar las recomendaciones inferidas
    def recomendar_pelicula(self, genero, duracion, estilo):
        hechos = (genero, duracion, estilo)
        
        # Llama al método para inferir recomendaciones
        recomendaciones = self.inferir_recomendaciones(hechos)
        return recomendaciones


# Se crea una instancia del sistema experto
sistema = SEpeliculas()

# Método para obtener la entrada del usuario
def obtener_opcion(opciones):

    # Muestra las opciones de géneros, duraciones y estilos
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
    generos = ["Acción", "Drama", "Comedia", "Ciencia Ficción"]
    duraciones = ["Corta", "Larga"]
    estilos = ["Intensa", "Tranquila", "Ligera"]

    print("          ╔══════════════════════════════════════════╗")
    print("          ║     Sistema de Recomendaciones de Películas  ║")
    print("          ╚══════════════════════════════════════════╝")
    print("Bienvenido al sistema de recomendaciones de películas")
    print("Para darte una mejor recomendación necesitaremos algunos datos")
    print("\n")

    print("Selecciona tu preferencia de género:")
    genero = obtener_opcion(generos)
    print("\n")

    print("Selecciona la duración de la película que prefieres:")
    duracion = obtener_opcion(duraciones)
    print("\n")
    
    print("Selecciona el estilo de película que prefieres:")
    estilo = obtener_opcion(estilos)
    print("\n")
    
    print("╔══════════════════════════════════════════╗")
    print("║         Recomendaciones de Películas      ║")
    print("╚══════════════════════════════════════════╝")
    print("\n")

    recomendaciones = sistema.recomendar_pelicula(genero, duracion, estilo)
    print("Las películas recomendadas son:")
    if recomendaciones:
        for pelicula in recomendaciones:
            print(f"  - {pelicula}")
    else:
        print("  No hay recomendaciones disponibles.")

    print("\n")
    print("***************** | DISFRUTA TU PELÍCULA | *****************")
    print("\n")

if __name__ == "__main__":
    main()
