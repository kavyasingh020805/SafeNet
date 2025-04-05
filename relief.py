from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..models import ReliefRequest, db

relief_bp = Blueprint('relief', __name__)

@relief_bp.route('/request', methods=['POST'])
@jwt_required()
def request_relief():
    user_id = get_jwt_identity()
    data = request.get_json()
    relief = ReliefRequest(user_id=user_id, request_type=data['request_type'], details=data['details'])
    db.session.add(relief)
    db.session.commit()
    return jsonify({"msg": "Relief request submitted"}), 201

@relief_bp.route('/volunteer', methods=['POST'])
@jwt_required()
def register_volunteer():
    # For now, just log the intent
    user_id = get_jwt_identity()
    return jsonify({"msg": f"User {user_id} registered as volunteer"})