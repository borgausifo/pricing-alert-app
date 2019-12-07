from abc import ABCMeta, abstractmethod
from common.database import Database
from typing import List, TypeVar, Type, Dict
''' Check back in to metaclass in Python 
'''

T =TypeVar('T', bound='Model')

class Model(ABCMeta):
    collection = str #'models'
    _id: str

    def __init__(self, *args, **kwargs):
        pass

    def save_to_mongo(self):
        Database.update(self.collection, {'id': self._id}, self.json())

    def remove_from_mongo(self):
        Database.remove(self.collection, {'id': self._id})

    @abstractmethod
    def json(self) -> Dict:
        raise NotImplemented

    @classmethod
    def get_by_id(cls: Type[T], _id:str) ->  T: #"Model"  Item.get_by_id() -> Item, Alert.get_by_id -> Alert
        return cls.find_one_by('_id', _id)

    @classmethod
    def all(cls: Type[T]) -> List[T]:
        elements_from_db = Database.find(cls.collection, {})
        return [cls(**elem) for elem in elements_from_db]

    @classmethod
    def find_one_by(cls: Type[T], attribute: str, value: str) -> T:
        """Single element return"""
        return cls(**Database.find_one((cls.collection, {attribute: value}))

    @classmethod
    def find_many_by(cls: Type[T], attribute: str, value: str) -> List[T]:
        return [cls(**elem) for elem in Database.find(cls.collection, {attribute: value})]
