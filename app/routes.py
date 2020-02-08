from flask import jsonify, request

from app.models import User
from app.schemas import UserSchema
from app import db


def load(app):
    @app.route('/api/v1/users', methods=['POST'])
    def add_user():
        user = request.json

        u = User()
        u.name = user['name']
        u.email = user['email']

        db.session.add(u)
        db.session.commit()

        return jsonify(dict(message='User successfully registered'))

    @app.route('/api/v1/users')
    def users():
        users = User.query.all()
        users_schema = UserSchema(many=True)
        result = users_schema.dump(users)
        return jsonify(result)

    return app
