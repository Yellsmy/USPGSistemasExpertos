import mysql.connector
from experta import Fact, KnowledgeEngine, Rule, P

# Conexión a la base de datos
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="*",
        database="sistemaexperto"
    )

# Función para obtener las recomendaciones de la base de datos
def obtener_recomendaciones(preferencia, temporada, presupuesto):
    conexion = connect_db()
    cursor = conexion.cursor(dictionary=True)
    query = """
    SELECT destino 
    FROM recomendaciones 
    WHERE preferencia = %s AND temporada = %s AND presupuesto = %s
    """
    cursor.execute(query, (preferencia, temporada, presupuesto))
    resultados = cursor.fetchall()
    conexion.close()
    return [resultado['destino'] for resultado in resultados]

# Definición de los hechos
class preferenciasUsuario(Fact):
    """Hechos que representan las preferencias del usuario."""
    preferencia = str
    temporada = str
    presupuesto = str

# Definición del motor de inferencia y reglas
class Recomendacion(KnowledgeEngine):
    """Motor de reglas que proporciona recomendaciones de viajes."""

    @Rule(preferenciasUsuario(preferencia="Playa", temporada="Verano", presupuesto="Alto"))
    def recomendar_playa_alto(self):
        destinos = obtener_recomendaciones("Playa", "Verano", "Alto")
        for destino in destinos:
            self.declare(Fact(recomendacion=destino))

    @Rule(preferenciasUsuario(preferencia="Playa", temporada="Verano", presupuesto="Bajo"))
    def recomendar_playa_bajo(self):
        destinos = obtener_recomendaciones("Playa", "Verano", "Bajo")
        for destino in destinos:
            self.declare(Fact(recomendacion=destino))

    @Rule(preferenciasUsuario(preferencia="Montaña", temporada="Invierno", presupuesto="Alto"))
    def recomendar_montana_alto(self):
        destinos = obtener_recomendaciones("Montaña", "Invierno", "Alto")
        for destino in destinos:
            self.declare(Fact(recomendacion=destino))

# Función para obtener la entrada del usuario
def obtener_opcion(opciones):
    for i, opcion in enumerate(opciones, 1):
        print(f"{i}. {opcion}")
    
    while True:
        seleccion = input("Ingresa el número de una opción: ")
        if seleccion.isdigit() and 1 <= int(seleccion) <= len(opciones):
            return opciones[int(seleccion) - 1]
        else:
            print("Opción inválida. Intenta de nuevo.")

# Función principal
def main():
    preferencias = ["Playa", "Montaña", "Aventura"]
    temporadas = ["Verano", "Invierno", "Primavera", "Otoño"]
    presupuestos = ["Alto", "Medio", "Bajo"]

    print("Bienvenido al sistema de recomendaciones de viajes")
    print("Por favor, selecciona tus opciones")

    print("Selecciona tu preferencia de destino:")
    preferencia = obtener_opcion(preferencias)
    print("\n")

    print("Selecciona la temporada en la que quieres viajar:")
    temporada = obtener_opcion(temporadas)
    print("\n")
    
    print("Selecciona tu presupuesto:")
    presupuesto = obtener_opcion(presupuestos)
    print("\n")

    # Crear instancia del motor de inferencia
    motorInferencia = Recomendacion()

    # Declarar los hechos sobre el usuario
    motorInferencia.reset()
    motorInferencia.declare(preferenciasUsuario(preferencia=preferencia, temporada=temporada, presupuesto=presupuesto))

    # Ejecutar el motor de inferencia
    motorInferencia.run()

    # Mostrar las recomendaciones generadas
    recomendaciones = []
    for fact in motorInferencia.facts.values():
        if fact.get("recomendacion"):
            recomendaciones.append(fact["recomendacion"])

    print("Destinos recomendados:")
    if recomendaciones:
        for destino in recomendaciones:
            print(f"  - {destino}")
    else:
        print("No se encontraron recomendaciones para tus preferencias.")

if __name__ == "__main__":
    main()
