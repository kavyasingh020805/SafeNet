import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'safenet-secret-key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://username:password@localhost/safenet_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False