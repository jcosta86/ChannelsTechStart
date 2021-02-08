from flask_restful import fields, marshal_with

from dao.channels_dao import ChannelsDao
from models.channels_model import Channels
from resources.base_resource import BaseResource


class ChannelsResource(BaseResource):
    fields = {
        "id_": fields.Integer,
        "name": fields.String,
        "description": fields.String,
        "contact": fields.String,
        "url": fields.String,
        "rate": fields.Float
    }

    def __init__(self):
        self.__dao = ChannelsDao()
        self.__model_type = Channels

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
