from sqlalchemy import Column, TEXT, BIGINT, DateTime, sql, VARCHAR
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
from src.models.db import *

base = declarative_base()


class userTable(base):
    __tablename__ = "user"

    id = Column(VARCHAR(16), nullable=False, primary_key=True)
    email = Column(TEXT, nullable=False)
    pswd = Column(TEXT, nullable=False)
    point = Column(BIGINT, default=0)
    regDate = Column(DateTime(timezone=True), server_default=sql.func.now())


class sessionController(base):
    __tablename__ = "session"

    id = Column(VARCHAR(16), nullable=False, primary_key=True)
    code = Column(TEXT, nullable=False)


def getUser(db: Session, id: str, pswd: str):
    return db.query(userTable).filter(userTable.id == id, userTable.pswd == pswd).first()


def getSession(db: Session, id: str):
    return db.query(sessionController).filter(sessionController.id == id).first()


async def createUser(db: Session, id: str, pswd: str, email: str):
    userData = userTable(
        id=id,
        pswd=pswd,
        email=email
    )

    db.add(userData)
    db.commit()
    db.refresh(userData)

    return userData

base.metadata.create_all(bind=conn.getEngine())
