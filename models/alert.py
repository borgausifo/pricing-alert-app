from typing import List, Dict
from models.item import Item
from models.model import Model
import uuid


class Alert(Model):
    collection = 'alerts'

    def __init__(self, item_id: str, price_limit: float, _id: str = None):
        super().__init__()
        self.item_id = item_id
        self.item = Item.get_by_id(item_id)
        self.price_limit = price_limit
        self._id = _id or uuid.uuid4().hex

    def json(self) -> Dict:
        return {
            'id': self._id,
            'price': self.price_limit,
            'item_id': self.item_id
        }

    # def save_to_mongo(self):
    #     Database.insert(self.collection, self.json())

    def load_item_price(self) -> float:
        self.item.load_price()
        return self.item.price

    def notify_if_price_reached(self):
        if self.item.price < self.price_limit:
            print(f'Item {self.item} has reached the price under {self.price_limit}.')

    # @classmethod # Don't need it because of models.model metaclass section
    # def all(cls) -> List:
    #     alerts_from_db = Database.find('alerts', {})
    #     return [cls(**alert) for alert in alerts_from_db]
