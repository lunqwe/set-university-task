import os
from flask import Flask
from flask_login import LoginManager

from app.models import User
from database import db


class Config:
    SECRET_KEY = 'super_secret_key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    

login_manager = LoginManager()



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    login_manager.init_app(app)
    
    from app.urls import router as ticket_router
    app.register_blueprint(ticket_router)
    
    return app