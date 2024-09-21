from App import db
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    presupuesto = db.Column(db.String(50), nullable=False)
    ubicacion = db.Column(db.String(100), nullable=False)