import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Development:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'dev.sqlite')

class Testing:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'testing.sqlite')

config = dict(
    development = Development(),
    testing = Testing()
)

