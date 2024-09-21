from App.Models.recomendaciones import Recomendacion, db

def agregar_recomendacion(data):
    nueva_recomendacion = Recomendacion(
        destino=data['destino'],
        actividad=data['actividad'],
        epoca=data['epoca'],
        presupuesto=data['presupuesto'],
        latitud=data['latitud'],
        longitud=data['longitud']
    )
    db.session.add(nueva_recomendacion)
    db.session.commit()
    return {"mensaje": "Recomendación agregada exitosamente"}, 201
