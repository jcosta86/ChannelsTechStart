from sqlalchemy import Column, String, Float
from sqlalchemy.orm import validates
from models.base_model import BaseModel
from utils.validators import (
    validate_len, 
    validate_not_empty,
    validate_type
)


class Channels(BaseModel):
    __tablename__ = 'channels'
    name = Column('name', String(length=100), nullable = False)
    description = Column('description', String(length=255), nullable = True)
    contact = Column('contact', String(length=100), nullable = False)
    url = Column('url', String(length=100), nullable = False)
    rate = Column('rate', Float(length=20), nullable = False)

    def __init__(self, name: str, description: str, contact: str, url: str, rate:float) -> None:
        self.name = name
        self.description = description
        self.contact = contact
        self.url = url 
        self.rate = rate

    @validates('name')
    def validate_name(self, key, name):
        name = validate_type(key, name, str)
        name = validate_not_empty(key, name)
        return validate_len(key, name, 100)

    @validates('description')
    def validate_description(self, key, description):
        description = validate_type(key, description, str)
        return validate_len(key, description, 255)

    @validates('contact')
    def validate_contact(self, key, contact):
        contact = validate_type(key, contact, str)
        contact = validate_not_empty(key, contact)
        return validate_len(key, contact, 100)

    @validates('url')
    def validate_url(self, key, url):
        url = validate_type(key, url, str)
        url = validate_not_empty(key, url)
        return validate_len(key, url, 100)

    @validates('rate')
    def validate_rate(self, key, rate):
        rate = validate_type(key, rate, float)
        rate = validate_not_empty(key, rate)
        return validate_len(key, rate, 100)
