from sqlalchemy import Column, String, Integer, ForeignKey

from models.base_model import BaseModel
from utils.validators import (
    validate_len, 
    validate_not_empty,
    validate_type
)



class Buyer(BaseModel):
    
    __tablename__ = 'buyer'

    name = Column('name', String(length=100), nullable = False)
    address = Column("address", String(length=200), nullable = False)
    phone = Column('phone', String(length=50), nullable = False)
    zip_code = Column('zip_code', String(length=50), nullable = False)
    state = Column('state', String(length=50), nullable = False)
    city = Column('city', String(length=50), nullable = False)
    id_channel = Column('id_channel', Integer, ForeignKey('channels.id'), nullable=False)

    @validates('name')
    def validate_name(self, key, name):
        name = validate_type(key, name, str)
        name = validate_not_empty(key, name)
        return validate_len(key, name, 100)
    
    @validates('address')
    def validate_adress(self, key, address):
        address = validate_type(key, address, str)
        address = validate_not_empty(key, address)
        return validate_len(key, address, 200)
        
    @validates('phone')
    def validate_phone(self, key, phone):
        phone = validate_type(key, phone, str)
        phone = validate_not_empty(key, phone)
        return validate_len(key, phone, 50)
    
    @validates('zip_code')
    def validate_zip_code(self, key, zip_code):
        zip_code = validate_type(key, zip_code, str)
        zip_code = validate_not_empty(key, zip_code)
        return validate_len(key, zip_code, 50)
    
    @validates('state')
    def validate_state(self, key, state):
        state = validate_type(key, state, str)
        state = validate_not_empty(key, state)
        return validate_len(key, state, 50)
        
    @validates('city')
    def validate_city(self, key, city):
        city = validate_type(key, city, str)
        city = validate_not_empty(key, city)
        return validate_len(key, city, 50)
            
    @validates('id_channel')
    def validate_id_channel(self, key, id_channel):
        id_channel = validate_type(key, id_channel, int)
        return validate_not_empty(key, id_channel)
