from datetime import datetime

from sqlalchemy import Column, String, TIMESTAMP
from sqlmodel import SQLModel


class User(SQLModel, table=True):
    name: str = Column(sa_type=String(255), nullable=False)
    email: str = Column(sa_type=String(255), nullable=False)
    password: str = Column(sa_type=String(255), nullable=False)
    created_at: datetime = Column(sa_type=TIMESTAMP, nullable=False)
    updated_at: datetime = Column(sa_type=TIMESTAMP, nullable=False)

    __tablename__ = "users"
