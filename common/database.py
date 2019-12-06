from typing import Dict
import pymongo


class Database:
    DATABASE = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(host='localhost', port=27017)
        Database.DATABASE = client['pricing']

    @staticmethod
    def insert(collection: str, data: Dict):
        Database.DATABASE[collection].insert(data)
