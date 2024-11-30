from App import db

class Accommodation(db.Model):
    __tablename__ = 'accommodation'

    id = db.Column(db.Integer, primary_key=True)
    destination = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    price_per_night = db.Column(db.Float, nullable=False)
