from App import db

class UserRecommendationHistory(db.Model):
    __tablename__ = 'user_recommendations_history'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    recommendation_id = db.Column(db.Integer, db.ForeignKey('recomendacion.id'), nullable=False)
    selected_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    user = db.relationship('User', backref='recommendation_history', lazy=True)
    recommendation = db.relationship('Recomendacion', backref='user_history', lazy=True)

