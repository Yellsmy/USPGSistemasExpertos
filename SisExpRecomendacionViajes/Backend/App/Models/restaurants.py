from App import db

class Restaurant(db.Model):
    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, primary_key=True)
    destination = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    cuisine = db.Column(db.String(50))
    price_per_person = db.Column(db.Float, nullable=False)
