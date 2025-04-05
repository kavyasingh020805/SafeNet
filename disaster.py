from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..models import DisasterReport, db

disaster_bp = Blueprint('disaster', __name__)

@disaster_bp.route('/report', methods=['POST'])
@jwt_required()
def report_disaster():
    user_id = get_jwt_identity()
    data = request.get_json()
    report = DisasterReport(user_id=user_id, location=data['location'], description=data.get('description'))
    db.session.add(report)
    db.session.commit()
    return jsonify({"msg": "Disaster reported"}), 201

@disaster_bp.route('/safe-zones', methods=['GET'])
def safe_zones():
    # Placeholder: This can be connected to OpenStreetMap API or DB data
    zones = [
        {"name": "Community Hall A", "lat": 12.93, "lng": 80.13},
        {"name": "School Shelter B", "lat": 12.94, "lng": 80.12}
    ]
    return jsonify(zones)