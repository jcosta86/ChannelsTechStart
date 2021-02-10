from dao.base_dao import BaseDao
from models.buyer import Buyer


class BuyerDao(BaseDao):
    def __init__(self):
        super().__init__(Buyer)

    def update(self, model: Buyer):
        return super().save(model)
