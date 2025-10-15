from sqlmodel import SQLModel, Field

class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True, index=True)
    name: str = Field(default=None, max_length=100)
    age: int = Field(default=None, index=True)
    