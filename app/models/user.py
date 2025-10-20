from sqlmodel import SQLModel, Field
from sqlalchemy import String, Integer, Text, Column, DateTime, ForeignKey, func


class User(SQLModel, table=True):
    __tablename__ = 'users'
    id: int = Field(sa_column=Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        comment="Primary key ID",
        nullable=False,
    ))
    name: str = Field(sa_column=Column(
        String(255),
        nullable=False,
        comment="Name of the user"
    ))
    age: int = Field(default=None, index=True)
    # note: str = 
