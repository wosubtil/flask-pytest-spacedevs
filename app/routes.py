from flask import jsonify

from app.models import User
from app.schemas import UserSchema

def load(app):
    @app.route('/api/v1/users')
    def users():
        users = User.query.all()
        users_schema = UserSchema(many=True)
        result = users_schema.dump(users)
        return jsonify(result)

    return app
