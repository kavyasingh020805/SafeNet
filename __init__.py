from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from config import Config
from flask_cors import CORS
from .routes import main
from .models import db, AidRequest 

import psycopg2
from flask import Flask, request, jsonify
from flask_cors import CORS


db = SQLAlchemy()
bcrypt = Bcrypt()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    CORS(app) 
    app.config.from_object(Config)

    app.register_blueprint(main)

    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    with app.app_context():
    db.create_all()

    from .routes.auth import auth_bp
    from .routes.disaster import disaster_bp
    from .routes.relief import relief_bp

    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(disaster_bp, url_prefix='/api/disaster')
    app.register_blueprint(relief_bp, url_prefix='/api/relief')

    @app.route('/api/hello', methods=['GET'])
    def hello():
        return {"message": "Hi Kavya! Backend is working 🎉"}, 200
    
    CORS(app)

@app.route('/api/aid-request', methods=['POST'])
def handle_aid_request():
    data = request.json

    name = data.get('name')
    contact = data.get('contact')
    location = data.get('location')
    aid_type = data.get('type_of_aid')
    description = data.get('description')

    try:
        conn = psycopg2.connect(
            host="localhost",
            database="safenetdb",
            user="postgres",  # default user
            password="abcd@1234"  # replace with your actual password
        )
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO aid_requests (name, contact, location, type_of_aid, description)
            VALUES (%s, %s, %s, %s, %s)
        """, (name, contact, location, aid_type, description))

        conn.commit()
        cur.close()
        conn.close()

        return jsonify({"message": "Aid request submitted successfully!"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class AidRequest(db.Model):
    __tablename__ = 'aid_requests'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    phone = db.Column(db.String(20))
    location = db.Column(db.String(200))
    need_type = db.Column(db.String(100))
    description = db.Column(db.String(300))

@app.route('/api/aid-request', methods=['POST'])
def submit_aid_request():
    data = request.get_json()
    name = data.get('name')
    phone = data.get('phone')
    location = data.get('location')
    description = data.get('description')

    conn = psycopg2.connect(
        host='localhost',
        dbname='safenetdb',
        user='postgres',
        password='abcd@1234',
        port='5432'
    )
    cur = conn.cursor()
    cur.execute("INSERT INTO aid_requests (name, phone, location, description) VALUES (%s, %s, %s, %s)",
                (name, phone, location, description))
    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"message": "Aid request submitted successfully"}), 200

    
    return app