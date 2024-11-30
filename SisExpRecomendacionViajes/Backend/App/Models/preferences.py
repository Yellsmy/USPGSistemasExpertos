from App import db

class Preference(db.Model):
    __tablename__ = 'preferences'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    climate_preference = db.Column(db.String(50))
    budget = db.Column(db.String(50))
    accommodation_type = db.Column(db.String(50))
    activities = db.Column(db.String(255))
    people_count = db.Column(db.Integer)
    travel_date = db.Column(db.Date)
