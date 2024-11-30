from App.ML.predict import generate_recommendations

def get_personalized_recommendations(data, user_id):
    recommendations = generate_recommendations(data)
    return recommendations
