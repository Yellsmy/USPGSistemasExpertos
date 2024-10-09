from App.Models.recomendaciones import Recomendacion, db
from App.Models.pronostico import Pais
from flask import request

def agregar_recomendacion(data):
    pais = Pais.query.filter_by(pais=data['pais']).first()
    #print("País recuperado: ", pais)

    if not pais:
        return {"mensaje": "País no encontrado"}, 404

    # Crear una nueva recomendación
    nueva_recomendacion = Recomendacion(
        destino=data['destino'],
        actividad=data['actividad'],
        epoca=data['epoca'],
        presupuesto=data['presupuesto'],
        latitud=data['latitud'],
        longitud=data['longitud'],
        id_pais=pais.id_pais,
        imagen=data['imagen'] 
    )
    db.session.add(nueva_recomendacion)
    db.session.commit()
    return {"mensaje": "Recomendación agregada exitosamente"}, 201