from sqlalchemy import  column, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True
    id_ = column('id', Integer, primary_key=True)
