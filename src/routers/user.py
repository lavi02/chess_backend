from fastapi.responses import JSONResponse
from fastapi import status, Depends
from pydantic import BaseModel

from src.conn import *
from src.models.__users__ import *


class userTemplate(BaseModel):
    id: str
    pswd: str
    email: str


@app.post("/api/v1/register")
async def register(user: userTemplate, db: Session = Depends(get_db)):
    checkUserStatus = getUser(db, user.id, user.pswd)
    print(checkUserStatus.id)

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
            return JSONResponse(status_code=status.HTTP_200_OK, content="successfully login.")
        else:
            return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content="login failed.")
    except:
        return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content="login failed.")
