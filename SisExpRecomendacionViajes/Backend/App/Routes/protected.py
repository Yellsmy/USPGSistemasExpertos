from flask import Blueprint, jsonify
from App.Services.auth_middleware import token_required

protected_bp = Blueprint('protected', __name__)

@protected_bp.route('/protected', methods=['GET'])
@token_required
def protected_route():
    return jsonify({"message": "This is a protected route"}), 200
