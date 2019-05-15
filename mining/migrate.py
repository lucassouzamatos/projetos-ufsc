import os
import xlrd

from pymongo import MongoClient
from _env_ import Env
from normalizer import Normalizer

class Migrate:
    def __init__(self, doc):
        data = xlrd.open_workbook(doc)
        sheet = data.sheet_by_index(0)

        client = MongoClient(Env('MONGODB_URL').value)

        for item in self.normalizer(sheet):
            print('Inserted => ', client.ufsc.projetos.insert_one(item).inserted_id)

    def normalizer(self, sheet):
        for i in range(sheet.nrows):
            yield Normalizer().get('ufsc', sheet, i)
