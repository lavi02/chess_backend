from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.conn import app
from backend.test.__init__ import testInit
from src.models.__users__ import base
from src.models.db import *

engineTest = create_engine(DB_URL, conneect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engineTest)
base.metadata.create_all(bind=engineTest)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    except:
        db.close()


app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)


class dbTest(testInit):
    def testCreateUser():
        res = client.post(
            "/api/v1/register", json={"id": "testuser", "pswd": "test1234", "email": "zerosec7@hanyang.ac.kr"})
        assert res.status_code == 200, res.text
