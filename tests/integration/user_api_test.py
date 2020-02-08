import pytest
from app import create_app, db
from app.models import User
import json


@pytest.fixture
def web():
    app = create_app('testing')
    ctx = app.app_context()
    ctx.push()

    db.create_all()

    yield app.test_client()

    db.drop_all()
    db.session.remove()
    
    ctx.pop()


def test_add_user(web, snapshot):
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    payload = {'name': 'Maria Marina', 'email': 'marina@maria.com'}

    response = web.post('/api/v1/users', data=json.dumps(payload), headers=headers)

    snapshot.assert_match(response.json)
    # assert response.json['message'] == 'Usuário cadastro com sucesso!'



def test_user_api(web, snapshot):
    user = User()
    user.name = 'Welinton'
    user.email = 'welinton.ti@gmail.com'

    user1 = User()
    user1.name = 'Felipe Subtil'
    user1.email = 'felipe.ti@gmail.com'

    user2 = User()
    user2.name = 'Gabriel'
    user2.email = 'gabriel.ti@gmail.com'



    db.session.add(user)
    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()

    response = web.get('/api/v1/users')

    # Default
    # assert response.status_code == 200
    # assert response.json[0]['name'] == 'Welinton'
    # assert response.json[0]['email'] == 'welinton.ti@gmail.com'

    # Libs
    snapshot.assert_match(response.json)

