from flask_login import UserMixin
import bcrypt
from enum import Enum

from config import Config
from .database import db



class User(UserMixin, db.Model):
    
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=True)
    password = db.Column(db.String(120), nullable=True)
    role = db.Column(db.Enum('admin', 'manager', 'analyst'), nullable=False)
    group = db.Column(db.Enum('customer1', 'customer2', 'customer3', 'all'), nullable=False, default='customer1')
    
    def set_password(self, password):
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        
    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))
    
class Ticket(db.Model):
    
    __tablename__ = 'tickets'
    
    id = db.Column(db.Integer, primary_key=True, name='id')
    status = db.Column(db.Enum('pending', 'in_review', 'closed'), nullable=False)
    note = db.Column(db.Text, nullable=True, name='note')
    group = db.Column(db.Enum('customer1', 'customer2', 'customer3'), nullable=False)
    

    
    