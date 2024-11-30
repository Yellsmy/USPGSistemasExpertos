#from .usuarios import Usuario
#from .recomendaciones import Recomendacion

# Importar todos los modelos aquí
'''from .recomendaciones import Recomendacion
from .pronostico import Pais, Temporada, Pronostico, Clima

# Exponer db para ser reutilizado
from App import db

__all__ = ['Recomendacion', 'Pais', 'Temporada', 'Pronostico', 'Clima', 'db']'''
#from .usuarios import Usuario
#from .recomendaciones import Recomendacion

# Importar todos los modelos aquí
from .recomendaciones import Recomendacion
from .pronostico import Pais, Temporada, Pronostico, Clima
from .activities import Activity  # Nuevo modelo de actividades
from .accommodation import Accommodation  # Nuevo modelo de alojamiento
from .restaurants import Restaurant  # Nuevo modelo de restaurantes

# Exponer db para ser reutilizado
from App import db

__all__ = [
    'Recomendacion',
    'Pais',
    'Temporada',
    'Pronostico',
    'Clima',
    'Activity',
    'Accommodation',
    'Restaurant',
    'db',
    'UserRecommendationHistory'
]


