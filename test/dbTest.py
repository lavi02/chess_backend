from fastapi import Depends
from fastapi.testclient import TestClient

from src.conn import app
from backend.test.__init__ import testInit
from src.models.__users__ import *
from src.models.db import *
from src.conn import *

client = TestClient(app)


class dbTest(testInit):
    def testCreateUser(self, db: Session = Depends(get_db)):
        res = client.post(
            "/api/v1/register", json={"id": "testuser", "pswd": "test1234", "email": "zerosec7@hanyang.ac.kr"})
        assert res.status_code == 200, res.text

        resGet = client.get("/api/v1/login?id=testuser&pswd=test1234")
        assert resGet.status_code == 200, resGet.text

        db.delete(resGet)
        db.commit()
