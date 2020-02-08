from app import create_app, db
from app.models import User

app = create_app('development')


@app.shell_context_processor
def make_context_processor():
    return dict(
        app=app,
        db=db,
        User=User
    )


if __name__ == '__main__':
    app.run(debug=True)
