from App import db
class ClimateHistory(db.Model):
    __tablename__ = 'climate_history'
    idClimaHistory = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, nullable=False)
    temperature_min = db.Column(db.Float, nullable=False)
    temperature_max = db.Column(db.Float, nullable=False)
    precipitation = db.Column(db.Float, nullable=False)
    season = db.Column(db.String(50), nullable=False)
