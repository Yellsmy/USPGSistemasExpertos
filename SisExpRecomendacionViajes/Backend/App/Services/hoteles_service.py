import requests

def obtener_codigo_ciudad(nombre_ciudad):
    url = "https://hotels4.p.rapidapi.com/locations/search"

    querystring = {"query": nombre_ciudad, "locale": "en_US"}

    headers = {
        "X-RapidAPI-Key": "6a4c71839fmshffbeb71f0be5f4cp1eba34jsn6ce698b5ea40",  # Reemplaza con tu API Key de RapidAPI
        "X-RapidAPI-Host": "hotels4.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    if response.status_code == 200:
        # Extraer el destinationId del resultado
        resultados = response.json()
        if resultados['suggestions']:
            # Accedemos al primer resultado de sugerencia de ciudades
            for sugerencia in resultados['suggestions']:
                if sugerencia['group'] == 'CITY_GROUP':
                    # Retornamos el primer destinationId encontrado
                    return sugerencia['entities'][0]['destinationId']
        return None
    else:
        print(f"Error al obtener el código de la ciudad: {response.status_code}")
        return None


def buscar_hoteles(city_code, check_in, check_out, adultos):
    url = "https://hotels4.p.rapidapi.com/properties/list"

    querystring = {
        "destinationId": city_code,
        "pageNumber": "1",
        "checkIn": check_in,
        "checkOut": check_out,
        "pageSize": "25",
        "adults1": adultos,
        "currency": "USD"
    }

    headers = {
        "X-RapidAPI-Key": "6a4c71839fmshffbeb71f0be5f4cp1eba34jsn6ce698b5ea40",
        "X-RapidAPI-Host": "hotels4.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error al buscar hoteles: {response.status_code}")
        return None
