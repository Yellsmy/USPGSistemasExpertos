from App import db

class ClimateData(db.Model):
    __tablename__ = 'climate_data'

    id = db.Column(db.Integer, primary_key=True)
    destination = db.Column(db.String(100), nullable=False)
    month = db.Column(db.Integer, nullable=False)
    temperature_min = db.Column(db.Float, nullable=False)
    temperature_max = db.Column(db.Float, nullable=False)
    season = db.Column(db.String(50), nullable=False)
