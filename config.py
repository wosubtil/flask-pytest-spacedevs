import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Development(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + \
        os.path.join(basedir, 'dev.sqlite')


class Testing(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + \
        os.path.join(basedir, 'testing.sqlite')


config = dict(
    development=Development(),
    testing=Testing()
)
