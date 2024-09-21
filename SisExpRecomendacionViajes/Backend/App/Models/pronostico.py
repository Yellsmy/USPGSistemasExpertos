from App import db

# Modelo para los países
class Pais(db.Model):
    __tablename__ = 'paises'
    
    id_pais = db.Column(db.Integer, primary_key=True)
    pais = db.Column(db.String(100), nullable=False)

    regiones = db.relationship('Region', backref='pais', lazy=True)

# Modelo para las regiones
class Region(db.Model):
    __tablename__ = 'regiones'
    
    id_region = db.Column(db.Integer, primary_key=True)
    region = db.Column(db.String(100), nullable=False)
    id_pais = db.Column(db.Integer, db.ForeignKey('paises.id_pais'), nullable=False)

# Modelo para las temporadas
class Temporada(db.Model):
    __tablename__ = 'temporadas'
    
    id_temporada = db.Column(db.Integer, primary_key=True)
    temporada = db.Column(db.String(50), nullable=False)

# Modelo para el pronóstico
class Pronostico(db.Model):
    __tablename__ = 'pronostico'
    
    id_pronostico = db.Column(db.Integer, primary_key=True)
    id_temporada = db.Column(db.Integer, db.ForeignKey('temporadas.id_temporada'), nullable=False)
    id_pais = db.Column(db.Integer, db.ForeignKey('paises.id_pais'), nullable=False)
    id_region = db.Column(db.Integer, db.ForeignKey('regiones.id_region'), nullable=True)
    mes_inicio = db.Column(db.String(50), nullable=False)
    mes_fin = db.Column(db.String(50), nullable=False)

    temporada = db.relationship('Temporada', backref='pronosticos', lazy=True)
    
    pais = db.relationship('Pais', backref='pronosticos', lazy=True)
    
    region = db.relationship('Region', backref='pronosticos', lazy=True)

# Modelo para el clima
class Clima(db.Model):
    __tablename__ = 'clima'
    
    id_clima = db.Column(db.Integer, primary_key=True)
    id_temporada = db.Column(db.Integer, db.ForeignKey('temporadas.id_temporada'), nullable=False)
    clima = db.Column(db.String(50), nullable=False)
    temperatura_min = db.Column(db.Float, nullable=False)
    temperatura_max = db.Column(db.Float, nullable=False)
    humedad = db.Column(db.Integer, nullable=False)
    velocidad_viento = db.Column(db.Float, nullable=False)
    dia = db.Column(db.Integer, nullable=False)

    temporada = db.relationship('Temporada', backref='climas', lazy=True)
