from _env_ import Env
from pymongo import MongoClient

class Database:
    def __init__(self):
        self.client = MongoClient(Env('MONGODB_URL').value)

    def insert(self, collection: str, item: {}):
        print('Inserted => ', self.client.ufsc[collection].insert_one(item).inserted_id)
