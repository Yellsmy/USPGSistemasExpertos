from amadeus import Client, ResponseError
import requests

amadeus = Client(
    client_id='PS1CSGLwXLs4qwOwrmWdyFNvfqRJ0kPt',
    client_secret='u3bNADcvM8s655fM'
)

# Función para buscar vuelos
def buscar_vuelos(origen, destino, fecha_salida, adultos):
    try:
        response = amadeus.shopping.flight_offers_search.get(
            originLocationCode=origen,
            destinationLocationCode=destino,
            departureDate=fecha_salida,
            adults=adultos
        )
        return response.data
    except ResponseError as error:
        print(f"Error en la búsqueda de vuelos: {error}")
        return None

# Función para buscar hoteles
def buscar_hoteles(ciudad, checkin, checkout, adultos):
    # Install the Python library from https://pypi.org/project/amadeus
#from amadeus import Client, ResponseError

    try:
        '''
        Confirm availability and price from SYD to BKK in summer 2022
        '''
        flights = amadeus.shopping.flight_offers_search.get(originLocationCode='SYD', destinationLocationCode='BKK',
                                                            departureDate='2024-07-01', adults=1).data
        response_one_flight = amadeus.shopping.flight_offers.pricing.post(
            flights[0])
        print(response_one_flight.data)

        response_two_flights = amadeus.shopping.flight_offers.pricing.post(
            flights[0:2])
        print(response_two_flights.data)
    except ResponseError as error:
        raise error



def obtener_token_amadeus(client_id, client_secret):
    url = 'https://test.api.amadeus.com/v1/security/oauth2/token'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret
    }

    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 200:
        return response.json()['access_token']
    else:
        print(f"Error al obtener el token de Amadeus: {response.status_code}")
        return None
