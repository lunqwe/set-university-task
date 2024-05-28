from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from app import create_app, db


app = create_app()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)