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


def getUser(db: Session, id: str, pswd: str):
    return db.query(userTable).filter(userTable.id == id, userTable.pswd == pswd).first()


async def createUser(db: Session, id: str, pswd: str, email: str):
    userData = userTable(
        id=id,
        pswd=pswd,
        email=email
    )

    db.add(userData)
    await db.commit()
    db.refresh(userData)

    return userData

base.metadata.create_all(bind=conn.getEngine())
