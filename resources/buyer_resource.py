from flask_restful import fields, marshal_with

from resources.base_resource import BaseResource
from dao.buyer_dao import BuyerDao
from models.buyer import Buyer


class BuyerResource(BaseResource):
    fields = {
        "id": fields.Integer,
        "name": fields.String,
        "address" : fields.String,
        "phone": fields.String,
        "zip_code": fields.String,
        "state": fields.String,
        "city": fields.String,
        "id_channel": fields.Integer
    }
    
    def __init__(self):
        self.__dao = BuyerDao()
        self.__model_type = Buyer

        super().__init__(self.__dao, self.__model_type)
        
    @marshal_with(fields)
    def get(self, id=None):
        return super().get(id)

    @marshal_with(fields)
    def post(self):
        return super().post()

    @marshal_with(fields)
    def put(self, id):
        return super().put(id)

    @marshal_with(fields)
    def delete(self, id):
        return super().delete(id)
