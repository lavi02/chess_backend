from sqlalchemy import *
from sqlalchemy.orm import sessionmaker

DB_URL = "mysql://b1cf2990e2ad14:9fe0323a@us-cdbr-east-06.cleardb.net/heroku_d4ca10f7d3f34a6"


class engineConnect:
    def __init__(self):
        self.engine = create_engine(DB_URL, encoding='utf-8')

    def engineSession(self):
        session = sessionmaker(
            bind=self.engine, autocommit=False, autoflush=False)
        Session = session()

        return Session

    def getEngine(self):
        return self.engine

    def connect(self):
        conn = self.engine.connect()
        return conn


conn = engineConnect()


def get_db():
    dbSession = conn.engineSession()
    try:
        yield dbSession
    finally:
        dbSession.close()
