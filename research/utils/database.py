from utils.env import Env
from pymongo import MongoClient

class Database:
    def __init__(self):
        self.client = MongoClient(Env('MONGODB_URL').value)

    def insert(self, collection, item: {}):
        print('Inserted one => ', self.client.ufsc[collection].insert_one(item).inserted_id)