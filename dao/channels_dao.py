from dao.base_dao import BaseDao
from models.channels_model import Channels


class ChannelsDao(BaseDao):
    def __init__(self):
        super().__init__(Channels)

    def update(self, model: Channels):
        return super().save(model)
