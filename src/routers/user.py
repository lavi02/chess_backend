from fastapi.responses import JSONResponse
from fastapi import status, Depends
from datetime import datetime, timedelta
from pydantic import BaseModel
import jwt

from src.conn import *
from src.models.__users__ import *

SECRET_KEY = "xxxz#0007TuNa#31578"
SECRET_HASH = "HS256"


class userTemplate(BaseModel):
    id: str
    pswd: str
    email: str


def accessToken(id: str):
    encodeData = {
        'UA': id,
        'exp': datetime.utcnow() + timedelta(seconds=60 * 60 * 24)
    }
    token = jwt.encode(encodeData, SECRET_KEY, SECRET_HASH)

    return token


@app.post("/api/v1/register")
async def register(user: userTemplate, db: Session = Depends(get_db)):
    checkUserStatus = getUser(db, user.id, user.pswd)

    if checkUserStatus:
        return JSONResponse(status_code=status.HTTP_409_CONFLICT, content="user already exist.")
    else:
        try:
            createUser(db, user.id, user.pswd, user.email)
            return JSONResponse(status_code=status.HTTP_201_CREATED, content="successfully generated.")

        except Exception as e:
            return JSONResponse(status_code=status.HTTP_424_FAILED_DEPENDENCY, content=str(e))


@app.get("/api/v1/login")
async def login(id: str, pswd: str, db: Session = Depends(get_db)):
    try:
        checkUserStatus = getUser(db, id, pswd)

        if checkUserStatus:
            userToken = accessToken(id)
            print(userToken)
            return JSONResponse(status_code=status.HTTP_200_OK, content=userToken)
        else:
            return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content="login failed.")
    except Exception as e:
        return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content=str(e))
