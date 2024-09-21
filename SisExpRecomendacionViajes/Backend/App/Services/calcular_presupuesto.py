from App.Services.amadeus_service import buscar_vuelos, buscar_hoteles

def calcular_presupuesto_viaje(token, origen, destino, fecha_salida, fecha_regreso, adultos, ciudad_hoteles):
    # Obtener precios de vuelos
    vuelos = buscar_vuelos(origen, destino, fecha_salida, adultos)
    if not vuelos:
        return None, "No se encontraron vuelos"
    
    precio_vuelo = float(vuelos[0]['price']['total'])
    
    # Obtener precios de hoteles
    hoteles = buscar_hoteles(ciudad_hoteles, fecha_salida, fecha_regreso, adultos)
    if not hoteles:
        return None, "No se encontraron hoteles"
    
    precio_hotel = float(hoteles[0]['offers'][0]['price']['total'])
    
    # Calcular el presupuesto total
    presupuesto_total = precio_vuelo + precio_hotel
    return presupuesto_total, None
