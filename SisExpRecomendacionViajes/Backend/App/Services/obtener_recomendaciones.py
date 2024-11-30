import os
from geopy.distance import geodesic
from App.Models.recomendaciones import Recomendacion
from App.Models.pronostico import Pais
from App.Services.consultar_clima import obtener_clima_simulado
from flask import current_app


DISTANCIA_MINIMA_MEDIO = 100  # Distancia mínima para un presupuesto medio (km)
DISTANCIA_MAXIMA_BAJO = 99.9  # Distancia máxima para un presupuesto bajo (km)

def inferir_recomendaciones(preferencia, temporada, presupuesto, latitud_usuario, longitud_usuario, paisIngreso, fecha_viaje, tipoRecomendacion):

    #print(f"Preferencia: {preferencia}, Temporada: {temporada}, Presupuesto: {presupuesto}")
    #print(f"Latitud Usuario: {latitud_usuario}, Longitud Usuario: {longitud_usuario}")
    #print(f"País Ingreso: {paisIngreso}, Fecha de Viaje: {fecha_viaje}")

    # Buscar el país por nombre
    pais = Pais.query.filter_by(pais=paisIngreso).first()

    if not pais:
        print("País no encontrado")
        return {"mensaje": "País no encontrado"}, 404
    
    pais_id = pais.id_pais 
    #print(f"País recuperado: {pais.pais} (ID: {pais_id})")

    # Si el presupuesto es alto, se filtran solo recomendaciones en el extranjero
    if presupuesto == "Alto":
        recomendaciones = Recomendacion.query.filter(
            Recomendacion.actividad == preferencia,
            Recomendacion.id_pais != pais_id
        ).all()

    # Si el presupuesto es medio, se filtran recomendaciones nacionales, pero se aplica la distancia mínima
    elif presupuesto == "Medio":
        recomendaciones = Recomendacion.query.filter(
            Recomendacion.actividad == preferencia,
            Recomendacion.id_pais == pais_id  
        ).all()
        
        recomendaciones = [
            recomendacion for recomendacion in recomendaciones
            if calcular_distancia(latitud_usuario, longitud_usuario, recomendacion.latitud, recomendacion.longitud) >= DISTANCIA_MINIMA_MEDIO
        ]
        #print(f"Recomendaciones tras filtrar por distancia mínima (medio): {len(recomendaciones)}")

    # Si el presupuesto es bajo, se filtran recomendaciones nacionales, pero se aplica la distancia máxima
    elif presupuesto == "Bajo":
        recomendaciones = Recomendacion.query.filter(
            Recomendacion.actividad == preferencia,
            Recomendacion.id_pais == pais_id  # Solo dentro del país del usuario
        ).all()

        recomendaciones = [
            recomendacion for recomendacion in recomendaciones
            if calcular_distancia(latitud_usuario, longitud_usuario, recomendacion.latitud, recomendacion.longitud) <= DISTANCIA_MAXIMA_BAJO
        ]
        #print(f"Recomendaciones tras filtrar por distancia máxima (bajo): {len(recomendaciones)}")

    destinos = []
    for recomendacion in recomendaciones:

        # Construir la URL de la imagen
        image_url = f"{recomendacion.imagen}"

        
        if tipoRecomendacion == "personalizada":
            destinos.append({
                "destino": recomendacion.destino,
                "imagen_url": image_url
            })
        else:
            # Consultar el clima para el destino en la fecha de viaje
            clima = obtener_clima_simulado(recomendacion.id_pais, fecha_viaje)

            if not clima:
                print(f"No se encontró clima para el destino: {recomendacion.destino}")
                continue

            
            
            # Agregar la recomendación con el clima y la temporada
            destinos.append({
                "destino": recomendacion.destino,
                "clima": clima['clima'],
                "temperatura_min": clima['temperatura_min'],
                "temperatura_max": clima['temperatura_max'],
                "humedad": clima['humedad'],
                "velocidad_viento": clima['velocidad_viento'],
                "temporada": clima['temporada'],
                "imagen_url": image_url
            })
        #print(f"Destinos generados: {len(destinos)}")

    return destinos


# Función para calcular la distancia entre dos puntos geográficos usando la fórmula de Haversine
def calcular_distancia(lat1, lon1, lat2, lon2):
    coords_1 = (lat1, lon1)
    coords_2 = (lat2, lon2)
    return geodesic(coords_1, coords_2).kilometers
