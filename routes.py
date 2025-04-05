from flask import Blueprint, request, jsonify

main = Blueprint('main', __name__)

@main.route('/api/aid-request', methods=['POST'])
def aid_request():
    data = request.get_json()
    
    # Just a sample to print the request data
    print("Received Aid Request:", data)

    # Here you would store it into PostgreSQL
    return jsonify({"message": "Aid request received", "data": data}), 201
