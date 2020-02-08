from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from config import config

db = SQLAlchemy()
ma = Marshmallow()

def create_app(config_name: str):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    db.init_app(app)
    ma.init_app(app)

    @app.route('/api/v1/users')
    def users():
        return 'Lista de usuários'

    return app