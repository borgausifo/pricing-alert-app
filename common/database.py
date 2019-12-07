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

    @staticmethod
    def find(collection: str, query: Dict) -> pymongo.cursor:
        """ Returns the cursor which something to iterate over."""
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection: str, query: Dict) -> Dict:
        """ Returns the dictionary """
        return Database.DATABASE[collection.find_one(query)]

    @staticmethod
    def update(collection: str, query: Dict, data: Dict) -> None:
        Database.DATABASE[collection].update(query, data, upsert = True)

    @staticmethod
    def remove(colletion: str, query: Dict) -> Dict:
        Database.DATABASE[colletion].remove(query)



