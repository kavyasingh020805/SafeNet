from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from config import Config
from flask_cors import CORS

db = SQLAlchemy()
bcrypt = Bcrypt()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    CORS(app) 
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    from .routes.auth import auth_bp
    from .routes.disaster import disaster_bp
    from .routes.relief import relief_bp

    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(disaster_bp, url_prefix='/api/disaster')
    app.register_blueprint(relief_bp, url_prefix='/api/relief')

    @app.route('/api/hello', methods=['GET'])
    def hello():
        return {"message": "Hi Kavya! Backend is working 🎉"}, 200

    return app
