from App import db

class Recomendacion(db.Model):
    __tablename__ = 'recomendacion'
    
    id = db.Column(db.Integer, primary_key=True)
    destino = db.Column(db.String(100), nullable=False)
    actividad = db.Column(db.String(100), nullable=False)
    epoca = db.Column(db.String(50), nullable=False)
    presupuesto = db.Column(db.String(50), nullable=False)
    latitud = db.Column(db.Float, nullable=False)
    longitud = db.Column(db.Float, nullable=False)

    __table_args__ = {'extend_existing': True}
