from App.Models.pronostico import Clima, Pronostico
from datetime import datetime

def obtener_clima_simulado(pais_id, region_id, fecha_viaje):
    
    mes_viaje = fecha_viaje.strftime("%B")
    dia_viaje = fecha_viaje.day

    pronostico = Pronostico.query.filter_by(
        id_pais=pais_id,
        id_region=region_id
    ).filter(
        Pronostico.mes_inicio <= mes_viaje,
        Pronostico.mes_fin >= mes_viaje
    ).first()

    if not pronostico:
        return None
   
    clima_dia = Clima.query.filter_by(
        id_temporada=pronostico.id_temporada,
        dia=dia_viaje
    ).first()

    if not clima_dia:
        return None

    return {
        "clima": clima_dia.clima,
        "temperatura_min": clima_dia.temperatura_min,
        "temperatura_max": clima_dia.temperatura_max,
        "humedad": clima_dia.humedad,
        "velocidad_viento": clima_dia.velocidad_viento
    }
