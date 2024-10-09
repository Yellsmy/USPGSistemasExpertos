from App.Models.pronostico import Clima, Pronostico
from datetime import datetime

# Diccionario para convertir el nombre del mes a su número
meses_a_numero = {
    "Enero": 1, "Febrero": 2, "Marzo": 3, "Abril": 4, 
    "Mayo": 5, "Junio": 6, "Julio": 7, "Agosto": 8, 
    "Septiembre": 9, "Octubre": 10, "Noviembre": 11, "Diciembre": 12
}

# Función para obtener el clima del destino recomendado
def obtener_clima_simulado(pais_id, fecha_viaje):
    mes_viaje = int(fecha_viaje.month)
    dia_viaje = fecha_viaje.day
      
    # Obtenemos el pronóstico para el país y la temporada correspondiente
    pronosticos = Pronostico.query.filter_by(id_pais=pais_id).all()
    for pronostico in pronosticos:
        mes_inicio_num = meses_a_numero[pronostico.mes_inicio]
        #print("Mes recuperado inicio: ", mes_inicio_num)
        mes_fin_num = meses_a_numero[pronostico.mes_fin]
        #print("Mes recuperado fin: ", mes_fin_num)

        if (mes_inicio_num <= mes_viaje <= mes_fin_num) or (mes_inicio_num > mes_fin_num and (mes_viaje >= mes_inicio_num or mes_viaje <= mes_fin_num)):        
            # Búsqueda del clima para el día seleccionado
            clima_dia = Clima.query.filter_by(
                id_temporada=pronostico.id_temporada,
                dia=dia_viaje
            ).first()

            if clima_dia:
                #print("TEMPORADA: ", clima_dia.id_temporada)
                return {
                    "clima": clima_dia.clima,
                    "temperatura_min": clima_dia.temperatura_min,
                    "temperatura_max": clima_dia.temperatura_max,
                    "humedad": clima_dia.humedad,
                    "velocidad_viento": clima_dia.velocidad_viento,
                    "temporada": pronostico.temporada.temporada
                }   
    return None