from sqlmodel import SQLModel, Field

class Division(SQLModel, table=True):
    __tablename__ = 'divisions'
    id: int = Field(default=None, primary_key=True, index=True)
    name: str = Field(max_length=100)