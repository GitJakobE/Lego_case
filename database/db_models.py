#mocked
# this will include the models used matching the pydantic schemas
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from .database import Base


class LegoColor(Base):
    __tablename__ = "LegoColors"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    color_hex = Column(String, unique=True)
    in_production = Column(Boolean)

#ect for all the other tables