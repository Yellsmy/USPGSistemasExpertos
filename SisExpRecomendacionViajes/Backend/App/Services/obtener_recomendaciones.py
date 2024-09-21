from .consultar_clima import obtener_clima_simulado
from App.Models.recomendaciones import Recomendacion

def inferir_recomendaciones(preferencia, temporada, presupuesto, latitud_usuario, longitud_usuario, pais_id, region_id, fecha_viaje):
    recomendaciones = Recomendacion.query.filter_by(
        actividad=preferencia,
        epoca=temporada,
        presupuesto=presupuesto
    ).all()

    destinos = []
    for recomendacion in recomendaciones:
        # Consulta el clima para el destino en la fecha de viaje
        clima = obtener_clima_simulado(pais_id, region_id, fecha_viaje)

        # Si no se encuentra clima, omitir este destino
        if not clima:
            continue

        # Filtrar si el clima no es adecuado
        if preferencia == "Playa" and clima['clima'] in ['Lluvioso', 'Nevado']:
            continue

        destinos.append({
            "destino": recomendacion.destino,
            "clima": clima['clima'],
            "temperatura_min": clima['temperatura_min'],
            "temperatura_max": clima['temperatura_max'],
            "humedad": clima['humedad'],
            "velocidad_viento": clima['velocidad_viento']
        })

    return destinos
