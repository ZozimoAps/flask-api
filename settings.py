class Database:
    def __init__(self, database, driver, user, password, host, port, namedb):
        self.database = database
        self.driver = driver
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.namedb = namedb

    def database_uri(self):
        return f'{self.database}+{self.driver}://{self.user}:{self.password}@{self.host}:{self.port}/{self.namedb}'


class Base:
    DEBUG = bool
    ENV = 'production'
    TESTING = bool


class Develop(Base):
    DEBUG = True
    ENV = 'development'
    DATABASE = Database(
        database='postgresql',
        driver='psycopg2',
        user='postgres',
        password='admin',
        host='127.0.0.1',
        port=5432,
        namedb='api'
    )
    SQLALCHEMY_DATABASE_URI = DATABASE.database_uri()
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class Test(Base):
    DEBUG = False
    ENV = 'development'
    DATABASE = Database(
        database='postgresql',
        driver='psycopg2',
        user='postgres',
        password='admin',
        host='127.0.0.1',
        port=5432,
        namedb='api_test'
    )
    SQLALCHEMY_DATABASE_URI = DATABASE.database_uri()
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Prod(Base):
    DEBUG = False


environment = dict()
environment['develop'] = Develop
environment['production'] = Prod
environment['test'] = Test
